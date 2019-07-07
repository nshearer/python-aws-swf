from .SWFEvent import SWFEvent

class FailWorkflowExecutionFailedEvent(SWFEvent):
    '''
    A request to mark a workflow execution as failed, itself failed.

    'failWorkflowExecutionFailedEventAttributes': {
        'cause': 'UNHANDLED_DECISION'|'OPERATION_NOT_PERMITTED',
        'decisionTaskCompletedEventId': 123
    },
    '''

    OPERATION_NOT_PERMITTED = 'OPERATION_NOT_PERMITTED'
    UNHANDLED_DECISION = 'UNHANDLED_DECISION'

    @property
    def cause(self):
        return self._get_data_attr('cause')
    
