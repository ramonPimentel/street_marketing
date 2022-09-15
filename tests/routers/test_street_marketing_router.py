from app.exceptions.aplication_exception import ApplicationException
from app.models.street_marketing_model import StreetMarketing
from app.repositories.street_market_repository import StreetMarketRepository
from fastapi import FastAPI
from fastapi.testclient import TestClient
import pytest
from app.routes.street_marketing_router import api as street_marketing_api
from tests.fixtures.utils import create_street_marketing, delete_all_street_marketing

app = FastAPI()
app.include_router(street_marketing_api)
client = TestClient(app)

class TestCreateStreetRouter:
  def test_index(self):
    delete_all_street_marketing()
    create_street_marketing()
    response = client.get("/street_marketing")
    assert response.status_code == 200
    response_json = response.json()
    assert response_json['pagina_anterior'] is None
    assert response_json['pagina_proxima'] is None
    assert len(response_json['items']) == 1
  
  def test_show_when_exists_street_marketing(self):
    delete_all_street_marketing()
    street_marketing = create_street_marketing()

    response = client.get(f"/street_marketing/{street_marketing.registro}")
    assert response.status_code == 200
    response_json = response.json()
    assert response_json['long'] == street_marketing.long
    assert response_json['lat'] == street_marketing.lat
    assert response_json['setcens'] == street_marketing.setcens
    assert response_json['areap'] == street_marketing.areap
    assert response_json['cod_dist'] == street_marketing.cod_dist
    assert response_json['distrito'] == street_marketing.distrito
    assert response_json['cod_subpref'] == street_marketing.cod_subpref
    assert response_json['subpref'] == street_marketing.subpref
    assert response_json['regiao5'] == street_marketing.regiao5
    assert response_json['regiao8'] == street_marketing.regiao8
    assert response_json['registro'] == street_marketing.registro
    assert response_json['logradouro'] == street_marketing.logradouro
    assert response_json['bairro'] == street_marketing.bairro
    assert response_json['referencia'] == street_marketing.referencia
  
  def test_show_when_not_exists_street_marketing(self):
    delete_all_street_marketing()

    response = client.get(f"/street_marketing/4041-0")
    assert response.status_code == 404
  
  def test_show_create_success(self):
    delete_all_street_marketing()
    street_marketing = create_street_marketing()
    data = street_marketing.dict(exclude={'_id', 'id'})
    delete_all_street_marketing()

    response = client.post(f"/street_marketing", json=data)
    response_json = response.json()
    assert response.status_code == 200
    assert response_json['registro'] == data['registro']
  
  def test_create_when_user_existis(self):
    delete_all_street_marketing()
    street_marketing = create_street_marketing()
    data = street_marketing.dict(exclude={'_id', 'id'})

    response = client.post(f"/street_marketing", json=data)
    assert response.status_code == 422
  
  def test_update_success(self):
    delete_all_street_marketing()
    street_marketing = create_street_marketing()

    response = client.put(f"/street_marketing/{street_marketing.registro}", json={'bairro': 'test'})
    response_json = response.json()
    assert response.status_code == 200
    assert response_json['bairro'] == 'test'
  
  def test_put_when_user_not_existis(self):
    delete_all_street_marketing()

    response = client.put(f"/street_marketing/4041-0", json={'regiao5': 'regiao5'})
    assert response.status_code == 404

  def test_delete_success(self):
    delete_all_street_marketing()
    street_marketing = create_street_marketing()

    response = client.delete(f"/street_marketing/{street_marketing.registro}", json={'bairro': 'test'})
    assert response.status_code == 200
  
  def test_delete_when_user_not_existis(self):
    delete_all_street_marketing()

    response = client.delete(f"/street_marketing/4041-0", json={'regiao5': 'regiao5'})
    assert response.status_code == 404