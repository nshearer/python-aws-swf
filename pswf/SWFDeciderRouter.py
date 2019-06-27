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
        key = (decider.wfname, decider.version)
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
        try:
            api_args = {
                'domain':       self.domain,
                'taskList':     {'name': self.task_list},
                'identity':     self.identity,
                'reverseOrder': True,
            }

            # Get next task
            response = None
            while response is None:
                try:
                    response = self.swf.poll_for_decision_task(**api_args)
                    self.reset_cooldown()
                except Exception as e:
                    self.log.error("Error polling for decision tasks: " + str(e))
                    self.log.debug('Response: ' + str(response))
                    response = None
                    self.cooldown()

            # Skip timeout response
            if response == dict():
                return

            # Select handler for this task
            task_token = dpath(response, 'taskToken')
            key = (dpath(response, 'workflowType', 'name'), dpath(response, 'workflowType', 'version'))
            try:
                decider = self.__deciders[key]
            except KeyError:
                self._respond_error("No decider registered for %s(%s)" % (key), task_token)

            # Pass to handler to continue
            try:
                decider.handle(
                    execution = SWFExecution(
                        run_id = dpath(response, 'workflowExecution', 'runId'),
                        exec_name = dpath(response, 'workflowExecution', 'workflowId'),
                        copyfrom = decider, # Decider subclasses SWFWorkflow, so this works
                    ),
                    events = parse_event_list(dpath(response, 'events')),
                    next_page_token = dpath(response, 'nextPageToken', required=False),
                    task_token = task_token,
                    decision_event_id = dpath(response, 'startedEventId'),
                )
            except Exception as e:
                exc_type, exc_value, exc_tb = sys.exc_info()
                self.__respond_error("Exception in decision handler", task_token,
                                     detail = ''.join(traceback.format_exception(exc_type, exc_value, exc_tb)))

        except Exception as e:
            if task_token is not None:
                self._respond_error("Unexpected exception: " + str(e))


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
                                'details': detail,
                            }
                        },
                    ],
                )
                self.reset_cooldown()
                return
            except Exception as e:
                self.log.error("Failed to record decision failure: " + str(response))
                self.cooldown()


