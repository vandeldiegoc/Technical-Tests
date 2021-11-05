from pydantic import BaseModel, EmailStr


class UserCreate(BaseModel):
    email: EmailStr
    name: str
    last_name: str
    password: str

class UserResponse(BaseModel):
    id: str
    email: EmailStr
    name: str
    last_name: str

class UserUpdate(BaseModel):
    name: str
    last_name: str

class Token(BaseModel):
    access_token: str
    token_type: str