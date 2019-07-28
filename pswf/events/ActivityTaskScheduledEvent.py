# coding=utf-8
from .SWFEvent import SWFEvent

class ActivityTaskScheduledEvent(SWFEvent):
    '''
    An activity task was scheduled for execution.

    'activityTaskScheduledEventAttributes': {
        'activityType': {
            'name': 'string',
            'version': 'string'
        },
        'activityId': 'string',
        'input': 'string',
        'control': 'string',
        'scheduleToStartTimeout': 'string',
        'scheduleToCloseTimeout': 'string',
        'startToCloseTimeout': 'string',
        'taskList': {
            'name': 'string'
        },
        'taskPriority': 'string',
        'decisionTaskCompletedEventId': 123,
        'heartbeatTimeout': 'string'
    },
    '''

    

    @property
    def activity_type(self):
        '''
        The type of the activity task.
    
        name (string) --
        The name of this activity.
    
        Note
        The combination of activity type name and version must be unique within a domain.
    
    
        version (string) --
        The version of this activity.
    
        Note
        The combination of activity type name and version must be unique with in a domain.
    
        :return dict:
        '''
        return self._get_dict_data_attr('activityType')
    
    
    @property
    def activity_id(self):
        '''
        The unique ID of the activity task.
    
        :return string:
        '''
        return self._get_string_data_attr('activityId')
    
    
    @property
    def input(self):
        '''
        The input provided to the activity task.
    
        :return string:
        '''
        return self._get_string_data_attr('input')
    
    
    @property
    def control(self):
        '''
        Data attached to the event that can be used by the decider in subsequent workflow tasks. This data isn't sent to the activity.
    
        :return string:
        '''
        return self._get_string_data_attr('control')
    
    
    @property
    def schedule_to_start_timeout(self):
        '''
        The maximum amount of time the activity task can wait to be assigned to a worker.
    
        :return string:
        '''
        return self._get_string_data_attr('scheduleToStartTimeout')
    
    
    @property
    def schedule_to_close_timeout(self):
        '''
        The maximum amount of time for this activity task.
    
        :return string:
        '''
        return self._get_string_data_attr('scheduleToCloseTimeout')
    
    
    @property
    def start_to_close_timeout(self):
        '''
        The maximum amount of time a worker may take to process the activity task.
    
        :return string:
        '''
        return self._get_string_data_attr('startToCloseTimeout')
    
    
    @property
    def task_list(self):
        '''
        The task list in which the activity task has been scheduled.
    
        name (string) --
        The name of the task list.
    
        :return dict:
        '''
        return self._get_dict_data_attr('taskList')
    
    
    @property
    def task_priority(self):
        '''
        The priority to assign to the scheduled activity task. If set, this overrides any default priority value that was assigned when the activity type was registered.
        Valid values are integers that range from Java's Integer.MIN_VALUE (-2147483648) to Integer.MAX_VALUE (2147483647). Higher numbers indicate higher priority.
        For more information about setting task priority, see Setting Task Priority in the Amazon SWF Developer Guide .
    
        :return string:
        '''
        return self._get_string_data_attr('taskPriority')
    
    
    @property
    def decision_task_completed_event_id(self):
        '''
        The ID of the DecisionTaskCompleted event corresponding to the decision that resulted in the scheduling of this activity task. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.
    
        :return integer:
        '''
        return self._get_integer_data_attr('decisionTaskCompletedEventId')
    
    
    @property
    def heartbeat_timeout(self):
        '''
        The maximum time before which the worker processing this task must report progress by calling  RecordActivityTaskHeartbeat . If the timeout is exceeded, the activity task is automatically timed out. If the worker subsequently attempts to record a heartbeat or return a result, it is ignored.
    
        :return string:
        '''
        return self._get_string_data_attr('heartbeatTimeout')
    
    
