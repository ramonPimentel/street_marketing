
from repositories.base_repository import BaseRepository

class StreetMarketRepository(BaseRepository):
  def __init__(self):
    db = self.get_db()
    self.collection = db.street_market
  
  def find(self):
    result = self.collection.find_one({})
    return result 
