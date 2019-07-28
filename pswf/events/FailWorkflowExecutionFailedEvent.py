# coding=utf-8
from .SWFEvent import SWFEvent

class FailWorkflowExecutionFailedEvent(SWFEvent):
    '''
    A request to mark a workflow execution as failed, itself failed.

    'failWorkflowExecutionFailedEventAttributes': {
        'cause': 'UNHANDLED_DECISION'|'OPERATION_NOT_PERMITTED',
        'decisionTaskCompletedEventId': 123
    },
    '''

    

    @property
    def cause(self):
        '''
        The cause of the failure. This information is generated by the system and can be useful for diagnostic purposes.
    
        Note
        If cause is set to OPERATION_NOT_PERMITTED , the decision failed because it lacked sufficient permissions. For details and example IAM policies, see Using IAM to Manage Access to Amazon SWF Workflows in the Amazon SWF Developer Guide .
    
        :return string:
        '''
        return self._get_string_data_attr('cause')
    
    
    @property
    def decision_task_completed_event_id(self):
        '''
        The ID of the DecisionTaskCompleted event corresponding to the decision task that resulted in the FailWorkflowExecution decision to fail this execution. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.
    
        :return integer:
        '''
        return self._get_integer_data_attr('decisionTaskCompletedEventId')
    
    
