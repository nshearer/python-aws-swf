from .SWFEvent import SWFEvent

class ChildWorkflowExecutionCompletedEvent(SWFEvent):
    '''
    A child workflow execution, started by this workflow execution, completed successfully and was closed.

    'childWorkflowExecutionCompletedEventAttributes': {
        'workflowExecution': {
            'workflowId': 'string',
            'runId': 'string'
        },
        'workflowType': {
            'name': 'string',
            'version': 'string'
        },
        'result': 'string',
        'initiatedEventId': 123,
        'startedEventId': 123
    },
    '''

    

    @property
    def result(self):
        return self._get_data_attr('result')
    
    @property
    def initiated_event_id(self):
        return self._get_data_attr('initiatedEventId')
    
