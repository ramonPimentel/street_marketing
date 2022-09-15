from app.exceptions.aplication_exception import ApplicationException
from app.models.street_marketing_model import StreetMarketing
from app.repositories.street_market_repository import StreetMarketRepository
from app.schemas.update_street_marketing_schema import UpdateStreetMarketingSchema
from app.use_cases.create_street_marketing import CreateStreetMarketing
from app.use_cases.update_sreet_marketing import UpdateStreetMarketing
import pytest
from tests.fixtures.utils import create_street_marketing, delete_all_street_marketing
class TestUpdateStreetMarketing:

  def test_when_street_marketing_is_valid(self):
    delete_all_street_marketing()
    street_marketing_create = create_street_marketing()
    repository = StreetMarketRepository()

    street_marketing_update = UpdateStreetMarketingSchema(**{
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
      'logradouro': None,
      'numero': 'S/N',
      'bairro': 'VL FORMOSA',
      'referencia': 'TV RUA PRETORIA'
    })


    data = street_marketing_update.dict(exclude_none=True)
    UpdateStreetMarketing(street_marketing_create.registro, data).execute()

    result = repository.find_by({'registro': street_marketing_create.registro})
    assert result.numero == data['numero']
    assert result.logradouro == 'RUA MARAGOJIPE'

  def test_when_street_marketing_not_exists(self):
    delete_all_street_marketing()

    data = UpdateStreetMarketingSchema(**{'logradouro': 'teste'}).dict(exclude_none=True)

    with pytest.raises(ApplicationException):
      UpdateStreetMarketing('4041-0', data).execute()