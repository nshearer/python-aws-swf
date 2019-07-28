# coding=utf-8
from .SWFEvent import SWFEvent

class ExternalWorkflowExecutionSignaledEvent(SWFEvent):
    '''
    A signal, requested by this workflow execution, was successfully delivered to the target external workflow execution.

    'externalWorkflowExecutionSignaledEventAttributes': {
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
        The external workflow execution that the signal was delivered to.
    
        workflowId (string) --
        The user defined identifier associated with the workflow execution.
    
        runId (string) --
        A system-generated unique identifier for the workflow execution.
    
        :return dict:
        '''
        return self._get_dict_data_attr('workflowExecution')
    
    
    @property
    def initiated_event_id(self):
        '''
        The ID of the SignalExternalWorkflowExecutionInitiated event corresponding to the SignalExternalWorkflowExecution decision to request this signal. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.
    
        :return integer:
        '''
        return self._get_integer_data_attr('initiatedEventId')
    
    
