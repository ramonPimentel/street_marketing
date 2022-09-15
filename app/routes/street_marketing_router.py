from app.exceptions.aplication_exception import ApplicationException
from app.models.street_marketing_model import StreetMarketing
from app.schemas.update_street_marketing_schema import UpdateStreetMarketingSchema
from app.use_cases.create_street_marketing import CreateStreetMarketing
from app.use_cases.delete_street_marketing import DeleteStreetMarketing
from app.use_cases.find_street_marketing import FindStreetMarketing
from app.use_cases.search_street_marketing import SearchStreetMarketing
from app.use_cases.update_sreet_marketing import UpdateStreetMarketing
from fastapi import FastAPI
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from fastapi import FastAPI
from bson import json_util
import json

from typing import Optional, Union
from pydantic import BaseModel, Field
from typing import List, Union


api = APIRouter(
  tags=["feira livres"],
)

@api.get("/feira_livres")
async def index(
  distrito: Optional[str] = None,
  regiao5: Optional[str] = None,
  nome_feira: Optional[str] = None,
  bairro: Optional[str] = None,
  pagina_proxima: Optional[str] = None,
  pagina_anterior: Optional[str] = None
):
  result = SearchStreetMarketing(
    district=distrito,
    region5=regiao5,
    name=nome_feira,
    neighborhood=bairro,
    next_page=pagina_proxima,
    prev_page=pagina_anterior
  ).execute()

  result_json = {
    'items': json.loads(json_util.dumps(result.response)),
    'pagina_anterior': result.prev_page,
    'pagina_proxima': result.next_page
  }

  return result_json

@api.get("/feira_livres/{registro}", response_model=StreetMarketing)
async def show(registro: str):
  try:
    street_marketing = FindStreetMarketing(registro).execute()
    return street_marketing.dict(exclude={'_id', 'id'})
  except ApplicationException as err:
    return JSONResponse(status_code=err.app_error_code, content={"message": f"{err.description}"})

@api.post("/feira_livres", response_model=StreetMarketing)
async def create(street_marketing: StreetMarketing):
  try:
    result = CreateStreetMarketing(street_marketing).execute()
    return result.dict(exclude={'_id', 'id'})
  except ApplicationException as err:
    return JSONResponse(status_code=err.app_error_code, content={"message": f"{err.description}"})

class Item(BaseModel):
  codigo: Union[str, None] = None
  nome_feira: Union[str, None] = None

@api.put("/feira_livres/{registro}", response_model=StreetMarketing)
async def update(registro: str, item: UpdateStreetMarketingSchema):
  try:
    result = UpdateStreetMarketing(register_code=registro, data=item.dict(exclude_none=True)).execute()
    return JSONResponse(status_code=200, content=result.dict(exclude={'_id', 'id'}))
  except ApplicationException as err:
    return JSONResponse(status_code=err.app_error_code, content={"message": f"{err.description}"})

@api.delete("/feira_livres/{registro}")
async def delete(registro: str):
  try:
    DeleteStreetMarketing(registro).execute()
    return JSONResponse(status_code=200, content={"message": "Street Marketing deleted"})
  except ApplicationException as err:
    return JSONResponse(status_code=err.app_error_code, content={"message": f"{err.description}"})