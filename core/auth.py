from bcrypt import hashpw, gensalt, checkpw
from jwt import PyJWTError, encode, decode
from datetime import datetime, timedelta
from core.config import Settings
from fastapi import HTTPException
from pydantic import ValidationError


def hash_password(password):
    hashed_password = hashpw(password.encode('utf-8'), gensalt())
    return hashed_password


def check_username_password(passwor, password):
    password = checkpw(passwor.encode('utf-8'), password.encode('utf-8'))
    return password


def create_access_token(*, data: dict, expires_delta: timedelta = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = \
            datetime.utcnow() + timedelta(minutes=Settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = encode(to_encode,
                         Settings.SECRET_KEY,
                         algorithm=Settings.ALGORITHM)
    return encoded_jwt


def decode_auth(
    token: str
):
    credentials_exception = HTTPException(
        status_code=403, detail="Could not validate credentials"
    )
    try:
        payload = decode(token, Settings.SECRET_KEY,
                         algorithms=[Settings.ALGORITHM])
        username: str = payload.get('sub')
        if username is None:
            raise credentials_exception
        return username
    except (PyJWTError, ValidationError):
        raise credentials_exception
