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
        return self._get_data_attr('identity')
    
