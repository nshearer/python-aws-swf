from .SWFEvent import SWFEvent

class TimerFiredEvent(SWFEvent):
    '''
    A timer, previously started for this workflow execution, fired.

    'timerFiredEventAttributes': {
        'timerId': 'string',
        'startedEventId': 123
    },
    '''

    

    @property
    def timer_id(self):
        return self._get_data_attr('timerId')
    
