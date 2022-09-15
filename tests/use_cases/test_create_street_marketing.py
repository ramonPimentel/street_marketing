from app.exceptions.aplication_exception import ApplicationException
from app.models.street_marketing_model import StreetMarketing
from app.repositories.street_market_repository import StreetMarketRepository
from app.use_cases.create_street_marketing import CreateStreetMarketing
import pytest
from tests.fixtures.utils import delete_all_street_marketing
class TestCreateStreetMarketing:

  def test_when_street_marketing_is_valid(self):
    delete_all_street_marketing()
    repository =  StreetMarketRepository()
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

    repository.delete_by_register_code(street_marketing.registro)
    CreateStreetMarketing(street_marketing).execute()
    result = repository.find_by({'registro': street_marketing.registro})
    assert result is not None
    assert result.registro == street_marketing.registro

  def test_when_street_marketing_exists(self):
    delete_all_street_marketing()
    repository =  StreetMarketRepository()
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

    repository.delete_by_register_code(street_marketing.registro)
    CreateStreetMarketing(street_marketing).execute()

    with pytest.raises(ApplicationException):
      assert CreateStreetMarketing(street_marketing).execute()