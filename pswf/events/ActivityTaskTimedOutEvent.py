# coding=utf-8
from .SWFEvent import SWFEvent

class ActivityTaskTimedOutEvent(SWFEvent):
    '''
    The activity task timed out.

    'activityTaskTimedOutEventAttributes': {
        'timeoutType': 'START_TO_CLOSE'|'SCHEDULE_TO_START'|'SCHEDULE_TO_CLOSE'|'HEARTBEAT',
        'scheduledEventId': 123,
        'startedEventId': 123,
        'details': 'string'
    },
    '''

    

    @property
    def timeout_type(self):
        '''
        The type of the timeout that caused this event.
    
        :return string:
        '''
        return self._get_string_data_attr('timeoutType')
    
    
    @property
    def scheduled_event_id(self):
        '''
        The ID of the ActivityTaskScheduled event that was recorded when this activity task was scheduled. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.
    
        :return integer:
        '''
        return self._get_integer_data_attr('scheduledEventId')
    
    
    @property
    def started_event_id(self):
        '''
        The ID of the ActivityTaskStarted event recorded when this activity task was started. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.
    
        :return integer:
        '''
        return self._get_integer_data_attr('startedEventId')
    
    
    @property
    def details(self):
        '''
        Contains the content of the details parameter for the last call made by the activity to RecordActivityTaskHeartbeat .
    
        :return string:
        '''
        return self._get_string_data_attr('details')
    
    
