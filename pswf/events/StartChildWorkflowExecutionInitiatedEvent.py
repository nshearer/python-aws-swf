# coding=utf-8
from .SWFEvent import SWFEvent

class StartChildWorkflowExecutionInitiatedEvent(SWFEvent):
    '''
    A request was made to start a child workflow execution.

    'startChildWorkflowExecutionInitiatedEventAttributes': {
        'workflowId': 'string',
        'workflowType': {
            'name': 'string',
            'version': 'string'
        },
        'control': 'string',
        'input': 'string',
        'executionStartToCloseTimeout': 'string',
        'taskList': {
            'name': 'string'
        },
        'taskPriority': 'string',
        'decisionTaskCompletedEventId': 123,
        'childPolicy': 'TERMINATE'|'REQUEST_CANCEL'|'ABANDON',
        'taskStartToCloseTimeout': 'string',
        'tagList': [
            'string',
        ],
        'lambdaRole': 'string'
    },
    '''

    

    @property
    def workflow_id(self):
        '''
        The workflowId of the child workflow execution.
    
        :return string:
        '''
        return self._get_string_data_attr('workflowId')
    
    
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
        return self._get_dict_data_attr('workflowType')
    
    
    @property
    def control(self):
        '''
        Data attached to the event that can be used by the decider in subsequent decision tasks. This data isn't sent to the activity.
    
        :return string:
        '''
        return self._get_string_data_attr('control')
    
    
    @property
    def input(self):
        '''
        The inputs provided to the child workflow execution.
    
        :return string:
        '''
        return self._get_string_data_attr('input')
    
    
    @property
    def execution_start_to_close_timeout(self):
        '''
        The maximum duration for the child workflow execution. If the workflow execution isn't closed within this duration, it is timed out and force-terminated.
        The duration is specified in seconds, an integer greater than or equal to 0 . You can use NONE to specify unlimited duration.
    
        :return string:
        '''
        return self._get_string_data_attr('executionStartToCloseTimeout')
    
    
    @property
    def task_list(self):
        '''
        The name of the task list used for the decision tasks of the child workflow execution.
    
        name (string) --
        The name of the task list.
    
        :return dict:
        '''
        return self._get_dict_data_attr('taskList')
    
    
    @property
    def task_priority(self):
        '''
        The priority assigned for the decision tasks for this workflow execution. Valid values are integers that range from Java's Integer.MIN_VALUE (-2147483648) to Integer.MAX_VALUE (2147483647). Higher numbers indicate higher priority.
        For more information about setting task priority, see Setting Task Priority in the Amazon SWF Developer Guide .
    
        :return string:
        '''
        return self._get_string_data_attr('taskPriority')
    
    
    @property
    def decision_task_completed_event_id(self):
        '''
        The ID of the DecisionTaskCompleted event corresponding to the decision task that resulted in the StartChildWorkflowExecution   Decision to request this child workflow execution. This information can be useful for diagnosing problems by tracing back the cause of events.
    
        :return integer:
        '''
        return self._get_integer_data_attr('decisionTaskCompletedEventId')
    
    
    @property
    def child_policy(self):
        '''
        The policy to use for the child workflow executions if this execution gets terminated by explicitly calling the  TerminateWorkflowExecution action or due to an expired timeout.
        The supported child policies are:
    
        TERMINATE – The child executions are terminated.
        REQUEST_CANCEL – A request to cancel is attempted for each child execution by recording a WorkflowExecutionCancelRequested event in its history. It is up to the decider to take appropriate actions when it receives an execution history with this event.
        ABANDON – No action is taken. The child executions continue to run.
    
        :return string:
        '''
        return self._get_string_data_attr('childPolicy')
    
    
    @property
    def task_start_to_close_timeout(self):
        '''
        The maximum duration allowed for the decision tasks for this workflow execution.
        The duration is specified in seconds, an integer greater than or equal to 0 . You can use NONE to specify unlimited duration.
    
        :return string:
        '''
        return self._get_string_data_attr('taskStartToCloseTimeout')
    
    
    @property
    def tag_list(self):
        '''
        The list of tags to associated with the child workflow execution.
    
        (string) --
    
        :return list:
        '''
        return self._get_list_data_attr('tagList')
    
    
    @property
    def lambda_role(self):
        '''
        The IAM role to attach to the child workflow execution.
    
        :return string:
        '''
        return self._get_string_data_attr('lambdaRole')
    
    
