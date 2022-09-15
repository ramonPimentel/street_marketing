from pydantic import BaseModel, Field, root_validator
from app.models.fields import ObjectIdStr
from typing import Optional

class UpdateStreetMarketingSchema(BaseModel):
  long: Optional[int] = Field(None)
  lat: Optional[int] = Field(None)
  setcens: Optional[int] = Field(None)
  areap: Optional[int] = Field(None)
  cod_dist: Optional[int] = Field(None)
  distrito: Optional[str] = Field(None)
  cod_subpref: Optional[int] = Field(None)
  subpref: Optional[str] = Field(None)
  regiao5: Optional[str] = Field(None)
  regiao8: Optional[str] = Field(None)
  nome_feira: Optional[str] = Field(None)
  logradouro: Optional[str] = Field(None)
  bairro: Optional[str] = Field(None)
  numero: Optional[str] = Field(None)
  referencia: Optional[str] = Field(None)

  @root_validator(pre=True)
  def remove_empty(cls, values):
    fields = list(values.keys())
    for field in fields:
        value = values[field]
        if isinstance(value, dict) or isinstance(value, list):
            if not values[field]:
                values.pop(field)
    return values
