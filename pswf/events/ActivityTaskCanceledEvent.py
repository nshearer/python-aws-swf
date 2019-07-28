# coding=utf-8
from .SWFEvent import SWFEvent

class ActivityTaskCanceledEvent(SWFEvent):
    '''
    The activity task was successfully canceled.

    'activityTaskCanceledEventAttributes': {
        'details': 'string',
        'scheduledEventId': 123,
        'startedEventId': 123,
        'latestCancelRequestedEventId': 123
    },
    '''

    

    @property
    def details(self):
        '''
        Details of the cancellation.
    
        :return string:
        '''
        return self._get_string_data_attr('details')
    
    
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
    def latest_cancel_requested_event_id(self):
        '''
        If set, contains the ID of the last ActivityTaskCancelRequested event recorded for this activity task. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.
    
        :return integer:
        '''
        return self._get_integer_data_attr('latestCancelRequestedEventId')
    
    
