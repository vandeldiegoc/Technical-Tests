from pydantic import BaseModel, EmailStr
from typing import List, Optional


class UserCreate(BaseModel):
    email:EmailStr
    name: str
    last_name: str
    password: str

class UserResponse(BaseModel):
    id: str
    email: EmailStr
    name: str
    last_name: str

class ListUserResponse(BaseModel):
    __root__: List[UserResponse]

class UserUpdate(BaseModel):
    name: Optional[str]
    last_name: Optional[str]

class Token(BaseModel):
    access_token: str
    token_type: str

class Email(BaseModel):
    email: EmailStr