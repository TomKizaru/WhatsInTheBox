import uuid

class User(object):
    def __init__(self, level=0, last_challenge=None, uuid=None):
        self.level = level
        self.last_challenge = last_challenge
        self.uuid = uuid or uuid.getnode()
