import random
import string

class Controller(object):

    def __init__(self, db):
        self.db = db

    @staticmethod
    def fix_int(obj, default_value):
        if not obj:
            obj = default_value
        if isinstance(obj, str):
            obj = int(obj)
        if not isinstance(obj, int):
            obj = default_value
        return obj

    @staticmethod
    def random_string(string_length=8):
        letters = string.ascii_lowercase
        return ''.join(random.choice(letters) for i in range(string_length))
