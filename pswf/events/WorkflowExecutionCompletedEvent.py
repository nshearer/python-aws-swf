# coding=utf-8
from .SWFEvent import SWFEvent

class WorkflowExecutionCompletedEvent(SWFEvent):
    '''
    The workflow execution was closed due to successful completion.

    'workflowExecutionCompletedEventAttributes': {
        'result': 'string',
        'decisionTaskCompletedEventId': 123
    },
    '''

    

    @property
    def result(self):
        '''
        The result produced by the workflow execution upon successful completion.
    
        :return string:
        '''
        return self._get_string_data_attr('result')
    
    
    @property
    def decision_task_completed_event_id(self):
        '''
        The ID of the DecisionTaskCompleted event corresponding to the decision task that resulted in the CompleteWorkflowExecution decision to complete this execution. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.
    
        :return integer:
        '''
        return self._get_integer_data_attr('decisionTaskCompletedEventId')
    
    
