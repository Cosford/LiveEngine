import random
from enum import Enum

class LiveEngineMessage(Enum):
    NONE = 0
    REGISTRATION = 1
    CONFIGURATION = 2
    EVENT = 3
    DATA = 4

class Message:
    def __init__(self, **kwargs):
        self.id         = random.randint(0, 4294967295),
        self.sender     = kwargs.get('sender', None)
        self.receiver   = kwargs.get('receiver', None)
        self.broadcast  = kwargs.get('broadcast', False)
        self.type       = kwargs.get('type', LiveEngineMessage.NONE)
        self.ack        = kwargs.get('ack', False)
        self.ack_req    = kwargs.get('ack_req', False)
        
        self.header = {
            "id"        : self.id,
            "sender"    : self.sender,
            "receiver"  : self.receiver,
            "broadcast" : self.broadcast,
            "type"      : self.type,
            "ack"       : self.ack
        }
        self.content = {}
    
    def build(self):
        pass
    
    def set_content(self, new_content):
        self.content = new_content
    
    def get_dict(self):
        return {
            "header" : self.header,
            "content" : self.content
        }