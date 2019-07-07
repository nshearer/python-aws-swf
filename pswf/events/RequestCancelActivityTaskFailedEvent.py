from .SWFEvent import SWFEvent

class RequestCancelActivityTaskFailedEvent(SWFEvent):
    '''
    Failed to process RequestCancelActivityTask decision. This happens when the decision isn't configured properly.

    'requestCancelActivityTaskFailedEventAttributes': {
        'activityId': 'string',
        'cause': 'ACTIVITY_ID_UNKNOWN'|'OPERATION_NOT_PERMITTED',
        'decisionTaskCompletedEventId': 123
    },
    '''

    ACTIVITY_ID_UNKNOWN = 'ACTIVITY_ID_UNKNOWN'
    OPERATION_NOT_PERMITTED = 'OPERATION_NOT_PERMITTED'

    @property
    def activity_id(self):
        return self._get_data_attr('activityId')
    
    @property
    def cause(self):
        return self._get_data_attr('cause')
    
