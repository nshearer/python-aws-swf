# coding=utf-8
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
        '''
        The ID of the DecisionTaskCompleted event corresponding to the decision task that resulted in the RequestCancelActivityTask decision for this cancellation request. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.
    
        :return integer:
        '''
        return self._get_integer_data_attr('decisionTaskCompletedEventId')
    
    
    @property
    def activity_id(self):
        '''
        The unique ID of the task.
    
        :return string:
        '''
        return self._get_string_data_attr('activityId')
    
    
