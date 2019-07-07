from .SWFEvent import SWFEvent

class ExternalWorkflowExecutionCancelRequestedEvent(SWFEvent):
    '''
    Request to cancel an external workflow execution was successfully delivered to the target execution.

    'externalWorkflowExecutionCancelRequestedEventAttributes': {
        'workflowExecution': {
            'workflowId': 'string',
            'runId': 'string'
        },
        'initiatedEventId': 123
    },
    '''

    

    
