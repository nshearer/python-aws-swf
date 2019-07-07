from .SWFEvent import SWFEvent

class DecisionTaskCompletedEvent(SWFEvent):
    '''
    The decider successfully completed a decision task by calling RespondDecisionTaskCompleted.

    'decisionTaskCompletedEventAttributes': {
        'executionContext': 'string',
        'scheduledEventId': 123,
        'startedEventId': 123
    },
    '''

    

    @property
    def execution_context(self):
        return self._get_data_attr('executionContext')
    
    @property
    def scheduled_event_id(self):
        return self._get_data_attr('scheduledEventId')
    
