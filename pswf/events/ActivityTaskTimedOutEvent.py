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

    HEARTBEAT = 'HEARTBEAT'
    SCHEDULE_TO_CLOSE = 'SCHEDULE_TO_CLOSE'
    SCHEDULE_TO_START = 'SCHEDULE_TO_START'
    START_TO_CLOSE = 'START_TO_CLOSE'

    @property
    def timeout_type(self):
        return self._get_data_attr('timeoutType')
    
    @property
    def scheduled_event_id(self):
        return self._get_data_attr('scheduledEventId')
    
    @property
    def started_event_id(self):
        return self._get_data_attr('startedEventId')
    
