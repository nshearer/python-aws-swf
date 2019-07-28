# coding=utf-8
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
        '''
        The unique ID of the timer that was canceled.
    
        :return string:
        '''
        return self._get_string_data_attr('timerId')
    
    
    @property
    def started_event_id(self):
        '''
        The ID of the TimerStarted event that was recorded when this timer was started. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.
    
        :return integer:
        '''
        return self._get_integer_data_attr('startedEventId')
    
    
    @property
    def decision_task_completed_event_id(self):
        '''
        The ID of the DecisionTaskCompleted event corresponding to the decision task that resulted in the CancelTimer decision to cancel this timer. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.
    
        :return integer:
        '''
        return self._get_integer_data_attr('decisionTaskCompletedEventId')
    
    
