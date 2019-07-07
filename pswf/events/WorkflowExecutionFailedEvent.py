from .SWFEvent import SWFEvent

class WorkflowExecutionFailedEvent(SWFEvent):
    '''
    The workflow execution closed due to a failure.

    'workflowExecutionFailedEventAttributes': {
        'reason': 'string',
        'details': 'string',
        'decisionTaskCompletedEventId': 123
    },
    '''

    

    @property
    def reason(self):
        return self._get_data_attr('reason')
    
    @property
    def details(self):
        return self._get_data_attr('details')
    
