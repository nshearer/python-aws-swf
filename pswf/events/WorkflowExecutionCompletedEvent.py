from .SWFEvent import SWFEvent

class WorkflowExecutionCompletedEvent(SWFEvent):
    '''
    The workflow execution was closed due to successful completion.

    'workflowExecutionCompletedEventAttributes': {
        'result': 'string',
        'decisionTaskCompletedEventId': 123
    },
    '''

    

    @property
    def result(self):
        return self._get_data_attr('result')
    
