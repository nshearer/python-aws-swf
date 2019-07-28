# coding=utf-8
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
        '''
        The unique ID of the timer that was started.
    
        :return string:
        '''
        return self._get_data_attr('timerId')
    
    
    @property
    def control(self):
        '''
        Data attached to the event that can be used by the decider in subsequent workflow tasks.
    
        :return string:
        '''
        return self._get_data_attr('control')
    
    
    @property
    def start_to_fire_timeout(self):
        '''
        The duration of time after which the timer fires.
        The duration is specified in seconds, an integer greater than or equal to 0 .
    
        :return string:
        '''
        return self._get_data_attr('startToFireTimeout')
    
    
    @property
    def decision_task_completed_event_id(self):
        '''
        The ID of the DecisionTaskCompleted event corresponding to the decision task that resulted in the StartTimer decision for this activity task. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.
    
        :return integer:
        '''
        return self._get_data_attr('decisionTaskCompletedEventId')
    
    
