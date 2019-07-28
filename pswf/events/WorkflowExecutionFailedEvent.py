# coding=utf-8
from .SWFEvent import SWFEvent

class WorkflowExecutionFailedEvent(SWFEvent):
    '''
    The workflow execution closed due to a failure.

    'workflowExecutionFailedEventAttributes': {
        'reason': 'string',
        'details': 'string',
        'decisionTaskCompletedEventId': 123
    },
    '''

    

    @property
    def reason(self):
        '''
        The descriptive reason provided for the failure.
    
        :return string:
        '''
        return self._get_data_attr('reason')
    
    
    @property
    def details(self):
        '''
        The details of the failure.
    
        :return string:
        '''
        return self._get_data_attr('details')
    
    
    @property
    def decision_task_completed_event_id(self):
        '''
        The ID of the DecisionTaskCompleted event corresponding to the decision task that resulted in the FailWorkflowExecution decision to fail this execution. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.
    
        :return integer:
        '''
        return self._get_data_attr('decisionTaskCompletedEventId')
    
    
