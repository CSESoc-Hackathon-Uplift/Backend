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
    
    def __save_to_database(self):
        with open(self.filename, "w+") as f:
            json.dump(self.__database, f)
    
    def add(self, uuid, title, source, score, author, date_added):
        """Add a new article as read by user `uuid`."""
        if uuid not in self.__users:
            self.__users[uuid] = []
        
        self.__users[uuid].append({
            "title": title,
            "source": source,
            "score": score,
            "author": author,
            "date_added": date_added
        })

        self.__save_to_database()
        
        return "success"
