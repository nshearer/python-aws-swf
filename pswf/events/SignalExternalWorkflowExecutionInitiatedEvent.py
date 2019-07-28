# coding=utf-8
from .SWFEvent import SWFEvent

class SignalExternalWorkflowExecutionInitiatedEvent(SWFEvent):
    '''
    A request to signal an external workflow was made.

    'signalExternalWorkflowExecutionInitiatedEventAttributes': {
        'workflowId': 'string',
        'runId': 'string',
        'signalName': 'string',
        'input': 'string',
        'decisionTaskCompletedEventId': 123,
        'control': 'string'
    },
    '''

    

    @property
    def workflow_id(self):
        '''
        The workflowId of the external workflow execution.
    
        :return string:
        '''
        return self._get_data_attr('workflowId')
    
    
    @property
    def run_id(self):
        '''
        The runId of the external workflow execution to send the signal to.
    
        :return string:
        '''
        return self._get_data_attr('runId')
    
    
    @property
    def signal_name(self):
        '''
        The name of the signal.
    
        :return string:
        '''
        return self._get_data_attr('signalName')
    
    
    @property
    def input(self):
        '''
        The input provided to the signal.
    
        :return string:
        '''
        return self._get_data_attr('input')
    
    
    @property
    def decision_task_completed_event_id(self):
        '''
        The ID of the DecisionTaskCompleted event corresponding to the decision task that resulted in the SignalExternalWorkflowExecution decision for this signal. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.
    
        :return integer:
        '''
        return self._get_data_attr('decisionTaskCompletedEventId')
    
    
    @property
    def control(self):
        '''
        Data attached to the event that can be used by the decider in subsequent decision tasks.
    
        :return string:
        '''
        return self._get_data_attr('control')
    
    
