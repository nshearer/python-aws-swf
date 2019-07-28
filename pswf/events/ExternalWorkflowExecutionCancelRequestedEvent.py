# coding=utf-8
from .SWFEvent import SWFEvent

class ExternalWorkflowExecutionCancelRequestedEvent(SWFEvent):
    '''
    Request to cancel an external workflow execution was successfully delivered to the target execution.

    'externalWorkflowExecutionCancelRequestedEventAttributes': {
        'workflowExecution': {
            'workflowId': 'string',
            'runId': 'string'
        },
        'initiatedEventId': 123
    },
    '''

    

    @property
    def workflow_execution(self):
        '''
        The external workflow execution to which the cancellation request was delivered.
    
        workflowId (string) --
        The user defined identifier associated with the workflow execution.
    
        runId (string) --
        A system-generated unique identifier for the workflow execution.
    
        :return dict:
        '''
        return self._get_data_attr('workflowExecution')
    
    
    @property
    def initiated_event_id(self):
        '''
        The ID of the RequestCancelExternalWorkflowExecutionInitiated event corresponding to the RequestCancelExternalWorkflowExecution decision to cancel this external workflow execution. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.
    
        :return integer:
        '''
        return self._get_data_attr('initiatedEventId')
    
    
