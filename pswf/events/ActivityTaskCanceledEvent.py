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
        return self._get_data_attr('details')
    
    @property
    def scheduled_event_id(self):
        return self._get_data_attr('scheduledEventId')
    
    @property
    def started_event_id(self):
        return self._get_data_attr('startedEventId')
    
