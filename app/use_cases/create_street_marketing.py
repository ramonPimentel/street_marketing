from app.exceptions.aplication_exception import ApplicationException
from app.repositories.street_market_repository import StreetMarketRepository


class CreateStreetMarketing():
  def __init__(self, model):
    self.model = model
    self.repository = StreetMarketRepository()

  def execute(self):
    self.check_exists()
    self.create()

  def check_exists(self):
    street_marketing = self.repository.find_by_code(self.model.codigo)
    if street_marketing:
       raise ApplicationException(
        app_error_code=422,
        msg='Model Existis'
       )
  
  def create(self):
    self.repository.add(self.model)

