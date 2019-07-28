# coding=utf-8
from .SWFEvent import SWFEvent

class WorkflowExecutionSignaledEvent(SWFEvent):
    '''
    An external signal was received for the workflow execution.

    'workflowExecutionSignaledEventAttributes': {
        'signalName': 'string',
        'input': 'string',
        'externalWorkflowExecution': {
            'workflowId': 'string',
            'runId': 'string'
        },
        'externalInitiatedEventId': 123
    },
    '''

    

    @property
    def signal_name(self):
        '''
        The name of the signal received. The decider can use the signal name and inputs to determine how to the process the signal.
    
        :return string:
        '''
        return self._get_string_data_attr('signalName')
    
    
    @property
    def input(self):
        '''
        The inputs provided with the signal. The decider can use the signal name and inputs to determine how to process the signal.
    
        :return string:
        '''
        return self._get_string_data_attr('input')
    
    
    @property
    def external_workflow_execution(self):
        '''
        The workflow execution that sent the signal. This is set only of the signal was sent by another workflow execution.
    
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
        The ID of the SignalExternalWorkflowExecutionInitiated event corresponding to the SignalExternalWorkflow decision to signal this workflow execution.The source event with this ID can be found in the history of the source workflow execution. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event. This field is set only if the signal was initiated by another workflow execution.
    
        :return integer:
        '''
        return self._get_integer_data_attr('externalInitiatedEventId')
    
    
