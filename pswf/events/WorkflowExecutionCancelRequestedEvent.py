from .SWFEvent import SWFEvent

class WorkflowExecutionCancelRequestedEvent(SWFEvent):
    '''
    A request to cancel this workflow execution was made.

    'workflowExecutionCancelRequestedEventAttributes': {
        'externalWorkflowExecution': {
            'workflowId': 'string',
            'runId': 'string'
        },
        'externalInitiatedEventId': 123,
        'cause': 'CHILD_POLICY_APPLIED'
    },
    '''

    

    @property
    def external_initiated_event_id(self):
        return self._get_data_attr('externalInitiatedEventId')
    
