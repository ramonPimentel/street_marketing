from app.exceptions.aplication_exception import ApplicationException
from app.models.street_marketing_model import StreetMarketing
from app.repositories.street_market_repository import StreetMarketRepository
from app.use_cases.create_street_marketing import CreateStreetMarketing
from app.use_cases.delete_street_marketing import DeleteStreetMarketing
import pytest

class TestDeleteStreetMarketing:
  def test_when_street_marketing_exists(self):
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

    repository.add(street_marketing)
    result = repository.find_by({'registro': street_marketing.registro})
    assert result is not None

    DeleteStreetMarketing(street_marketing.registro).execute()
    result = repository.find_by({'registro': street_marketing.registro})
    assert result is not None
  
  def test_when_street_marketing_not_exists(self):
    repository =  StreetMarketRepository()
    register_code = '4041-0'
    repository.delete_by_register_code(register_code)

    with pytest.raises(ApplicationException):
      assert DeleteStreetMarketing(register_code).execute()