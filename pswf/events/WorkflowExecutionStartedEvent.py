from .SWFEvent import SWFEvent

class WorkflowExecutionStartedEvent(SWFEvent):
    '''
    The workflow execution was started.

    'workflowExecutionStartedEventAttributes': {
        'input': 'string',
        'executionStartToCloseTimeout': 'string',
        'taskStartToCloseTimeout': 'string',
        'childPolicy': 'TERMINATE'|'REQUEST_CANCEL'|'ABANDON',
        'taskList': {
            'name': 'string'
        },
        'taskPriority': 'string',
        'workflowType': {
            'name': 'string',
            'version': 'string'
        },
        'tagList': [
            'string',
        ],
        'continuedExecutionRunId': 'string',
        'parentWorkflowExecution': {
            'workflowId': 'string',
            'runId': 'string'
        },
        'parentInitiatedEventId': 123,
        'lambdaRole': 'string'
    },
    '''

    ABANDON = 'ABANDON'
    REQUEST_CANCEL = 'REQUEST_CANCEL'
    TERMINATE = 'TERMINATE'

    @property
    def input(self):
        return self._get_data_attr('input')
    
    @property
    def execution_start_to_close_timeout(self):
        return self._get_data_attr('executionStartToCloseTimeout')
    
    @property
    def task_start_to_close_timeout(self):
        return self._get_data_attr('taskStartToCloseTimeout')
    
    @property
    def child_policy(self):
        return self._get_data_attr('childPolicy')
    
    @property
    def task_priority(self):
        return self._get_data_attr('taskPriority')
    
    @property
    def continued_execution_run_id(self):
        return self._get_data_attr('continuedExecutionRunId')
    
    @property
    def parent_initiated_event_id(self):
        return self._get_data_attr('parentInitiatedEventId')
    
