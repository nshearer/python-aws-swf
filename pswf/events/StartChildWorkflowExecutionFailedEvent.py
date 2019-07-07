from .SWFEvent import SWFEvent

class StartChildWorkflowExecutionFailedEvent(SWFEvent):
    '''
    Failed to process StartChildWorkflowExecution decision. This happens when the decision isn't configured properly, for example the workflow type specified isn't registered.

    'startChildWorkflowExecutionFailedEventAttributes': {
        'workflowType': {
            'name': 'string',
            'version': 'string'
        },
        'cause': 'WORKFLOW_TYPE_DOES_NOT_EXIST'|'WORKFLOW_TYPE_DEPRECATED'|'OPEN_CHILDREN_LIMIT_EXCEEDED'|'OPEN_WORKFLOWS_LIMIT_EXCEEDED'|'CHILD_CREATION_RATE_EXCEEDED'|'WORKFLOW_ALREADY_RUNNING'|'DEFAULT_EXECUTION_START_TO_CLOSE_TIMEOUT_UNDEFINED'|'DEFAULT_TASK_LIST_UNDEFINED'|'DEFAULT_TASK_START_TO_CLOSE_TIMEOUT_UNDEFINED'|'DEFAULT_CHILD_POLICY_UNDEFINED'|'OPERATION_NOT_PERMITTED',
        'workflowId': 'string',
        'initiatedEventId': 123,
        'decisionTaskCompletedEventId': 123,
        'control': 'string'
    },
    '''

    CHILD_CREATION_RATE_EXCEEDED = 'CHILD_CREATION_RATE_EXCEEDED'
    DEFAULT_CHILD_POLICY_UNDEFINED = 'DEFAULT_CHILD_POLICY_UNDEFINED'
    DEFAULT_EXECUTION_START_TO_CLOSE_TIMEOUT_UNDEFINED = 'DEFAULT_EXECUTION_START_TO_CLOSE_TIMEOUT_UNDEFINED'
    DEFAULT_TASK_LIST_UNDEFINED = 'DEFAULT_TASK_LIST_UNDEFINED'
    DEFAULT_TASK_START_TO_CLOSE_TIMEOUT_UNDEFINED = 'DEFAULT_TASK_START_TO_CLOSE_TIMEOUT_UNDEFINED'
    OPEN_CHILDREN_LIMIT_EXCEEDED = 'OPEN_CHILDREN_LIMIT_EXCEEDED'
    OPEN_WORKFLOWS_LIMIT_EXCEEDED = 'OPEN_WORKFLOWS_LIMIT_EXCEEDED'
    OPERATION_NOT_PERMITTED = 'OPERATION_NOT_PERMITTED'
    WORKFLOW_ALREADY_RUNNING = 'WORKFLOW_ALREADY_RUNNING'
    WORKFLOW_TYPE_DEPRECATED = 'WORKFLOW_TYPE_DEPRECATED'
    WORKFLOW_TYPE_DOES_NOT_EXIST = 'WORKFLOW_TYPE_DOES_NOT_EXIST'

    @property
    def cause(self):
        return self._get_data_attr('cause')
    
    @property
    def workflow_id(self):
        return self._get_data_attr('workflowId')
    
    @property
    def initiated_event_id(self):
        return self._get_data_attr('initiatedEventId')
    
    @property
    def decision_task_completed_event_id(self):
        return self._get_data_attr('decisionTaskCompletedEventId')
    
