
from .SWFWorkflow import SWFWorkflow

class SWFWorkflowDecider(SWFWorkflow):
    '''
    Base class for defining handlers that make the decisions to direct SWF Workflows
    '''

    def __init__(self, workflow_name, workflow_version=None):
        '''
        :param workflow_name:
            Name of the workflow to handle decisions for.
        :param workflow_version:
            Version of the workflow to handle decisions for.
            If None, will match any version
        '''
        self.__workflow_name = workflow_name
        self.__workflow_ver = str(workflow_version)

        self.workflow = None
        self.task = None
        self.last_event = None


    def extract_event_data(self, workflow, event, wfdata):
        '''
        Extract data from workflow events and store to WF instance data

        Events will be provided in order they occured

        :param workflow: WorkflowInstance for workflow data
        :param event: Event to extract data from
        :param wfdata: Data to collect into (same as workflow.wfdata
        '''
        pass


    def handle(self, execution, events, next_page_token, task_token, decision_event_id):
        '''
        Determine what action the workflow should take

        :param workflow: WorkflowInstance
        :param task: SWFDecisionTask
        :param event: (SWFEvent) Last event that occurred in the workflow
        '''

        self.workflow = workflow
        self.task = task
        self.last_event = event

        if event.event_type == 'WorkflowExecutionStarted':
            self.on_workflow_start()
        else:
            print("Unknown event type: " + event.event_type)


    def start_activity(self, name):
        raise NotImplementedError()


    def complete_workflow(self):
        raise NotImplementedError()