from app.repositories.street_market_repository import StreetMarketRepository
from app.schemas.update_street_marketing_schema import UpdateStreetMarketingSchema
from app.use_cases.import_street_marketing_from_csv import ImportStreetMarketingFromCSV
from tests.fixtures.utils import create_street_marketing, delete_all_street_marketing

class TestImportStreetMarketingFromCSV:
  def test_import_all(self):
    delete_all_street_marketing()
    ImportStreetMarketingFromCSV(
      file_path='/src/tests/fixtures/test.csv'
    ).execute()
    repository = StreetMarketRepository()
    result = repository.find_all()
    assert len(result) == 9
  
  def test_import_street_marketing_existis(self):
    delete_all_street_marketing()
    ImportStreetMarketingFromCSV(
      file_path='/src/tests/fixtures/test.csv'
    ).execute()
    repository = StreetMarketRepository()
    street_marketing = repository.find_by({'registro': '4041-0'})
    old_name = street_marketing.nome_feira
    update_model = UpdateStreetMarketingSchema(**{'nome_feira': 'Teste'})
    repository.update(street_marketing.id, update_model.dict(exclude_none=True))
    street_marketing = repository.find_by({'registro': '4041-0'})
    assert street_marketing.nome_feira == 'Teste'
    ImportStreetMarketingFromCSV(
      file_path='/src/tests/fixtures/test.csv'
    ).execute()
    street_marketing = repository.find_by({'registro': '4041-0'})
    assert street_marketing.nome_feira == old_name