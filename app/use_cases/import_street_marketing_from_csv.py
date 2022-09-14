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
            'subpref': row[9]
            'regiao5': row[10],
            'regiao8': row[11],
            'nome_feira': row[12],
            'registro': row[13],
            'logradouro': row[14],
            'bairro': row[15],
            'referencia': row[16]
          })
          StreetMarketRepository().add(model)
          print(model.dict())
