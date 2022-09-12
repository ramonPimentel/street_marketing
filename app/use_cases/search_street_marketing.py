from app.repositories.street_market_repository import StreetMarketRepository


class SearchStreetMarketing():
  def __init__(self, query):
    self.query = query
    self.repository = StreetMarketRepository()

  def execute(self):
    return self.repository.search(self.query)