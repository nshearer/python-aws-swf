
class EventDataError(Exception):
    def __init__(self, data, error):
        self.event_data = data
        super(EventDataError, self).__init__(error)
