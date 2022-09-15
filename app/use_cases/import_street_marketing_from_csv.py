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
          print(row[8])
          try:
            data = {
              'long': row[1],
              'lat': row[2],
              'setcens': row[3],
              'areap': row[4],
              'cod_dist': row[5],
              'distrito': row[6],
              'cod_subpref': row[7],
              'subpref': row[8],
              'regiao5': row[9],
              'regiao8': row[10],
              'nome_feira': row[11],
              'registro': row[12],
              'logradouro': row[13],
              'numero': row[14],
              'bairro': row[15] or '',
              'referencia': row[16] or ''
            }
            model = StreetMarketing(**data)
            StreetMarketRepository().add(model)
          except:
            pass
