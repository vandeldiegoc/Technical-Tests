from bcrypt import hashpw, gensalt, checkpw
from jwt import PyJWTError, encode
from datetime import datetime, timedelta
from core.config import Settings



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
        expire = datetime.utcnow() + timedelta(minutes=Settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = encode(to_encode,
                         Settings.SECRET_KEY,
                         algorithm=Settings.ALGORITHM)
    return encoded_jwt

