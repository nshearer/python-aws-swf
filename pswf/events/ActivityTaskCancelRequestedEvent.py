from .SWFEvent import SWFEvent

class ActivityTaskCancelRequestedEvent(SWFEvent):
    '''
    A RequestCancelActivityTask decision was received by the system.

    'activityTaskCancelRequestedEventAttributes': {
        'decisionTaskCompletedEventId': 123,
        'activityId': 'string'
    },
    '''

    

    @property
    def decision_task_completed_event_id(self):
        return self._get_data_attr('decisionTaskCompletedEventId')
    
