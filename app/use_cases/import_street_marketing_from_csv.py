import csv

from app.models.street_marketing_model import StreetMarketing
from app.repositories.street_market_repository import StreetMarketRepository
from app.routes.street_marketing_router import create, update
from app.schemas.update_street_marketing_schema import UpdateStreetMarketingSchema
from app.use_cases.create_street_marketing import CreateStreetMarketing
from app.use_cases.update_sreet_marketing import UpdateStreetMarketing
from app.utils.logger import Logger

class ImportStreetMarketingFromCSV:
  def __init__(self, file_path):
    self.file_path = file_path
    self.repository = StreetMarketRepository()
    self._logger = Logger(self.__class__.__name__)

  def execute(self):
    self._logger.info('start process')
    with open(self.file_path, newline='') as csvfile:
      spamreader = csv.reader(csvfile, delimiter=',', quotechar=',')
      for row in spamreader:
        
        if row[0] != 'ID':
          data = {
            'long': self.get_index_of_array(row, 1),
            'lat': self.get_index_of_array(row, 2),
            'setcens': self.get_index_of_array(row, 3),
            'areap': self.get_index_of_array(row, 4),
            'cod_dist': self.get_index_of_array(row, 5),
            'distrito': self.get_index_of_array(row, 6),
            'cod_subpref': self.get_index_of_array(row, 7),
            'subpref': self.get_index_of_array(row, 8),
            'regiao5': self.get_index_of_array(row, 9),
            'regiao8': self.get_index_of_array(row, 10),
            'nome_feira': self.get_index_of_array(row, 11),
            'registro': self.get_index_of_array(row, 12),
            'logradouro': self.get_index_of_array(row, 13),
            'numero': self.get_index_of_array(row, 14),
            'bairro': self.get_index_of_array(row, 15),
            'referencia': self.get_index_of_array(row, 16)
          }
          register_code = self.get_index_of_array(row, 12)
          street_marketing = self.repository.find_by({'registro': register_code})
          if street_marketing:
            self._logger.info(f"update {register_code}")
            update_model = UpdateStreetMarketingSchema(**data).dict(exclude_none=True)
            UpdateStreetMarketing(register_code, update_model).execute()
          else:
            self._logger.info(f"create {register_code}")
            create_model = StreetMarketing(**data)
            CreateStreetMarketing(create_model).execute()
    self._logger.info('end process')

  def get_index_of_array(self, array, index):
    try:
      return array[index]
    except:
      return ''

