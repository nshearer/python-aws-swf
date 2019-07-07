from .SWFEvent import SWFEvent

class WorkflowExecutionCanceledEvent(SWFEvent):
    '''
    The workflow execution was successfully canceled and closed.

    'workflowExecutionCanceledEventAttributes': {
        'details': 'string',
        'decisionTaskCompletedEventId': 123
    },
    '''

    

    @property
    def details(self):
        return self._get_data_attr('details')
    
