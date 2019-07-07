from .SWFEvent import SWFEvent

class RequestCancelExternalWorkflowExecutionFailedEvent(SWFEvent):
    '''
    Request to cancel an external workflow execution failed.

    'requestCancelExternalWorkflowExecutionFailedEventAttributes': {
        'workflowId': 'string',
        'runId': 'string',
        'cause': 'UNKNOWN_EXTERNAL_WORKFLOW_EXECUTION'|'REQUEST_CANCEL_EXTERNAL_WORKFLOW_EXECUTION_RATE_EXCEEDED'|'OPERATION_NOT_PERMITTED',
        'initiatedEventId': 123,
        'decisionTaskCompletedEventId': 123,
        'control': 'string'
    },
    '''

    OPERATION_NOT_PERMITTED = 'OPERATION_NOT_PERMITTED'
    REQUEST_CANCEL_EXTERNAL_WORKFLOW_EXECUTION_RATE_EXCEEDED = 'REQUEST_CANCEL_EXTERNAL_WORKFLOW_EXECUTION_RATE_EXCEEDED'
    UNKNOWN_EXTERNAL_WORKFLOW_EXECUTION = 'UNKNOWN_EXTERNAL_WORKFLOW_EXECUTION'

    @property
    def workflow_id(self):
        return self._get_data_attr('workflowId')
    
    @property
    def run_id(self):
        return self._get_data_attr('runId')
    
    @property
    def cause(self):
        return self._get_data_attr('cause')
    
    @property
    def initiated_event_id(self):
        return self._get_data_attr('initiatedEventId')
    
    @property
    def decision_task_completed_event_id(self):
        return self._get_data_attr('decisionTaskCompletedEventId')
    
