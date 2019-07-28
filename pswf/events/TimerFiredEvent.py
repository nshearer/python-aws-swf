# coding=utf-8
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
        '''
        The unique ID of the timer that fired.
    
        :return string:
        '''
        return self._get_data_attr('timerId')
    
    
    @property
    def started_event_id(self):
        '''
        The ID of the TimerStarted event that was recorded when this timer was started. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.
    
        :return integer:
        '''
        return self._get_data_attr('startedEventId')
    
    
