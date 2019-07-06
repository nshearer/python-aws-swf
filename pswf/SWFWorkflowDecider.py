
class SWFWorkflowDecider:
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

        self.decisions = list() # (decision_type, decision_data)


    @property
    def wfname(self):
        return self.__workflow_name

    @property
    def wfver(self):
        return self.__workflow_ver


    def extract_event_data(self, workflow, event, wfdata):
        '''
        Extract data from workflow events and store to WF instance data

        Events will be provided in order they occured

        :param workflow: WorkflowInstance for workflow data
        :param event: Event to extract data from
        :param wfdata: Data to collect into (same as workflow.wfdata
        '''
        pass


    def reset(self):
        self.decisions = list()


    def handle(self, execution, events, decision_event_id, task_token):
        '''
        Determine what activity is next in the workflow

        :param execution: SWFExecution handle
        :param events: The prior events in the workflow
        :param decision_event_id:
        :param task_token:
        :return:
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