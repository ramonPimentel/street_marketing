
from app.models.street_marketing_model import StreetMarketing
from app.repositories.base_repository import BaseRepository
from mongonator import Paginate, ASCENDING

class StreetMarketRepository(BaseRepository):
  def __init__(self):
    db = self.get_db()
    self.collection = db.street_market
  
  def find_by_code(self, code):
    result = self.collection.find_one({"codigo": code})
    if result:
      return StreetMarketing(**result)
    
  def delete_by_code(self, code):
    return self.collection.delete_one({"codigo": code})

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
