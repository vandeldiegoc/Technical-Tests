from typing import Dict
from dotenv import load_dotenv
from pydantic import BaseSettings, PostgresDsn, Field, HttpUrl

load_dotenv()

class Settings(BaseSettings):
    db_URI: PostgresDsn = Field(..., env="DATABASE_URL")
    PORT: int = 8000
    URL_API_REQUEST: HttpUrl = "https://dog.ceo/api/breeds/image/random"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    SECRET_KEY: str = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
    ALGORITHM: str = "HS256"
    

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"



Settings = Settings()
