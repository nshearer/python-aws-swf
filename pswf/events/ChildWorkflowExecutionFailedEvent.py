from .SWFEvent import SWFEvent

class ChildWorkflowExecutionFailedEvent(SWFEvent):
    '''
    A child workflow execution, started by this workflow execution, failed to complete successfully and was closed.

    'childWorkflowExecutionFailedEventAttributes': {
        'workflowExecution': {
            'workflowId': 'string',
            'runId': 'string'
        },
        'workflowType': {
            'name': 'string',
            'version': 'string'
        },
        'reason': 'string',
        'details': 'string',
        'initiatedEventId': 123,
        'startedEventId': 123
    },
    '''

    

    @property
    def reason(self):
        return self._get_data_attr('reason')
    
    @property
    def details(self):
        return self._get_data_attr('details')
    
    @property
    def initiated_event_id(self):
        return self._get_data_attr('initiatedEventId')
    
