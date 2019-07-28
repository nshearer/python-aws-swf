# coding=utf-8
from .SWFEvent import SWFEvent

class WorkflowExecutionTerminatedEvent(SWFEvent):
    '''
    The workflow execution was terminated.

    'workflowExecutionTerminatedEventAttributes': {
        'reason': 'string',
        'details': 'string',
        'childPolicy': 'TERMINATE'|'REQUEST_CANCEL'|'ABANDON',
        'cause': 'CHILD_POLICY_APPLIED'|'EVENT_LIMIT_EXCEEDED'|'OPERATOR_INITIATED'
    },
    '''

    

    @property
    def reason(self):
        '''
        The reason provided for the termination.
    
        :return string:
        '''
        return self._get_data_attr('reason')
    
    
    @property
    def details(self):
        '''
        The details provided for the termination.
    
        :return string:
        '''
        return self._get_data_attr('details')
    
    
    @property
    def child_policy(self):
        '''
        The policy used for the child workflow executions of this workflow execution.
        The supported child policies are:
    
        TERMINATE – The child executions are terminated.
        REQUEST_CANCEL – A request to cancel is attempted for each child execution by recording a WorkflowExecutionCancelRequested event in its history. It is up to the decider to take appropriate actions when it receives an execution history with this event.
        ABANDON – No action is taken. The child executions continue to run.
    
        :return string:
        '''
        return self._get_data_attr('childPolicy')
    
    
    @property
    def cause(self):
        '''
        If set, indicates that the workflow execution was automatically terminated, and specifies the cause. This happens if the parent workflow execution times out or is terminated and the child policy is set to terminate child executions.
    
        :return string:
        '''
        return self._get_data_attr('cause')
    
    
