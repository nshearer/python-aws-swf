from .SWFEvent import SWFEvent

class DecisionTaskScheduledEvent(SWFEvent):
    '''
    A decision task was scheduled for the workflow execution.

    'decisionTaskScheduledEventAttributes': {
        'taskList': {
            'name': 'string'
        },
        'taskPriority': 'string',
        'startToCloseTimeout': 'string'
    },
    '''

    

    @property
    def task_priority(self):
        return self._get_data_attr('taskPriority')
    
