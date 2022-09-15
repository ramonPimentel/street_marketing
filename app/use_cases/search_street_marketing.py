from app.repositories.street_market_repository import StreetMarketRepository
from app.utils.logger import Logger

class SearchStreetMarketing():
  def __init__(self,
    district=None,
    region=None,
    name=None,
    neighborhood=None,
    next_page=None,
    prev_page=None,
  ):
    self.district = district
    self.region = region
    self.name = name
    self.neighborhood = neighborhood
    self.next_page = next_page
    self.prev_page = prev_page
    self.repository = StreetMarketRepository()
    self._logger = Logger(self.__class__.__name__)

  def execute(self):
    self._logger.info("start search")
    query = {}

    if self.district:
      query['distrito'] = { '$eq' : self.district }

    if self.neighborhood:
      query['bairro'] = { '$eq' : self.neighborhood }
    
    if self.name:
      query['nome_feira'] = { '$eq' : self.name }
    
    if self.region:
      query['regiao5'] = { '$eq' : self.region }

    self._logger.info(f"query {query}")
      
    return self.repository.search(
      query=query,
      next_page=self.next_page,
      prev_page=self.prev_page
    )
