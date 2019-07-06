import traceback
import sys
import os

import logging
from time import sleep
from datetime import datetime, timedelta

from .SWF import SWF
from .SWFExecution import SWFExecution
from .SWFEvent import parse_event_list
from .utils import dpath

class ApiReqeustFailed(Exception): pass
class CantHandleDecsionTask(Exception): pass


class CantHandleDecision(Exception): pass


class SWFDeciderRouter(SWF):
    '''
    Process that queries the SWF endpoints and applies makes decisions on workflow execution.

    In SWF, a decider process determines what the next steps are in an executing workflow.

    Because a single decider process can server multiple Workflow Types (SWFWorkflows), this
    decider class polls for any decision tasks in a given tasklist (AWS SWF queue).  It relies
    on SWFWorkflowDecider instances to provide the logic for a given workflow type.  If a decision
    task is received and no SWFWorkflowDecider has been added to handle that type, then the
    decider will respond with an error (SWF failWorkflowExecutionDecisionAttributes)

    '''

    def __init__(self, domain, identity, task_list, creds):
        '''
        :param domain: Name of the domain in SWF to poll for decisions in.
        :param identity: String to identify this decider in the workflow history
        :param task_list:
            Name of the task list to poll for decisions in.
            (task lists are basically SWF queues)

        '''

        super(SWFDeciderRouter, self).__init__(creds=creds)

        self.log = logging.getLogger(__name__)

        self.domain = domain
        self.identity = str(identity)
        self.task_list = str(task_list)

        self.__deciders = dict() # [wfname, wfver] = SWFDecisionHander()


    def add(self, decider):
        '''
        Add a decision handler for a given Workflow

        :param decider: SWFWorkflowDecider
        '''
        key = (decider.wfname, decider.wfver)
        if key in self.__deciders:
            raise KeyError("A decider alread exists for %s.%s" % (decider.wfname, decider.version))
        self.__deciders[key] = decider


    def poll_forever(self):
        '''Keep polling the SWF service to find decions that need to be made'''
        while True:
            try:
                self.poll_once()
            except Exception as e:
                self.log.error("Exception during poll_once(): " + str(e))


    def poll_once(self):
        '''Call the SWF poll_for_decision_task API'''
        task_token = None

        # Get next task
        task = self._get_next_decsion_task()
        if task is None:
            return

        task_token = dpath(task, 'taskToken', default=None)
        task_desc = "{task_id} ({wf}.{ver})".format(
            task_id = dpath(task, 'workflowExecution', 'workflowId'),
            wf = dpath(task, 'workflowType', 'name'),
            ver = dpath(task, 'workflowType', 'version'),
        )

        # Pass to handler to continue
        try:
            decider = self._select_handler(task)

            try:
                decider.reset()
                decider.handle(
                    execution = SWFExecution(
                        run_id = dpath(task, 'workflowExecution', 'runId'),
                        exec_name = dpath(task, 'workflowExecution', 'workflowId'),
                        copyfrom = decider, # Decider subclasses SWFWorkflow, so this works
                    ),
                    events = parse_event_list(self._retrieve_all_events(task)),
                    decision_event_id = dpath(task, 'startedEventId'),
                    task_token = task_token)
            except Exception as e:
                exc_type, exc_value, exc_tb = sys.exc_info()
                self._respond_error("Exception in decision handler", task_token,
                                    detail = ''.join(traceback.format_exception(exc_type, exc_value, exc_tb)))

            # Report decisions to SWF
            while True:
                try:
                    decisions = list()
                    for decision_type, decision_data in decider.decisions:
                        decision_data_attr = decision_type[0].lower() + decision_type[1:] + 'DecisionAttributes'
                        decisions.append({
                            'decisionType': decision_type,
                            decision_data_attr: decision_data
                        })

                    response = self.swf.respond_decision_task_completed(
                        taskToken=task_token,
                        decisions=decisions,
                    )
                    self.reset_cooldown()
                    return

                except Exception as e:
                    self.log.error("Failed to record decision failure: " + str(response))
                    self.cooldown()

        except CantHandleDecision as e:
            self.log.error("Can't handle decision task %s: %s" % (task_desc, str(e)))
            self._respond_error(
                reason = "Can't handle decision",
                task_token = task_token,
                detail = str(e)
            )


    def _get_next_decsion_task(self, next_page_token=None):
        '''Return next decsion task or None'''

        args = {
            'domain':       self.domain,
            'taskList':     {'name': self.task_list},
            'identity':     self.identity,
            'reverseOrder': True,
        }
        if next_page_token is not None:
            args['nextPageToken'] = next_page_token

        response = None
        while response is None:
            try:
                response = self.swf.poll_for_decision_task(**args)
                self.reset_cooldown()
            except Exception as e:
                self.log.error("Error polling for decision tasks: " + str(e))
                self.log.debug('Response: ' + str(response))
                response = None
                self.cooldown()

        # Skip timeout response
        if 'taskToken' not in response:
            return None

        return response


    def _select_handler(self, decider_task):

        # Select handler for this task
        handler_key = (dpath(decider_task, 'workflowType', 'name'), dpath(decider_task, 'workflowType', 'version'))
        try:
            return self.__deciders[handler_key]
        except KeyError:
            raise CantHandleDecision("No decider registered for %s(%s)" % (handler_key))


    def _retrieve_all_events(self, decider_task):
        '''Get all events to support the decision task'''
        # TODO: Implement cache

        # Get events provided with decision task
        for event in dpath(decider_task, 'events', default=list()):
            yield event

        # Get next pages of events
        response = decider_task
        while dpath(response, 'nextPageToken') is not None:
            next_page_args = self._decision_poll_args()
            next_page_args['nextPageToken'] = dpath(response, 'nextPageToken')
            tries = 0
            try:
                response = self.swf.poll_for_decision_task(**next_page_args)
                for event in dpath(decider_task, 'events'):
                    yield event
                self.reset_cooldown()
            except Exception as e:
                tries += 1
                self.log.error("Error retrieving next page of events: " + str(e))
                self.log.debug('Response: ' + str(response))

                self.cooldown()

                if tries >= 3:
                    self._respond_error(
                        reason = "Error retrieving next page of events: " + str(e),
                        task_token = dpath(decider_task, 'taskToken'),
                        detail = str(e),
                    )
                    raise e


    def _respond_error(self, reason, task_token, detail=None):
        while True:
            try:
                response = self.swf.respond_decision_task_completed(
                    taskToken = task_token,
                    decisions = [
                        {
                            'decisionType': 'FailWorkflowExecution',
                            'failWorkflowExecutionDecisionAttributes': {
                                'reason': reason,
                                'details': detail or '',
                            }
                        },
                    ],
                )
                self.reset_cooldown()
                return
            except Exception as e:
                self.log.error("Failed to record decision failure: " + str(e))
                self.cooldown()


