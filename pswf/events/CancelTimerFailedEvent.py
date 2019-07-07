from .SWFEvent import SWFEvent

class CancelTimerFailedEvent(SWFEvent):
    '''
    Failed to process CancelTimer decision. This happens when the decision isn't configured properly, for example no timer exists with the specified timer Id.

    'cancelTimerFailedEventAttributes': {
        'timerId': 'string',
        'cause': 'TIMER_ID_UNKNOWN'|'OPERATION_NOT_PERMITTED',
        'decisionTaskCompletedEventId': 123
    },
    '''

    OPERATION_NOT_PERMITTED = 'OPERATION_NOT_PERMITTED'
    TIMER_ID_UNKNOWN = 'TIMER_ID_UNKNOWN'

    @property
    def timer_id(self):
        return self._get_data_attr('timerId')
    
    @property
    def cause(self):
        return self._get_data_attr('cause')
    
