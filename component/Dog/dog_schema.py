from datetime import datetime
from pydantic import BaseModel


class DogCreate(BaseModel):
    name: str
    picture: str
    is_adopted: bool = False
    create_date: datetime


class DogResponse(BaseModel):
    id: int
    name: str
    picture: str
    is_adopted: bool
    datetime: str 