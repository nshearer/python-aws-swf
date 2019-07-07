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
    def activity_id(self):
        return self._get_data_attr('activityId')
    
    @property
    def input(self):
        return self._get_data_attr('input')
    
    @property
    def control(self):
        return self._get_data_attr('control')
    
    @property
    def schedule_to_start_timeout(self):
        return self._get_data_attr('scheduleToStartTimeout')
    
    @property
    def schedule_to_close_timeout(self):
        return self._get_data_attr('scheduleToCloseTimeout')
    
    @property
    def start_to_close_timeout(self):
        return self._get_data_attr('startToCloseTimeout')
    
    @property
    def task_priority(self):
        return self._get_data_attr('taskPriority')
    
    @property
    def decision_task_completed_event_id(self):
        return self._get_data_attr('decisionTaskCompletedEventId')
    
