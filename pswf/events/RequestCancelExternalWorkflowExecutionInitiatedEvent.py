# coding=utf-8
from .SWFEvent import SWFEvent

class RequestCancelExternalWorkflowExecutionInitiatedEvent(SWFEvent):
    '''
    A request was made to request the cancellation of an external workflow execution.

    'requestCancelExternalWorkflowExecutionInitiatedEventAttributes': {
        'workflowId': 'string',
        'runId': 'string',
        'decisionTaskCompletedEventId': 123,
        'control': 'string'
    },
    '''

    

    @property
    def workflow_id(self):
        '''
        The workflowId of the external workflow execution to be canceled.
    
        :return string:
        '''
        return self._get_data_attr('workflowId')
    
    
    @property
    def run_id(self):
        '''
        The runId of the external workflow execution to be canceled.
    
        :return string:
        '''
        return self._get_data_attr('runId')
    
    
    @property
    def decision_task_completed_event_id(self):
        '''
        The ID of the DecisionTaskCompleted event corresponding to the decision task that resulted in the RequestCancelExternalWorkflowExecution decision for this cancellation request. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.
    
        :return integer:
        '''
        return self._get_data_attr('decisionTaskCompletedEventId')
    
    
    @property
    def control(self):
        '''
        Data attached to the event that can be used by the decider in subsequent workflow tasks.
    
        :return string:
        '''
        return self._get_data_attr('control')
    
    
