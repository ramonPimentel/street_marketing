from repositories.street_market_repository import StreetMarketRepository
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
  repository = StreetMarketRepository()
  repository.add({'teste': 'Ramon'})
  result = repository.find()
  return result