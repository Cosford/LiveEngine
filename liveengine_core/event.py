from liveengine_core.message import *

class Event(Message):
    def __init__(self, **kwargs):
        pass
    
    def trigger(self):
        pass
    
    def set_content(self, content):
        pass
    
    def on_receive(self):
        pass
    
class EventManager:
    def __init__(self, **kwargs):
        pass
    
    def register_event(self, event_type, on_event):
        pass