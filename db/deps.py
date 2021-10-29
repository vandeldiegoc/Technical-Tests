from os import close
from typing import Generator

from sqlalchemy.orm import session
from sess import SessionLocal


def get_dep() -> Generator:
    """conect and desconect databases conection session """
    try:
        db = session()
        yield db
    finally:
        db.close()
