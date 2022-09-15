from pydantic import BaseSettings
import os

class Settings(BaseSettings):
  
  @property
  def database_url(self):
    return os.getenv("DATABASE_DB", None)

settings = Settings()