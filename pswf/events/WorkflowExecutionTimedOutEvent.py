from .SWFEvent import SWFEvent

class WorkflowExecutionTimedOutEvent(SWFEvent):
    '''
    The workflow execution was closed because a time out was exceeded.

    'workflowExecutionTimedOutEventAttributes': {
        'timeoutType': 'START_TO_CLOSE',
        'childPolicy': 'TERMINATE'|'REQUEST_CANCEL'|'ABANDON'
    },
    '''

    ABANDON = 'ABANDON'
    REQUEST_CANCEL = 'REQUEST_CANCEL'
    TERMINATE = 'TERMINATE'

    @property
    def timeout_type(self):
        return self._get_data_attr('timeoutType')
    
