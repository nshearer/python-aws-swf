from datetime import timedelta


from lru import LRUCache


class EventCache(LRUCache):
    '''
    Cache event data so that we don't have to pull entire event history from SWF every time.

    Events are uniquely identified within a workflow execution by their integer eventID.
    They look sequential, but I can't confirm that's guaranteed.
    '''


    def __init__(self):
        super(EventCache, self).__init__(max_size=1024*1024, max_age=timedelta(days=1))


    def has_event(self, run_id, event_id):
        '''Check to see if event_id is known for a workflow'''
        if run_id in self:
            data = self[run_id]
            return run_id

