from .SWFEvent import SWFEvent

class ActivityTaskCompletedEvent(SWFEvent):
    '''
    An activity worker successfully completed an activity task by calling RespondActivityTaskCompleted.

    'activityTaskCompletedEventAttributes': {
        'result': 'string',
        'scheduledEventId': 123,
        'startedEventId': 123
    },
    '''

    

    @property
    def result(self):
        return self._get_data_attr('result')
    
    @property
    def scheduled_event_id(self):
        return self._get_data_attr('scheduledEventId')
    
