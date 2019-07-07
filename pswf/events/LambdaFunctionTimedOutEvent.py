from .SWFEvent import SWFEvent

class LambdaFunctionTimedOutEvent(SWFEvent):
    '''
    LambdaFunctionTimedOutEvent event

    'lambdaFunctionTimedOutEventAttributes': {
        'scheduledEventId': 123,
        'startedEventId': 123,
        'timeoutType': 'START_TO_CLOSE'
    },
    '''

    

    @property
    def scheduled_event_id(self):
        return self._get_data_attr('scheduledEventId')
    
    @property
    def started_event_id(self):
        return self._get_data_attr('startedEventId')
    
