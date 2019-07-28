# coding=utf-8
from .SWFEvent import SWFEvent

class DecisionTaskCompletedEvent(SWFEvent):
    '''
    The decider successfully completed a decision task by calling  RespondDecisionTaskCompleted .

    'decisionTaskCompletedEventAttributes': {
        'executionContext': 'string',
        'scheduledEventId': 123,
        'startedEventId': 123
    },
    '''

    

    @property
    def execution_context(self):
        '''
        User defined context for the workflow execution.
    
        :return string:
        '''
        return self._get_string_data_attr('executionContext')
    
    
    @property
    def scheduled_event_id(self):
        '''
        The ID of the DecisionTaskScheduled event that was recorded when this decision task was scheduled. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.
    
        :return integer:
        '''
        return self._get_integer_data_attr('scheduledEventId')
    
    
    @property
    def started_event_id(self):
        '''
        The ID of the DecisionTaskStarted event recorded when this decision task was started. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.
    
        :return integer:
        '''
        return self._get_integer_data_attr('startedEventId')
    
    
