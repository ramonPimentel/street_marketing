import pymongo

class Connection:
  def __init__(self):
    self.session_mongo_db = pymongo.MongoClient('mongodb://mongo:27017/my_mongo', 27017)