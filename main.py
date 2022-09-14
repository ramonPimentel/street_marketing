from app.exceptions.aplication_exception import ApplicationException
from app.models.street_marketing_model import StreetMarketing
from app.use_cases.create_street_marketing import CreateStreetMarketing
from app.use_cases.search_street_marketing import SearchStreetMarketing
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from app.repositories.street_market_repository import StreetMarketRepository
from bson import json_util, ObjectId
import json
from fastapi import FastAPI, Query
from typing import Optional, Union

app = FastAPI()


@app.get("/street_marketing")
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

@app.get("/street_marketing/{id}", response_model=StreetMarketing)
async def show(id: str):
  repository = StreetMarketRepository()
  result = repository.find()
  
  return json.loads(json_util.dumps(result))

@app.post("/street_marketing")
async def create(street_marketing: StreetMarketing):
  try:
    CreateStreetMarketing(street_marketing).execute()
  except ApplicationException as err:
    return JSONResponse(status_code=422, content={"message": f"{err}"})

@app.put("/street_marketing/{id}", response_model=StreetMarketing)
async def index(id: str, street_marketing: StreetMarketing):
  print(id)
  print(street_marketing.dict())
  return {}
