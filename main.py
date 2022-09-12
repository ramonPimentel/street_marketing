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

@app.get("/")
async def root():
  repository = StreetMarketRepository()
  result = repository.find()
  
  return json.loads(json_util.dumps(result))


@app.post("/street_marketing")
async def create(street_marketing: StreetMarketing):
  try:
    CreateStreetMarketing(street_marketing).execute()
  except ApplicationException as err:
    return JSONResponse(status_code=422, content={"message": f"{err}"})

@app.get("/street_marketing/")
async def index(q: Optional[str] = None):
  result = SearchStreetMarketing(query=q).execute()
  return json.loads(json_util.dumps(result))
