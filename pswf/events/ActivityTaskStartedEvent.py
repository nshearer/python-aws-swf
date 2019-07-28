# coding=utf-8
from .SWFEvent import SWFEvent

class ActivityTaskStartedEvent(SWFEvent):
    '''
    The scheduled activity task was dispatched to a worker.

    'activityTaskStartedEventAttributes': {
        'identity': 'string',
        'scheduledEventId': 123
    },
    '''

    

    @property
    def identity(self):
        '''
        Identity of the worker that was assigned this task. This aids diagnostics when problems arise. The form of this identity is user defined.
    
        :return string:
        '''
        return self._get_string_data_attr('identity')
    
    
    @property
    def scheduled_event_id(self):
        '''
        The ID of the ActivityTaskScheduled event that was recorded when this activity task was scheduled. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.
    
        :return integer:
        '''
        return self._get_integer_data_attr('scheduledEventId')
    
    
