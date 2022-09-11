from app.configs.mongo import Connection
from fastapi.encoders import jsonable_encoder

class BaseRepository:
  def get_db(self):
    conn = Connection()
    session = conn.session_mongo_db
    db = session.test
    return db
  
  def add(self, model):
    data = jsonable_encoder(model)
    del data["_id"]
    result = self.collection.insert_one(data)
    model.id = result.inserted_id
    return model
