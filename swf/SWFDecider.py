
import boto3
from botocore.client import Config
import uuid

from .WorkflowInstance import WorkflowInstanceCollection

class SWFDecider:
    '''
    Process that queries the SWF enpoints and applies SWFDecider logic

    This class is meant to be instantiated, and then gien one or more SWFDecider
    objects to use to make decisions and direct SWF workflows.  Typical usage is:

    runner = SWFDecider()
    runner.add(SWFDecisionHandlerA())
    runner.add(SWFDecisionHandlerB())
    runner.run_forever()
    '''

    def __init__(self, identity, domain, task_list):
        '''
        :param identity: String to identify this decider in the workflow history
        :param domain: Name of the domain in SWF to poll for decisions in.
        :param task_list: Name of the task list to poll for decisions in.
            (one decider per domain + task list)
        '''

        self.__identity = str(identity)
        self.__domain = str(domain)
        self.__task_list = str(task_list)

        self.__deciders = list()
        self.__workflows = WorkflowInstanceCollection()

        botoConfig = Config(connect_timeout=50, read_timeout=70)
        swf = boto3.client('swf', config=botoConfig)


    def add(self, decision_hander):
        '''Add a decision handler which contains the logic for a SWF workflow'''
        self.__deciders.add(decision_hander)


    def poll_forever(self):
        '''Keep polling the SWF service to find decions that need to be made'''
        while True:
            self.poll_one_decision()


    def poll_one_decision(self):
        '''Poll SFW for a decision and handle it'''

        task = self.__swf.poll_for_decision_task(
            domain  = self.__domain,
            taskList= {'name': self.__task_list},
            identity= self.__identity,
            reverseOrder=True)

        # Check for timeout
        if 'taskToken' not in task:
            print("Poll timed out, no new task.  Repoll")

        # Match to handler

        # Match to workflow instance

        # Retrieve any events that are new (and extract WF state data)

        # Ask handler what to do
        



