# coding=utf-8
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
        '''
        The name of the marker.
    
        :return string:
        '''
        return self._get_string_data_attr('markerName')
    
    
    @property
    def details(self):
        '''
        The details of the marker.
    
        :return string:
        '''
        return self._get_string_data_attr('details')
    
    
    @property
    def decision_task_completed_event_id(self):
        '''
        The ID of the DecisionTaskCompleted event corresponding to the decision task that resulted in the RecordMarker decision that requested this marker. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.
    
        :return integer:
        '''
        return self._get_integer_data_attr('decisionTaskCompletedEventId')
    
    
