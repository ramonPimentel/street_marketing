from app.utils.logger import Logger
from app.exceptions.aplication_exception import ApplicationException
from app.repositories.street_market_repository import StreetMarketRepository


class FindStreetMarketing():
  def __init__(self, register_code):
    self.register_code = register_code
    self.repository = StreetMarketRepository()
    self._logger = Logger(self.__class__.__name__)

  def execute(self):
    self._logger.info("find street_marketing")
    street_marketing = self.repository.find_by({'registro': self.register_code})

    if not street_marketing:
      raise ApplicationException(
        app_error_code=404,
        msg='Not Found'
      )

    return street_marketing
    
