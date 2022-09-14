from app.exceptions.aplication_exception import ApplicationException
from app.models.street_marketing_model import StreetMarketing
from app.use_cases.create_street_marketing import CreateStreetMarketing
from app.use_cases.delete_street_marketing import DeleteStreetMarketing
from app.use_cases.find_street_marketing import FindStreetMarketing
from app.use_cases.search_street_marketing import SearchStreetMarketing
from app.use_cases.update_sreet_marketing import UpdateStreetMarketing
from fastapi.encoders import jsonable_encoder
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from app.repositories.street_market_repository import StreetMarketRepository
from bson import json_util, ObjectId
import json
from fastapi import FastAPI, Query
from typing import Optional, Union
from pydantic import BaseModel, Field, root_validator
from typing import List, Union
from fastapi import APIRouter

api = APIRouter(
  tags=["street_marketing"],
)

@api.get("/street_marketing", tags=['street_marketing'])
async def index(
  district: Optional[str] = None,
  region5: Optional[str] = None,
  name: Optional[str] = None,
  neighborhood: Optional[str] = None,
  next_page: Optional[str] = None,
  prev_page: Optional[str] = None,
):
  result = SearchStreetMarketing(
    district=district,
    region5=region5,
    name=name,
    neighborhood=neighborhood,
    next_page=next_page,
    prev_page=prev_page
  ).execute()

  result_json = {
    'response': json.loads(json_util.dumps(result.response)),
    'prev_page': result.prev_page,
    'next_page': result.next_page,
    'batch_size': result.batch_size
  }

  return result_json

@api.get("/street_marketing/{registro}", response_model=StreetMarketing, tags=['feiras'])
async def show(registro: str):
  try:
    street_marketing = FindStreetMarketing(registro).execute()
    return street_marketing.dict(exclude={'_id', 'id'})
  except ApplicationException as err:
    return JSONResponse(status_code=err.app_error_code, content={"message": f"{err.description}"})

@api.post("/street_marketing", response_model=StreetMarketing)
async def create(street_marketing: StreetMarketing):
  try:
    result = CreateStreetMarketing(street_marketing).execute()
    return result.dict(exclude={'_id', 'id'})
  except ApplicationException as err:
    return JSONResponse(status_code=err.app_error_code, content={"message": f"{err.description}"})

class Item(BaseModel):
  codigo: Union[str, None] = None
  nome_feira: Union[str, None] = None

@api.put("/street_marketing/{registro}", response_model=StreetMarketing)
async def update(registro: str, item: StreetMarketing, tags=['street_marketing']):
  try:
    result = UpdateStreetMarketing(register_code=registro, data=item.dict(exclude_none=True)).execute()
    return result.dict(exclude={'_id', 'id'})
  except ApplicationException as err:
    return JSONResponse(status_code=err.app_error_code, content={"message": f"{err.description}"})

@api.delete("/street_marketing/{registro}", tags=['street_marketing'])
async def delete(registro: str):
  try:
    DeleteStreetMarketing(registro).execute()
    return JSONResponse(status_code=200, content={"message": "Street Marketing deleted"})
  except ApplicationException as err:
    return JSONResponse(status_code=err.app_error_code, content={"message": f"{err.description}"})