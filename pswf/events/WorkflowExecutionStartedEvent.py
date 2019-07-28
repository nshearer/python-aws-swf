# coding=utf-8
from .SWFEvent import SWFEvent

class WorkflowExecutionStartedEvent(SWFEvent):
    '''
    The workflow execution was started.

    'workflowExecutionStartedEventAttributes': {
        'input': 'string',
        'executionStartToCloseTimeout': 'string',
        'taskStartToCloseTimeout': 'string',
        'childPolicy': 'TERMINATE'|'REQUEST_CANCEL'|'ABANDON',
        'taskList': {
            'name': 'string'
        },
        'taskPriority': 'string',
        'workflowType': {
            'name': 'string',
            'version': 'string'
        },
        'tagList': [
            'string',
        ],
        'continuedExecutionRunId': 'string',
        'parentWorkflowExecution': {
            'workflowId': 'string',
            'runId': 'string'
        },
        'parentInitiatedEventId': 123,
        'lambdaRole': 'string'
    },
    '''

    

    @property
    def input(self):
        '''
        The input provided to the workflow execution.
    
        :return string:
        '''
        return self._get_data_attr('input')
    
    
    @property
    def execution_start_to_close_timeout(self):
        '''
        The maximum duration for this workflow execution.
        The duration is specified in seconds, an integer greater than or equal to 0 . You can use NONE to specify unlimited duration.
    
        :return string:
        '''
        return self._get_data_attr('executionStartToCloseTimeout')
    
    
    @property
    def task_start_to_close_timeout(self):
        '''
        The maximum duration of decision tasks for this workflow type.
        The duration is specified in seconds, an integer greater than or equal to 0 . You can use NONE to specify unlimited duration.
    
        :return string:
        '''
        return self._get_data_attr('taskStartToCloseTimeout')
    
    
    @property
    def child_policy(self):
        '''
        The policy to use for the child workflow executions if this workflow execution is terminated, by calling the  TerminateWorkflowExecution action explicitly or due to an expired timeout.
        The supported child policies are:
    
        TERMINATE – The child executions are terminated.
        REQUEST_CANCEL – A request to cancel is attempted for each child execution by recording a WorkflowExecutionCancelRequested event in its history. It is up to the decider to take appropriate actions when it receives an execution history with this event.
        ABANDON – No action is taken. The child executions continue to run.
    
        :return string:
        '''
        return self._get_data_attr('childPolicy')
    
    
    @property
    def task_list(self):
        '''
        The name of the task list for scheduling the decision tasks for this workflow execution.
    
        name (string) --
        The name of the task list.
    
        :return dict:
        '''
        return self._get_data_attr('taskList')
    
    
    @property
    def task_priority(self):
        '''
        The priority of the decision tasks in the workflow execution.
    
        :return string:
        '''
        return self._get_data_attr('taskPriority')
    
    
    @property
    def workflow_type(self):
        '''
        The workflow type of this execution.
    
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
    def tag_list(self):
        '''
        The list of tags associated with this workflow execution. An execution can have up to 5 tags.
    
        (string) --
    
        :return list:
        '''
        return self._get_data_attr('tagList')
    
    
    @property
    def continued_execution_run_id(self):
        '''
        If this workflow execution was started due to a ContinueAsNewWorkflowExecution decision, then it contains the runId of the previous workflow execution that was closed and continued as this execution.
    
        :return string:
        '''
        return self._get_data_attr('continuedExecutionRunId')
    
    
    @property
    def parent_workflow_execution(self):
        '''
        The source workflow execution that started this workflow execution. The member isn't set if the workflow execution was not started by a workflow.
    
        workflowId (string) --
        The user defined identifier associated with the workflow execution.
    
        runId (string) --
        A system-generated unique identifier for the workflow execution.
    
        :return dict:
        '''
        return self._get_data_attr('parentWorkflowExecution')
    
    
    @property
    def parent_initiated_event_id(self):
        '''
        The ID of the StartChildWorkflowExecutionInitiated event corresponding to the StartChildWorkflowExecution   Decision to start this workflow execution. The source event with this ID can be found in the history of the source workflow execution. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.
    
        :return integer:
        '''
        return self._get_data_attr('parentInitiatedEventId')
    
    
    @property
    def lambda_role(self):
        '''
        The IAM role attached to the workflow execution.
    
        :return string:
        '''
        return self._get_data_attr('lambdaRole')
    
    
