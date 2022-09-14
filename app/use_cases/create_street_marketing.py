from app.utils.logger import Logger
from app.exceptions.aplication_exception import ApplicationException
from app.repositories.street_market_repository import StreetMarketRepository


class CreateStreetMarketing():
  def __init__(self, model):
    self.model = model
    self.repository = StreetMarketRepository()
    self._logger = Logger(self.__class__.__name__)

  def execute(self):
    self.check_exists()
    return self.create()

  def check_exists(self):
    self._logger.info("check street_marketing exists")
    street_marketing = self.repository.find_by({'registro': self.model.registro})
    if street_marketing:
      raise ApplicationException(
        app_error_code=422,
        msg='Model Existis'
      )
  
  def create(self):
    self._logger.info("create street marketing")
    return self.repository.add(self.model)

