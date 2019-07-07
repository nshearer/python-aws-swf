from .SWFEvent import SWFEvent

class LambdaFunctionFailedEvent(SWFEvent):
    '''
    LambdaFunctionFailedEvent event

    'lambdaFunctionFailedEventAttributes': {
        'scheduledEventId': 123,
        'startedEventId': 123,
        'reason': 'string',
        'details': 'string'
    },
    '''

    

    @property
    def scheduled_event_id(self):
        return self._get_data_attr('scheduledEventId')
    
    @property
    def started_event_id(self):
        return self._get_data_attr('startedEventId')
    
    @property
    def reason(self):
        return self._get_data_attr('reason')
    
