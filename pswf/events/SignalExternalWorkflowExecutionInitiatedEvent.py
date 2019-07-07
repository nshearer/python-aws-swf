from .SWFEvent import SWFEvent

class SignalExternalWorkflowExecutionInitiatedEvent(SWFEvent):
    '''
    A request to signal an external workflow was made.

    'signalExternalWorkflowExecutionInitiatedEventAttributes': {
        'workflowId': 'string',
        'runId': 'string',
        'signalName': 'string',
        'input': 'string',
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
    def signal_name(self):
        return self._get_data_attr('signalName')
    
    @property
    def input(self):
        return self._get_data_attr('input')
    
    @property
    def decision_task_completed_event_id(self):
        return self._get_data_attr('decisionTaskCompletedEventId')
    
