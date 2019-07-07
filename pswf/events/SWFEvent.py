
from .utils import dpath

class SWFEvent:
    '''An event in the workflow'''

    def __init__(self, workflow_exec_id, data):
        self.data = data
        #self.__id = EventID(workflow_exec_id, dpath(self.data, 'eventId', required=True))


    def __str__(self):
        return str(self.__id)


    @property
    def event_id(self):
        return self.__id


    @property
    def event_type(self):
        return dpath(self.data, 'eventType', required=True)


    @property
    def event_type_for_decision(self):
        return not self.event_type.startswith('Decision')


def parse_event_list(event_infos):
    print("TODO")