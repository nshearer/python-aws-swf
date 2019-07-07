from .SWFEvent import SWFEvent

class LambdaFunctionCompletedEvent(SWFEvent):
    '''
    LambdaFunctionCompletedEvent event

    'lambdaFunctionCompletedEventAttributes': {
        'scheduledEventId': 123,
        'startedEventId': 123,
        'result': 'string'
    },
    '''

    

    @property
    def scheduled_event_id(self):
        return self._get_data_attr('scheduledEventId')
    
    @property
    def started_event_id(self):
        return self._get_data_attr('startedEventId')
    
