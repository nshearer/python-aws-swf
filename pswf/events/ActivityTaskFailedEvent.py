from .SWFEvent import SWFEvent

class ActivityTaskFailedEvent(SWFEvent):
    '''
    An activity worker failed an activity task by calling RespondActivityTaskFailed.

    'activityTaskFailedEventAttributes': {
        'reason': 'string',
        'details': 'string',
        'scheduledEventId': 123,
        'startedEventId': 123
    },
    '''

    

    @property
    def reason(self):
        return self._get_data_attr('reason')
    
    @property
    def details(self):
        return self._get_data_attr('details')
    
    @property
    def scheduled_event_id(self):
        return self._get_data_attr('scheduledEventId')
    
