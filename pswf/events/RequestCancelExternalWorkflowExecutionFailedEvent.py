# coding=utf-8
from .SWFEvent import SWFEvent

class RequestCancelExternalWorkflowExecutionFailedEvent(SWFEvent):
    '''
    Request to cancel an external workflow execution failed.

    'requestCancelExternalWorkflowExecutionFailedEventAttributes': {
        'workflowId': 'string',
        'runId': 'string',
        'cause': 'UNKNOWN_EXTERNAL_WORKFLOW_EXECUTION'|'REQUEST_CANCEL_EXTERNAL_WORKFLOW_EXECUTION_RATE_EXCEEDED'|'OPERATION_NOT_PERMITTED',
        'initiatedEventId': 123,
        'decisionTaskCompletedEventId': 123,
        'control': 'string'
    },
    '''

    

    @property
    def workflow_id(self):
        '''
        The workflowId of the external workflow to which the cancel request was to be delivered.
    
        :return string:
        '''
        return self._get_data_attr('workflowId')
    
    
    @property
    def run_id(self):
        '''
        The runId of the external workflow execution.
    
        :return string:
        '''
        return self._get_data_attr('runId')
    
    
    @property
    def cause(self):
        '''
        The cause of the failure. This information is generated by the system and can be useful for diagnostic purposes.
    
        Note
        If cause is set to OPERATION_NOT_PERMITTED , the decision failed because it lacked sufficient permissions. For details and example IAM policies, see Using IAM to Manage Access to Amazon SWF Workflows in the Amazon SWF Developer Guide .
    
        :return string:
        '''
        return self._get_data_attr('cause')
    
    
    @property
    def initiated_event_id(self):
        '''
        The ID of the RequestCancelExternalWorkflowExecutionInitiated event corresponding to the RequestCancelExternalWorkflowExecution decision to cancel this external workflow execution. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.
    
        :return integer:
        '''
        return self._get_data_attr('initiatedEventId')
    
    
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
        The data attached to the event that the decider can use in subsequent workflow tasks. This data isn't sent to the workflow execution.
    
        :return string:
        '''
        return self._get_data_attr('control')
    
    
