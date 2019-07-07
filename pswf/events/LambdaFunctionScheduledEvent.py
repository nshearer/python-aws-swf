from .SWFEvent import SWFEvent

class LambdaFunctionScheduledEvent(SWFEvent):
    '''
    LambdaFunctionScheduledEvent event

    'lambdaFunctionScheduledEventAttributes': {
        'id': 'string',
        'name': 'string',
        'control': 'string',
        'input': 'string',
        'startToCloseTimeout': 'string',
        'decisionTaskCompletedEventId': 123
    },
    '''

    

    @property
    def id(self):
        return self._get_data_attr('id')
    
    @property
    def name(self):
        return self._get_data_attr('name')
    
    @property
    def control(self):
        return self._get_data_attr('control')
    
    @property
    def input(self):
        return self._get_data_attr('input')
    
    @property
    def start_to_close_timeout(self):
        return self._get_data_attr('startToCloseTimeout')
    
