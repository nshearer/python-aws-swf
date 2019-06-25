
from datetime import datetime, timedelta

class EventAlreadySeen(Exception): pass


class WorkflowExecution:
    '''Data container for a running instance'''

    def __init__(self, exec_id):
        '''
        Get instance data for the given execution of the workflow

        :param exec_id: WokflowExecutionID
        '''
        self.__id = exec_id
        self.__last_used = None
        self.__events = dict()

        self.wfdata = dict()

        self.tap_last_used()


    @property
    def exec_id(self):
        return self.__id


    def tap_last_used(self):
        self.__last_used = datetime.now()


    @property
    def last_used(self):
        return self.__last_used
    @property
    def age(self):
        return datetime.now() - self.__last_used


    def seen_event(self, event):
        '''Check to see if event has already been added'''
        return event.event_id in self.__events


    def add_event(self, event):
        if event.event_id in self.__events:
            raise KeyError("Event already added")



class WorkflowExecutionCollection:
    '''Collection of workflow instances which manages disk caching'''

    MAX_CACHED_WORKFLOW_CNT = 1000
    MAX_CACHED_WORKFLOW_AGE = timedelta(hours=1)
    CHECK_EXPIRE_EVERY = timedelta(minutes=1)

    def __init__(self):
        self.__instances = dict() # [WokflowExecutionID()] = instance
        self.__check_expire = datetime.now() + self.CHECK_EXPIRE_EVERY

    def get(self, exec_id):
        '''Get (or create) an workflow instance data container for a running workflow'''

        # Clean if to many cached
        if len(self.__instances) > self.MAX_CACHED_WORKFLOW_CNT:
            keep = int(0.75*self.MAX_CACHED_WORKFLOW_CNT)
            self.__instances = list(sorted(self.__instances.values(), key=lambda i: i.last_used, reverse=True))
            self.__instances[:keep]
            self.__instances = {i.exec_id: i for i in self.__instances}

        try:
            self.__instances[exec_id].tap_last_used()
            return self.__instances[exec_id]
        except KeyError:

            # Expire old entries
            if datetime.now() > self.__check_expire:
                self.__instances = {i.exec_id: i for i in self.__instances.values()
                                    if i.age < self.MAX_CACHED_WORKFLOW_AGE}
                self.__check_expire = datetime.now() + self.CHECK_EXPIRE_EVERY

            # Build new entry
            self.__instances[exec_id] = WorkflowExecution(exec_id)
            return self.__instances[exec_id]
