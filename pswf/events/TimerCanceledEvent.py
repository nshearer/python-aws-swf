from .SWFEvent import SWFEvent

class TimerCanceledEvent(SWFEvent):
    '''
    A timer, previously started for this workflow execution, was successfully canceled.

    'timerCanceledEventAttributes': {
        'timerId': 'string',
        'startedEventId': 123,
        'decisionTaskCompletedEventId': 123
    },
    '''

    

    @property
    def timer_id(self):
        return self._get_data_attr('timerId')
    
    @property
    def started_event_id(self):
        return self._get_data_attr('startedEventId')
    
