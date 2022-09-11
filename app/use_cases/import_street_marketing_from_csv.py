import csv

from app.models.street_marketing_model import StreetMarketing
from app.repositories.street_market_repository import StreetMarketRepository

class ImportStreetMarketingFromCSV:
  def __init__(self) -> None:
    pass

  def execute(self):
    with open('/src/DEINFO_AB_FEIRASLIVRES_2014.csv', newline='') as csvfile:
      spamreader = csv.reader(csvfile, delimiter=',', quotechar=',')
      for row in spamreader:
        if row[0] != 'ID':
          model = StreetMarketing(**{
            'codigo': row[0],
            'long': row[1],
            'lat': row[2],
            'setcens': row[3],
            'areap': row[4],
            'cod_dist': row[5],
            'distrito': row[6],
            'cod_subpref': row[7],
            'regiao5': row[8],
            'regiao8': row[9],
            'nome_feira': row[10],
            'registro': row[11],
            'logradouro': row[12],
            'bairro': row[13],
            'referencia': row[14]
          })
          StreetMarketRepository().add(model)
          print(model.dict())
