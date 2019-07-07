from .SWFEvent import SWFEvent

class WorkflowExecutionContinuedAsNewEvent(SWFEvent):
    '''
    The workflow execution was closed and a new execution of the same type was created with the same workflowId.

    'workflowExecutionContinuedAsNewEventAttributes': {
        'input': 'string',
        'decisionTaskCompletedEventId': 123,
        'newExecutionRunId': 'string',
        'executionStartToCloseTimeout': 'string',
        'taskList': {
            'name': 'string'
        },
        'taskPriority': 'string',
        'taskStartToCloseTimeout': 'string',
        'childPolicy': 'TERMINATE'|'REQUEST_CANCEL'|'ABANDON',
        'tagList': [
            'string',
        ],
        'workflowType': {
            'name': 'string',
            'version': 'string'
        },
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
    def decision_task_completed_event_id(self):
        return self._get_data_attr('decisionTaskCompletedEventId')
    
    @property
    def new_execution_run_id(self):
        return self._get_data_attr('newExecutionRunId')
    
    @property
    def execution_start_to_close_timeout(self):
        return self._get_data_attr('executionStartToCloseTimeout')
    
    @property
    def task_priority(self):
        return self._get_data_attr('taskPriority')
    
    @property
    def task_start_to_close_timeout(self):
        return self._get_data_attr('taskStartToCloseTimeout')
    
    @property
    def child_policy(self):
        return self._get_data_attr('childPolicy')
    
