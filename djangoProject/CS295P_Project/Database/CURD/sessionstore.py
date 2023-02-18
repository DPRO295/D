import pymongo
import datetime
import uuid

class MongoDBSessionStore:
    def __init__(self, client, session_key=None):
        self.client = client
        self.db = self.client["mydatabase"]
        self.collection = self.db["sessions"]

        if session_key is not None:
            data = self.collection.find_one({"session_key": session_key})
            if data is not None:
                self._session = data["session_data"]
            else:
                self._session = {}

    def load(self):
        return self._session

    def create(self):
        session_key = str(uuid.uuid4())
        self._session_key = session_key
        self._session = {}
        self.collection.insert_one({
            "session_key": session_key,
            "session_data": self._session,
            "last_accessed": datetime.datetime.utcnow()
        })

    def save(self, must_create=False):
        self.collection.update_one(
            {"session_key": self.session_key},
            {"$set": {"session_data": self._session, "last_accessed": datetime.datetime.utcnow()}},
            upsert=True
        )

    def exists(self, session_key):
        data = self.collection.find_one({"session_key": session_key})
        return data is not None

    def delete(self, session_key=None):
        if session_key is None:
            session_key = self.session_key
        self.collection.delete_one({"session_key": session_key})
        self._session = {}

    def flush(self):
        self._session = {}

    @classmethod
    def clear_expired(cls):
        cls.collection.delete_many({"last_accessed": {"$lt": datetime.datetime.utcnow() - datetime.timedelta(seconds=3600)}})
