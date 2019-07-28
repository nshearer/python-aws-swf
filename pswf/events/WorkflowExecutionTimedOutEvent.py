# coding=utf-8
from .SWFEvent import SWFEvent

class WorkflowExecutionTimedOutEvent(SWFEvent):
    '''
    The workflow execution was closed because a time out was exceeded.

    'workflowExecutionTimedOutEventAttributes': {
        'timeoutType': 'START_TO_CLOSE',
        'childPolicy': 'TERMINATE'|'REQUEST_CANCEL'|'ABANDON'
    },
    '''

    

    @property
    def timeout_type(self):
        '''
        The type of timeout that caused this event.
    
        :return string:
        '''
        return self._get_string_data_attr('timeoutType')
    
    
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
        return self._get_string_data_attr('childPolicy')
    
    
