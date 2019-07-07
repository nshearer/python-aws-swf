from .SWFEvent import SWFEvent

class RecordMarkerFailedEvent(SWFEvent):
    '''
    A RecordMarker decision was returned as failed.

    'recordMarkerFailedEventAttributes': {
        'markerName': 'string',
        'cause': 'OPERATION_NOT_PERMITTED',
        'decisionTaskCompletedEventId': 123
    },
    '''

    

    @property
    def marker_name(self):
        return self._get_data_attr('markerName')
    
    @property
    def cause(self):
        return self._get_data_attr('cause')
    
