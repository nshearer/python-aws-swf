
from .SWFEvent import SWFEvent
from .all_events import SWF_EVENT_CLASSES
from .exceptions import EventDataError

from ..utils import dpath

def wrap_event_data(data):

    try:
        event_type = data['eventType']
    except KeyError:
        raise EventDataError(data, "Missing required eventType")

    try:
        return SWF_EVENT_CLASSES[event_type](data)
    except KeyError:
        return SWFEvent(data)
