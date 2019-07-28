# coding=utf-8
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
    def task_list(self):
        '''
        The name of the task list in which the decision task was scheduled.
    
        name (string) --
        The name of the task list.
    
        :return dict:
        '''
        return self._get_dict_data_attr('taskList')
    
    
    @property
    def task_priority(self):
        '''
        A task priority that, if set, specifies the priority for this decision task. Valid values are integers that range from Java's Integer.MIN_VALUE (-2147483648) to Integer.MAX_VALUE (2147483647). Higher numbers indicate higher priority.
        For more information about setting task priority, see Setting Task Priority in the Amazon SWF Developer Guide .
    
        :return string:
        '''
        return self._get_string_data_attr('taskPriority')
    
    
    @property
    def start_to_close_timeout(self):
        '''
        The maximum duration for this decision task. The task is considered timed out if it doesn't completed within this duration.
        The duration is specified in seconds, an integer greater than or equal to 0 . You can use NONE to specify unlimited duration.
    
        :return string:
        '''
        return self._get_string_data_attr('startToCloseTimeout')
    
    
