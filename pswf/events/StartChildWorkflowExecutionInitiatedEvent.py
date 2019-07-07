from .SWFEvent import SWFEvent

class StartChildWorkflowExecutionInitiatedEvent(SWFEvent):
    '''
    A request was made to start a child workflow execution.

    'startChildWorkflowExecutionInitiatedEventAttributes': {
        'workflowId': 'string',
        'workflowType': {
            'name': 'string',
            'version': 'string'
        },
        'control': 'string',
        'input': 'string',
        'executionStartToCloseTimeout': 'string',
        'taskList': {
            'name': 'string'
        },
        'taskPriority': 'string',
        'decisionTaskCompletedEventId': 123,
        'childPolicy': 'TERMINATE'|'REQUEST_CANCEL'|'ABANDON',
        'taskStartToCloseTimeout': 'string',
        'tagList': [
            'string',
        ],
        'lambdaRole': 'string'
    },
    '''

    ABANDON = 'ABANDON'
    REQUEST_CANCEL = 'REQUEST_CANCEL'
    TERMINATE = 'TERMINATE'

    @property
    def workflow_id(self):
        return self._get_data_attr('workflowId')
    
    @property
    def control(self):
        return self._get_data_attr('control')
    
    @property
    def input(self):
        return self._get_data_attr('input')
    
    @property
    def execution_start_to_close_timeout(self):
        return self._get_data_attr('executionStartToCloseTimeout')
    
    @property
    def task_priority(self):
        return self._get_data_attr('taskPriority')
    
    @property
    def decision_task_completed_event_id(self):
        return self._get_data_attr('decisionTaskCompletedEventId')
    
    @property
    def child_policy(self):
        return self._get_data_attr('childPolicy')
    
    @property
    def task_start_to_close_timeout(self):
        return self._get_data_attr('taskStartToCloseTimeout')
    
