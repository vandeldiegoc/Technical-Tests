from os import close
from typing import Generator
from db.sess import SessionLocal


def get_dep() -> Generator:
    """conect and desconect databases conection session """
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()
