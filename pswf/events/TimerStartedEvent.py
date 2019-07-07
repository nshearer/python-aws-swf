from .SWFEvent import SWFEvent

class TimerStartedEvent(SWFEvent):
    '''
    A timer was started for the workflow execution due to a StartTimer decision.

    'timerStartedEventAttributes': {
        'timerId': 'string',
        'control': 'string',
        'startToFireTimeout': 'string',
        'decisionTaskCompletedEventId': 123
    },
    '''

    

    @property
    def timer_id(self):
        return self._get_data_attr('timerId')
    
    @property
    def control(self):
        return self._get_data_attr('control')
    
    @property
    def start_to_fire_timeout(self):
        return self._get_data_attr('startToFireTimeout')
    
