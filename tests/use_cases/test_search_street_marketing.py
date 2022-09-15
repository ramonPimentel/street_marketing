from app.use_cases.search_street_marketing import SearchStreetMarketing
from tests.fixtures.utils import create_street_marketing, delete_all_street_marketing
class TestDeleteStreetMarketing:
  def test_when_not_exists_result(self):
    delete_all_street_marketing()
    # street_marketing = create_street_marketing()

    result = SearchStreetMarketing().execute()
    assert len(result.response) == 0
  
  def test_when_exists_result(self):
    delete_all_street_marketing()
    street_marketing = create_street_marketing()

    result = SearchStreetMarketing(
      name=street_marketing.nome_feira,
      region=street_marketing.regiao5,
      neighborhood=street_marketing.bairro,
      district=street_marketing.distrito
    ).execute()

    assert len(result.response) == 1
