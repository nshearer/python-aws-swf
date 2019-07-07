from .SWFEvent import SWFEvent

class CompleteWorkflowExecutionFailedEvent(SWFEvent):
    '''
    The workflow execution failed to complete.

    'completeWorkflowExecutionFailedEventAttributes': {
        'cause': 'UNHANDLED_DECISION'|'OPERATION_NOT_PERMITTED',
        'decisionTaskCompletedEventId': 123
    },
    '''

    OPERATION_NOT_PERMITTED = 'OPERATION_NOT_PERMITTED'
    UNHANDLED_DECISION = 'UNHANDLED_DECISION'

    @property
    def cause(self):
        return self._get_data_attr('cause')
    
