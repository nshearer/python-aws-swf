from .SWFEvent import SWFEvent

class ChildWorkflowExecutionTerminatedEvent(SWFEvent):
    '''
    A child workflow execution, started by this workflow execution, was terminated.

    'childWorkflowExecutionTerminatedEventAttributes': {
        'workflowExecution': {
            'workflowId': 'string',
            'runId': 'string'
        },
        'workflowType': {
            'name': 'string',
            'version': 'string'
        },
        'initiatedEventId': 123,
        'startedEventId': 123
    },
    '''

    

    @property
    def initiated_event_id(self):
        return self._get_data_attr('initiatedEventId')
    
