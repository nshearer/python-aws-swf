from .SWFEvent import SWFEvent

class RequestCancelExternalWorkflowExecutionInitiatedEvent(SWFEvent):
    '''
    A request was made to request the cancellation of an external workflow execution.

    'requestCancelExternalWorkflowExecutionInitiatedEventAttributes': {
        'workflowId': 'string',
        'runId': 'string',
        'decisionTaskCompletedEventId': 123,
        'control': 'string'
    },
    '''

    

    @property
    def workflow_id(self):
        return self._get_data_attr('workflowId')
    
    @property
    def run_id(self):
        return self._get_data_attr('runId')
    
    @property
    def decision_task_completed_event_id(self):
        return self._get_data_attr('decisionTaskCompletedEventId')
    
