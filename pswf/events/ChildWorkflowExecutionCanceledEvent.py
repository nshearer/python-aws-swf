from .SWFEvent import SWFEvent

class ChildWorkflowExecutionCanceledEvent(SWFEvent):
    '''
    A child workflow execution, started by this workflow execution, was canceled and closed.

    'childWorkflowExecutionCanceledEventAttributes': {
        'workflowExecution': {
            'workflowId': 'string',
            'runId': 'string'
        },
        'workflowType': {
            'name': 'string',
            'version': 'string'
        },
        'details': 'string',
        'initiatedEventId': 123,
        'startedEventId': 123
    },
    '''

    

    @property
    def details(self):
        return self._get_data_attr('details')
    
    @property
    def initiated_event_id(self):
        return self._get_data_attr('initiatedEventId')
    
