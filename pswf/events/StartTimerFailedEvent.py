from .SWFEvent import SWFEvent

class StartTimerFailedEvent(SWFEvent):
    '''
    Failed to process StartTimer decision. This happens when the decision isn't configured properly, for example a timer already exists with the specified timer Id.

    'startTimerFailedEventAttributes': {
        'timerId': 'string',
        'cause': 'TIMER_ID_ALREADY_IN_USE'|'OPEN_TIMERS_LIMIT_EXCEEDED'|'TIMER_CREATION_RATE_EXCEEDED'|'OPERATION_NOT_PERMITTED',
        'decisionTaskCompletedEventId': 123
    },
    '''

    OPEN_TIMERS_LIMIT_EXCEEDED = 'OPEN_TIMERS_LIMIT_EXCEEDED'
    OPERATION_NOT_PERMITTED = 'OPERATION_NOT_PERMITTED'
    TIMER_CREATION_RATE_EXCEEDED = 'TIMER_CREATION_RATE_EXCEEDED'
    TIMER_ID_ALREADY_IN_USE = 'TIMER_ID_ALREADY_IN_USE'

    @property
    def timer_id(self):
        return self._get_data_attr('timerId')
    
    @property
    def cause(self):
        return self._get_data_attr('cause')
    
