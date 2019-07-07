from .SWFEvent import SWFEvent

class DecisionTaskStartedEvent(SWFEvent):
    '''
    The decision task was dispatched to a decider.

    'decisionTaskStartedEventAttributes': {
        'identity': 'string',
        'scheduledEventId': 123
    },
    '''

    

    @property
    def identity(self):
        return self._get_data_attr('identity')
    
