import os
from typing import Dict
from dotenv import load_dotenv
from pydantic import BaseSettings, PostgresDsn, Field

load_dotenv()

class Settings(BaseSettings):
    Postgres: PostgresDsn = Field(..., env="DATABASE_URL")

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

Settings = Settings()

print(Settings.Postgres)