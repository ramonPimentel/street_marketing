from app.exceptions.aplication_exception import ApplicationException
from app.models.street_marketing_model import StreetMarketing
from app.repositories.street_market_repository import StreetMarketRepository
from app.use_cases.create_street_marketing import CreateStreetMarketing
from app.use_cases.update_sreet_marketing import UpdateStreetMarketing
import pytest
class TestUpdateStreetMarketing:

  def test_when_street_marketing_is_valid(self):
    repository =  StreetMarketRepository()
    street_marketing = StreetMarketing(**{
      'long': -46550164,
      'lat': -23558733,
      'setcens': 355030885000091,
      'areap': 3550308005040,
      'coddist': 87,
      'distrito': 'VILA FORMOSA',
      'codsubpref': 26,
      'subprefe': 'ARICANDUVA-FORMOSA-CARRAO',
      'regiao5': 'Leste',
      'regiao8': 'Leste 1',
      'nome_feira': 'VILA FORMOSA',
      'registro': '4041-0',
      'logradouro': 'RUA MARAGOJIPE',
      'numero': 'S/N',
      'bairro': 'VL FORMOSA',
      'referencia': 'TV RUA PRETORIA'
    })

    repository.delete_by_register_code(street_marketing.registro)
    CreateStreetMarketing(street_marketing).execute()

    data = StreetMarketing(**{'logradouro': 'teste'}).dict(exclude_none=True)
    UpdateStreetMarketing(street_marketing.registro, data).execute()

    result = repository.find_by({'registro': street_marketing.registro})
    assert result.logradouro == data['logradouro']

  def test_when_street_marketing_not_exists(self):
    repository =  StreetMarketRepository()
    street_marketing = StreetMarketing(**{
      'long': -46550164,
      'lat': -23558733,
      'setcens': 355030885000091,
      'areap': 3550308005040,
      'coddist': 87,
      'distrito': 'VILA FORMOSA',
      'codsubpref': 26,
      'subprefe': 'ARICANDUVA-FORMOSA-CARRAO',
      'regiao5': 'Leste',
      'regiao8': 'Leste 1',
      'nome_feira': 'VILA FORMOSA',
      'registro': '4041-0',
      'logradouro': 'RUA MARAGOJIPE',
      'numero': 'S/N',
      'bairro': 'VL FORMOSA',
      'referencia': 'TV RUA PRETORIA'
    })

    repository.delete_by_register_code(street_marketing.registro)

    data = StreetMarketing(**{'logradouro': 'teste'}).dict(exclude_none=True)
    with pytest.raises(ApplicationException):
      UpdateStreetMarketing(street_marketing.registro, data).execute()