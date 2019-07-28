# coding=utf-8
from .SWFEvent import SWFEvent

class WorkflowExecutionCanceledEvent(SWFEvent):
    '''
    The workflow execution was successfully canceled and closed.

    'workflowExecutionCanceledEventAttributes': {
        'details': 'string',
        'decisionTaskCompletedEventId': 123
    },
    '''

    

    @property
    def details(self):
        '''
        The details of the cancellation.
    
        :return string:
        '''
        return self._get_string_data_attr('details')
    
    
    @property
    def decision_task_completed_event_id(self):
        '''
        The ID of the DecisionTaskCompleted event corresponding to the decision task that resulted in the CancelWorkflowExecution decision for this cancellation request. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.
    
        :return integer:
        '''
        return self._get_integer_data_attr('decisionTaskCompletedEventId')
    
    
