import uuid


class User(object):
    def __init__(self, level=0, last_challenge=None, user_id=None):
        self.level = level
        self.last_challenge = last_challenge
        self.user_id = user_id or uuid.getnode()
