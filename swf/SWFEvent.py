
from .WorkflowID import WokflowExecutionID

from .utils import dpath


class EventID(WokflowExecutionID):
    '''Uniquly identify a Workflow event'''

    def __init__(self, workflow_exec_id, event_id):
        super().__init__(
            wfname = workflow_exec_id.wfname,
            wfver = workflow_exec_id.wfver,
            wfid = workflow_exec_id.wfid,
            run_id = workflow_exec_id.run_id)
        self.__event_id = int(event_id)

    @property
    def event_id(self):
        return self.__event_id

    def __str__(self):
        return "Event %d of "%(self.__event_id) + super().__str__()


class SWFEvent:
    '''An event in the workflow'''

    def __init__(self, workflow_exec_id, data):
        self.data = data
        self.__id = EventID(workflow_exec_id, dpath(self.data, 'eventId', required=True))


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

