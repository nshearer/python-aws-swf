import os

import logging
import boto3
from botocore.client import Config
import uuid
from time import sleep
from datetime import datetime, timedelta
from dotenv import load_dotenv

from .SWFWorkflow import SWFWorkflow
from .SWFDecisionTask import SWFDecisionTask
from .WorkflowExecution import WorkflowInstanceCollection
from .utils import dpath

class ApiReqeustFailed(Exception): pass
class CantHandleDecsionTask(Exception): pass


# TODO: Get terminology consistant (workflow, task, event, ID, etc.)


class SWFDecider(SWFWorkflow):
    '''
    Process that queries the SWF endpoints and applies makes decisions on workflow execution.

    In SWF, a decider process determines what the next steps are in an executing workflow.  This class is intended
    to be subclassed with methods implemented to respond to workflow events and queue up the next actions to take.
    '''

    def __init__(self, identity, task_list):
        '''
        :param identity: String to identify this decider in the workflow history
        :param domain: Name of the domain in SWF to poll for decisions in.
        :param task_list:
            Name of the task list to poll for decisions in.
            (one decider per domain + task list)
        '''

        self.log = logging.getLogger(__name__)

        self.__identity = str(identity)
        self.__task_list = str(task_list)

        self.__workflow_execution_cache = WorkflowInstanceCollection()

        try:
            os.environ['AWS_ACCESS_KEY_ID']
            os.environ['AWS_SECRET_ACCESS_KEY']
        except KeyError:
            raise Exception("Need to set env AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY (can use .env)")
        botoConfig = Config(connect_timeout=50, read_timeout=70)
        self.__swf = boto3.client('pswf', config=botoConfig)

        self.__failed_request_wait = None


    def add(self, decision_hander):
        '''Add a decision handler which contains the logic for a SWF workflow'''
        self.__deciders.append(decision_hander)


    def poll_forever(self):
        '''Keep polling the SWF service to find decions that need to be made'''
        while True:
            self.poll_one_decision()


    def _call_poll_for_descision_task_api(self, next_page_token=None):
        '''Call the SWF poll_for_decision_task API'''

        started = datetime.now()

        try:
            api_args = {
                'domain':       self.__domain,
                'taskList':     {'name': self.__task_list},
                'identity':     self.__identity,
                'reverseOrder': True,
            }
            if next_page_token is not None:
                api_args['nextPageToken'] = next_page_token
            task = self.__swf.poll_for_decision_task(**api_args)
            task = SWFDecisionTask(task)

            # Check for timeout response
            if task.is_timeout:

                # Check failed too fast
                request_duration = datetime.now() - started
                if request_duration.total_seconds() < 20:
                    raise ApiReqeustFailed("Timeout occured in just %s" % (str(request_duration)))

                return None

            self.successful_api_call()
            return task

        except Exception as e:
            self.check_failed_request_freq()
            self.log.error("SWF PollForDecisionTask failed: %s" % (str(e)))
            return None


    def poll_one_decision(self):
        '''Poll SWF for a decision and handle it'''

        # Get next decision task
        task = self._call_poll_for_descision_task_api()
        if task is None:
            return

        # Match to handler
        handler = self.select_handler_for(task)

        # Match to workflow instance
        wf_instance = self.__workflow_instances.get(task.workflow_instance)

        # Retrieve any events that are new
        new_events = list()
        for event in self._all_events_for_task(task):
            if not wf_instance.seen_event(event):
                new_events.append(event)
            else:
                break

        # Collect data and add events to workflow instance data
        last_event = None
        for event in sorted(new_events, key=lambda e: e.event_id.event_id):
            handler.extract_event_data(wf_instance, event, wf_instance.wfdata)
            if event.event_type_for_decision:
                last_event = event

        # Ask handler what to do
        if last_event is None:
            raise Exception("No event found to decide on")
        handler.handle(wf_instance, task, last_event)


    def _all_events_for_task(self, task):
        '''Get all events for the task'''
        for event in task.events:
            yield event
        # Look at other pages
        while task.next_page_token is not None:
            task = self._call_poll_for_descision_task_api(task.next_page_token)
            for event in task.events:
                yield event


    MIN_FAILED_WAIT = timedelta(seconds=15)
    MAX_FAILED_WAIT = timedelta(minutes=5)

    def check_failed_request_freq(self):
        '''Watch the number of times an API call fails and back off if needed'''
        if self.__failed_request_wait is None:
            self.__failed_request_wait = self.MIN_FAILED_WAIT
        else:
            self.__failed_request_wait *= 2
        self.__failed_request_wait = min(self.__failed_request_wait, self.MAX_FAILED_WAIT)
        sleep(self.__failed_request_wait.total_seconds())

    def successful_api_call(self):
        self.__failed_request_wait = None


    def select_handler_for(self, task):
        '''
        Find the correct handler for a given request

        :param task:
            Full result from poll_for_decision_task
            https://docs.aws.amazon.com/amazonswf/latest/apireference/API_PollForDecisionTask.html
        :return: SWFDecisionHandler
        '''

        for handler in self.__deciders:
            if handler.should_handle(task):
                return handler

        raise CantHandleDecsionTask("Can't find handler for decision task: %s" % (str(task)))
