from pydantic import BaseSettings
import os

class Settings(BaseSettings):
  
  @property
  def database_url(self):
    return os.getenv("DATABASE_DB", None)
  
  @property
  def environment(self):
    return os.getenv("ENVIRONMENT", "development")

settings = Settings()