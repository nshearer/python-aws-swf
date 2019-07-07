from .SWFEvent import SWFEvent

class ExternalWorkflowExecutionSignaledEvent(SWFEvent):
    '''
    A signal, requested by this workflow execution, was successfully delivered to the target external workflow execution.

    'externalWorkflowExecutionSignaledEventAttributes': {
        'workflowExecution': {
            'workflowId': 'string',
            'runId': 'string'
        },
        'initiatedEventId': 123
    },
    '''

    

    
