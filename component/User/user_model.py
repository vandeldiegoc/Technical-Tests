
from db.base_class import Base
from datetime import datetime
from sqlalchemy import Column, Integer, String

from sqlalchemy.orm import relationship

class User(Base):
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(), nullable=False, unique=True)
    name = Column(String(), nullable=False)
    last_name = Column(String(), nullable=False)
    password = Column(String(), nullable=False, unique=True)

     # ORM relationship between User and Dog entity
    dogs = relationship('Dog', back_populates='user')