# coding=utf-8
from .SWFEvent import SWFEvent

class ActivityTaskFailedEvent(SWFEvent):
    '''
    An activity worker failed an activity task by calling  RespondActivityTaskFailed .

    'activityTaskFailedEventAttributes': {
        'reason': 'string',
        'details': 'string',
        'scheduledEventId': 123,
        'startedEventId': 123
    },
    '''

    

    @property
    def reason(self):
        '''
        The reason provided for the failure.
    
        :return string:
        '''
        return self._get_data_attr('reason')
    
    
    @property
    def details(self):
        '''
        The details of the failure.
    
        :return string:
        '''
        return self._get_data_attr('details')
    
    
    @property
    def scheduled_event_id(self):
        '''
        The ID of the ActivityTaskScheduled event that was recorded when this activity task was scheduled. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.
    
        :return integer:
        '''
        return self._get_data_attr('scheduledEventId')
    
    
    @property
    def started_event_id(self):
        '''
        The ID of the ActivityTaskStarted event recorded when this activity task was started. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.
    
        :return integer:
        '''
        return self._get_data_attr('startedEventId')
    
    
