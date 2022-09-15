
from app.models.street_marketing_model import StreetMarketing
from app.repositories.base_repository import BaseRepository
from mongonator import Paginate, ASCENDING

class StreetMarketRepository(BaseRepository):
  def __init__(self):
    db = self.get_db()
    self.collection = db.feira_livres

  def find_by(self, query):
    result = self.collection.find_one(query)
    if result:
      return StreetMarketing(**result)
    
  def delete_by_register_code(self, register_code):
    self.collection.delete_one({"registro": register_code})

  def update(self, _id, data):
    self.collection.update_one({"_id": _id}, {"$set": data}, upsert=True)

  def search(
    self,
    query={},
    next_page=None,
    prev_page=None
  ):

    paginator = Paginate(
      collection=self.collection,
      query=query,
      limit=30,
      ordering_field='registro',
      ordering_case=ASCENDING,
      projection={'registro': True, 'nome_feira': True, 'region5': True, 'bairro': True },
      prev_page=prev_page,
      next_page=next_page,
      automatic_pagination=False
    ).paginate()

    return paginator
