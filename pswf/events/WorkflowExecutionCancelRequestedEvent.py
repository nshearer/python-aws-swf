# coding=utf-8
from .SWFEvent import SWFEvent

class WorkflowExecutionCancelRequestedEvent(SWFEvent):
    '''
    A request to cancel this workflow execution was made.

    'workflowExecutionCancelRequestedEventAttributes': {
        'externalWorkflowExecution': {
            'workflowId': 'string',
            'runId': 'string'
        },
        'externalInitiatedEventId': 123,
        'cause': 'CHILD_POLICY_APPLIED'
    },
    '''

    

    @property
    def external_workflow_execution(self):
        '''
        The external workflow execution for which the cancellation was requested.
    
        workflowId (string) --
        The user defined identifier associated with the workflow execution.
    
        runId (string) --
        A system-generated unique identifier for the workflow execution.
    
        :return dict:
        '''
        return self._get_dict_data_attr('externalWorkflowExecution')
    
    
    @property
    def external_initiated_event_id(self):
        '''
        The ID of the RequestCancelExternalWorkflowExecutionInitiated event corresponding to the RequestCancelExternalWorkflowExecution decision to cancel this workflow execution.The source event with this ID can be found in the history of the source workflow execution. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.
    
        :return integer:
        '''
        return self._get_integer_data_attr('externalInitiatedEventId')
    
    
    @property
    def cause(self):
        '''
        If set, indicates that the request to cancel the workflow execution was automatically generated, and specifies the cause. This happens if the parent workflow execution times out or is terminated, and the child policy is set to cancel child executions.
    
        :return string:
        '''
        return self._get_string_data_attr('cause')
    
    
