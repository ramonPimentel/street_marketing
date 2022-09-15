from app.repositories.street_market_repository import StreetMarketRepository
from app.models.street_marketing_model import StreetMarketing

def delete_all_street_marketing():
  repository = StreetMarketRepository()
  repository.delete_all()

def create_street_marketing():
  repository = StreetMarketRepository()
  repository.delete_all()

  street_marketing = StreetMarketing(**{
    'long': -46550164,
    'lat': -23558733,
    'setcens': 355030885000091,
    'areap': 3550308005040,
    'cod_dist': 87,
    'distrito': 'VILA FORMOSA',
    'cod_subpref': 26,
    'subpref': 'ARICANDUVA-FORMOSA-CARRAO',
    'regiao5': 'Leste',
    'regiao8': 'Leste 1',
    'nome_feira': 'VILA FORMOSA',
    'registro': '4041-0',
    'logradouro': 'RUA MARAGOJIPE',
    'numero': 'S/N',
    'bairro': 'VL FORMOSA',
    'referencia': 'TV RUA PRETORIA'
  })

  return repository.add(street_marketing)

