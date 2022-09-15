from app.configs.settings import settings
import pymongo

class Connection:
  def __init__(self):
    self.session_mongo_db = pymongo.MongoClient(settings.database_url, 27017)