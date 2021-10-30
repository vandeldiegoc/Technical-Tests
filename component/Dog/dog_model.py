from datetime import datetime
from sqlalchemy.sql.schema import PrimaryKeyConstraint
from sqlalchemy.sql.sqltypes import String
from db.base_class import Base
from datetime import datetime
from sqlalchemy import Column, Integer, String, Boolean, DateTime


class Dog(Base):
    id = Column(Integer(), primary_key=True)
    name = Column(String(), nullable=False, unique=True)
    picture = Column(String(), nullable=False, unique=True)
    is_adopted = Column(Boolean, default=False)
    create_date = Column(DateTime, default=datetime.utcnow())


