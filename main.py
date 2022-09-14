
from fastapi import FastAPI

from app.routes.street_marketing_router import api as street_marketing_api

app = FastAPI()
app.include_router(street_marketing_api)
