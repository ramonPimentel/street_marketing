from app.exceptions.aplication_exception import ApplicationException
from app.repositories.street_market_repository import StreetMarketRepository
from app.utils.logger import Logger


class DeleteStreetMarketing():
  def __init__(self, id):
    self.id = id
    self.repository = StreetMarketRepository()
    self._logger = Logger(self.__class__.__name__)

  def execute(self):
    self.check_exists()
    self.delete()

  def check_exists(self):
    self._logger.info("check street marketing exists")
    self.street_marketing = self.repository.find_by_code(self.id)
    if not self.street_marketing:
      raise ApplicationException(
        app_error_code=404,
        msg='Model not Existis'
      )
  
  def delete(self):
    self._logger.info("delete street marketing")
    self.repository.delete_by_code(self.id)
