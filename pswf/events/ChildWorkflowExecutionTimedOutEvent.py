from .SWFEvent import SWFEvent

class ChildWorkflowExecutionTimedOutEvent(SWFEvent):
    '''
    A child workflow execution, started by this workflow execution, timed out and was closed.

    'childWorkflowExecutionTimedOutEventAttributes': {
        'workflowExecution': {
            'workflowId': 'string',
            'runId': 'string'
        },
        'workflowType': {
            'name': 'string',
            'version': 'string'
        },
        'timeoutType': 'START_TO_CLOSE',
        'initiatedEventId': 123,
        'startedEventId': 123
    },
    '''

    

    @property
    def timeout_type(self):
        return self._get_data_attr('timeoutType')
    
    @property
    def initiated_event_id(self):
        return self._get_data_attr('initiatedEventId')
    
