from .SWFEvent import SWFEvent

class ScheduleLambdaFunctionFailedEvent(SWFEvent):
    '''
    ScheduleLambdaFunctionFailedEvent event

    'scheduleLambdaFunctionFailedEventAttributes': {
        'id': 'string',
        'name': 'string',
        'cause': 'ID_ALREADY_IN_USE'|'OPEN_LAMBDA_FUNCTIONS_LIMIT_EXCEEDED'|'LAMBDA_FUNCTION_CREATION_RATE_EXCEEDED'|'LAMBDA_SERVICE_NOT_AVAILABLE_IN_REGION',
        'decisionTaskCompletedEventId': 123
    },
    '''

    ID_ALREADY_IN_USE = 'ID_ALREADY_IN_USE'
    LAMBDA_FUNCTION_CREATION_RATE_EXCEEDED = 'LAMBDA_FUNCTION_CREATION_RATE_EXCEEDED'
    LAMBDA_SERVICE_NOT_AVAILABLE_IN_REGION = 'LAMBDA_SERVICE_NOT_AVAILABLE_IN_REGION'
    OPEN_LAMBDA_FUNCTIONS_LIMIT_EXCEEDED = 'OPEN_LAMBDA_FUNCTIONS_LIMIT_EXCEEDED'

    @property
    def id(self):
        return self._get_data_attr('id')
    
    @property
    def name(self):
        return self._get_data_attr('name')
    
    @property
    def cause(self):
        return self._get_data_attr('cause')
    
