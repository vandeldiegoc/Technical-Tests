import os
from typing import Dict
from dotenv import load_dotenv
from pydantic import BaseSettings, PostgresDsn, Field, HttpUrl

load_dotenv()

class Settings(BaseSettings):
    db_URI: PostgresDsn = Field(..., env="DATABASE_URL")
    PORT: int = 8000
    URL_API_REQUEST: HttpUrl = "https://dog.ceo/api/breeds/image/random"

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"



Settings = Settings()
