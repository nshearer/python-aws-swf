from .SWFEvent import SWFEvent

class DecisionTaskTimedOutEvent(SWFEvent):
    '''
    The decision task timed out.

    'decisionTaskTimedOutEventAttributes': {
        'timeoutType': 'START_TO_CLOSE',
        'scheduledEventId': 123,
        'startedEventId': 123
    },
    '''

    

    @property
    def timeout_type(self):
        return self._get_data_attr('timeoutType')
    
    @property
    def scheduled_event_id(self):
        return self._get_data_attr('scheduledEventId')
    
