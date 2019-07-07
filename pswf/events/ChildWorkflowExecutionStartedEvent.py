from .SWFEvent import SWFEvent

class ChildWorkflowExecutionStartedEvent(SWFEvent):
    '''
    A child workflow execution was successfully started.

    'childWorkflowExecutionStartedEventAttributes': {
        'workflowExecution': {
            'workflowId': 'string',
            'runId': 'string'
        },
        'workflowType': {
            'name': 'string',
            'version': 'string'
        },
        'initiatedEventId': 123
    },
    '''

    

    
