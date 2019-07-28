# coding=utf-8
from .SWFEvent import SWFEvent

class WorkflowExecutionContinuedAsNewEvent(SWFEvent):
    '''
    The workflow execution was closed and a new execution of the same type was created with the same workflowId.

    'workflowExecutionContinuedAsNewEventAttributes': {
        'input': 'string',
        'decisionTaskCompletedEventId': 123,
        'newExecutionRunId': 'string',
        'executionStartToCloseTimeout': 'string',
        'taskList': {
            'name': 'string'
        },
        'taskPriority': 'string',
        'taskStartToCloseTimeout': 'string',
        'childPolicy': 'TERMINATE'|'REQUEST_CANCEL'|'ABANDON',
        'tagList': [
            'string',
        ],
        'workflowType': {
            'name': 'string',
            'version': 'string'
        },
        'lambdaRole': 'string'
    },
    '''

    

    @property
    def input(self):
        '''
        The input provided to the new workflow execution.
    
        :return string:
        '''
        return self._get_string_data_attr('input')
    
    
    @property
    def decision_task_completed_event_id(self):
        '''
        The ID of the DecisionTaskCompleted event corresponding to the decision task that resulted in the ContinueAsNewWorkflowExecution decision that started this execution. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.
    
        :return integer:
        '''
        return self._get_integer_data_attr('decisionTaskCompletedEventId')
    
    
    @property
    def new_execution_run_id(self):
        '''
        The runId of the new workflow execution.
    
        :return string:
        '''
        return self._get_string_data_attr('newExecutionRunId')
    
    
    @property
    def execution_start_to_close_timeout(self):
        '''
        The total duration allowed for the new workflow execution.
        The duration is specified in seconds, an integer greater than or equal to 0 . You can use NONE to specify unlimited duration.
    
        :return string:
        '''
        return self._get_string_data_attr('executionStartToCloseTimeout')
    
    
    @property
    def task_list(self):
        '''
        The task list to use for the decisions of the new (continued) workflow execution.
    
        name (string) --
        The name of the task list.
    
        :return dict:
        '''
        return self._get_dict_data_attr('taskList')
    
    
    @property
    def task_priority(self):
        '''
        The priority of the task to use for the decisions of the new (continued) workflow execution.
    
        :return string:
        '''
        return self._get_string_data_attr('taskPriority')
    
    
    @property
    def task_start_to_close_timeout(self):
        '''
        The maximum duration of decision tasks for the new workflow execution.
        The duration is specified in seconds, an integer greater than or equal to 0 . You can use NONE to specify unlimited duration.
    
        :return string:
        '''
        return self._get_string_data_attr('taskStartToCloseTimeout')
    
    
    @property
    def child_policy(self):
        '''
        The policy to use for the child workflow executions of the new execution if it is terminated by calling the  TerminateWorkflowExecution action explicitly or due to an expired timeout.
        The supported child policies are:
    
        TERMINATE – The child executions are terminated.
        REQUEST_CANCEL – A request to cancel is attempted for each child execution by recording a WorkflowExecutionCancelRequested event in its history. It is up to the decider to take appropriate actions when it receives an execution history with this event.
        ABANDON – No action is taken. The child executions continue to run.
    
        :return string:
        '''
        return self._get_string_data_attr('childPolicy')
    
    
    @property
    def tag_list(self):
        '''
        The list of tags associated with the new workflow execution.
    
        (string) --
    
        :return list:
        '''
        return self._get_list_data_attr('tagList')
    
    
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
        return self._get_dict_data_attr('workflowType')
    
    
    @property
    def lambda_role(self):
        '''
        The IAM role to attach to the new (continued) workflow execution.
    
        :return string:
        '''
        return self._get_string_data_attr('lambdaRole')
    
    
