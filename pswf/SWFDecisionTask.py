

from .SWFWorkflow import WokflowExecutionID
from .utils import dpath
from .SWFEvent import SWFEvent

class SWFDecisionTask:
    '''
    A decsion task

    Wraps response from poll_for_decision_task
    https://docs.aws.amazon.com/amazonswf/latest/apireference/API_PollForDecisionTask.html
    '''

    def __init__(self, task_data):
        '''
        :param task_data: Data from SWF
        '''
        self.data = task_data


    @property
    def workflow_instance(self):
        '''Identification of the workflow that this decision is for'''
        return WokflowExecutionID(
            wfname=dpath(self.data, 'workflowType', 'name', required=True),
            wfver=str(dpath(self.data, 'workflowType', 'version', required=True)),
            wfid=dpath(self.data, 'workflowExecution', 'workflowId', required=True),
            run_id=dpath(self.data, 'workflowExecution', 'runId', required=True),
        )

    @property
    def workflow(self):
        return self.workflow_instance.workflow

    def __str__(self):
        return "Decision for " + str(self.workflow)

    @property
    def is_timeout(self):
        return 'taskToken' not in self.data

    @property
    def next_page_token(self):
        '''If decision has more event in the history, then returns token to retrieve'''
        return dpath(self.data, 'nextPageToken', required=False)


    @property
    def events(self):
        for event_data in self.data['events']:
            yield SWFEvent(self.workflow_instance, event_data)

