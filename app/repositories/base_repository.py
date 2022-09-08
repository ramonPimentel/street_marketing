from configs.mongo import Connection

class BaseRepository:
  def get_db(self):
    conn = Connection()
    session = conn.session_mongo_db
    db = session.test
    return db
  
  def add(self, data):
    result = self.collection.insert_one(data)
    return result
