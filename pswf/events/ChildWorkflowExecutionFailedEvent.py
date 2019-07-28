# coding=utf-8
from .SWFEvent import SWFEvent

class ChildWorkflowExecutionFailedEvent(SWFEvent):
    '''
    A child workflow execution, started by this workflow execution, failed to complete successfully and was closed.

    'childWorkflowExecutionFailedEventAttributes': {
        'workflowExecution': {
            'workflowId': 'string',
            'runId': 'string'
        },
        'workflowType': {
            'name': 'string',
            'version': 'string'
        },
        'reason': 'string',
        'details': 'string',
        'initiatedEventId': 123,
        'startedEventId': 123
    },
    '''

    

    @property
    def workflow_execution(self):
        '''
        The child workflow execution that failed.
    
        workflowId (string) --
        The user defined identifier associated with the workflow execution.
    
        runId (string) --
        A system-generated unique identifier for the workflow execution.
    
        :return dict:
        '''
        return self._get_data_attr('workflowExecution')
    
    
    @property
    def workflow_type(self):
        '''
        The type of the child workflow execution.
    
        name (string) --
        The name of the workflow type.
    
        Note
        The combination of workflow type name and version must be unique with in a domain.
    
    
        version (string) --
        The version of the workflow type.
    
        Note
        The combination of workflow type name and version must be unique with in a domain.
    
        :return dict:
        '''
        return self._get_data_attr('workflowType')
    
    
    @property
    def reason(self):
        '''
        The reason for the failure (if provided).
    
        :return string:
        '''
        return self._get_data_attr('reason')
    
    
    @property
    def details(self):
        '''
        The details of the failure (if provided).
    
        :return string:
        '''
        return self._get_data_attr('details')
    
    
    @property
    def initiated_event_id(self):
        '''
        The ID of the StartChildWorkflowExecutionInitiated event corresponding to the StartChildWorkflowExecution   Decision to start this child workflow execution. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.
    
        :return integer:
        '''
        return self._get_data_attr('initiatedEventId')
    
    
    @property
    def started_event_id(self):
        '''
        The ID of the ChildWorkflowExecutionStarted event recorded when this child workflow execution was started. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.
    
        :return integer:
        '''
        return self._get_data_attr('startedEventId')
    
    
