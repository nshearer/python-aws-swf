from .SWFEvent import SWFEvent

class WorkflowExecutionSignaledEvent(SWFEvent):
    '''
    An external signal was received for the workflow execution.

    'workflowExecutionSignaledEventAttributes': {
        'signalName': 'string',
        'input': 'string',
        'externalWorkflowExecution': {
            'workflowId': 'string',
            'runId': 'string'
        },
        'externalInitiatedEventId': 123
    },
    '''

    

    @property
    def signal_name(self):
        return self._get_data_attr('signalName')
    
    @property
    def input(self):
        return self._get_data_attr('input')
    
