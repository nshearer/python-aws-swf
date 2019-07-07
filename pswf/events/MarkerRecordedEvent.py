from .SWFEvent import SWFEvent

class MarkerRecordedEvent(SWFEvent):
    '''
    A marker was recorded in the workflow history as the result of a RecordMarker decision.

    'markerRecordedEventAttributes': {
        'markerName': 'string',
        'details': 'string',
        'decisionTaskCompletedEventId': 123
    },
    '''

    

    @property
    def marker_name(self):
        return self._get_data_attr('markerName')
    
    @property
    def details(self):
        return self._get_data_attr('details')
    
