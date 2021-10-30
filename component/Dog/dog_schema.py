from datetime import datetime
from pydantic import BaseModel


class DogCreate(BaseModel):
    id: int
    name: str
    picture: str
    is_adopted: bool = False
    create_date: datetime


class dogUpdate(BaseModel):
    name: str
    picture: str
    is_adopted: bool
    datetime: str 