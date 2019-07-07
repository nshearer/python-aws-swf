from .SWFEvent import SWFEvent

class StartLambdaFunctionFailedEvent(SWFEvent):
    '''
    StartLambdaFunctionFailedEvent event

                'startLambdaFunctionFailedEventAttributes': {
                    'scheduledEventId': 123,
                    'cause': 'ASSUME_ROLE_FAILED',
                    'message': 'string'
                }
            },
        ],
        'nextPageToken': 'string',
        'previousStartedEventId': 123
    }
    '''

    

    @property
    def scheduled_event_id(self):
        return self._get_data_attr('scheduledEventId')
    
    @property
    def cause(self):
        return self._get_data_attr('cause')
    
