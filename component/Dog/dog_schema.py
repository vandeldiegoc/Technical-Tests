from datetime import datetime
from pydantic import BaseModel, StrictStr
from typing import Optional


class DogCreate(BaseModel):
    name: StrictStr
    picture: str
    is_adopted: bool = False
    create_date: datetime = datetime.utcnow()


class DogResponse(BaseModel):
    id: int
    name: str
    picture: str
    is_adopted: bool
    datetime: str 

class DogUpdate(BaseModel):
    name: Optional[str]
    is_adopted: Optional[bool]