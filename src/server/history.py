import json

class HistoryException(Exception):
    pass

class History:
    def __init__(self, filename):
        self.filename = filename
        with open(filename) as f:
            database = json.load(f)
        self.__database = database
        self.__users = database["users"]
