from pydantic import BaseModel, Field, root_validator
from .fields import ObjectIdStr
from typing import Optional

class StreetMarketing(BaseModel):
  id: Optional[ObjectIdStr] = Field(alias="_id")
  long: Optional[int] = Field(...)
  lat: Optional[int] = Field(...)
  setcens: Optional[int] = Field(...)
  areap: Optional[int] = Field(...)
  cod_dist: Optional[int] = Field(...)
  distrito: Optional[str] = Field(...)
  cod_subpref: Optional[int] = Field(...)
  subpref: Optional[str] = Field(...)
  regiao5: Optional[str] = Field(...)
  regiao8: Optional[str] = Field(...)
  nome_feira: Optional[str] = Field(...)
  registro: Optional[str] = Field(...)
  logradouro: Optional[str] = Field(...)
  numero: Optional[str] = Field(...)
  bairro: Optional[str] = Field(...)
  referencia: Optional[str] = Field(...)

  @root_validator(pre=True)
  def remove_empty(cls, values):
    fields = list(values.keys())
    for field in fields:
        value = values[field]
    return values
