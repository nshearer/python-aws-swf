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

    ABANDON = 'ABANDON'
    CHILD_POLICY_APPLIED = 'CHILD_POLICY_APPLIED'
    EVENT_LIMIT_EXCEEDED = 'EVENT_LIMIT_EXCEEDED'
    OPERATOR_INITIATED = 'OPERATOR_INITIATED'
    REQUEST_CANCEL = 'REQUEST_CANCEL'
    TERMINATE = 'TERMINATE'

    @property
    def reason(self):
        return self._get_data_attr('reason')
    
    @property
    def details(self):
        return self._get_data_attr('details')
    
    @property
    def child_policy(self):
        return self._get_data_attr('childPolicy')
    
