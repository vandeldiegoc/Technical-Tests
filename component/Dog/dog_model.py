from datetime import datetime
from db.base_class import Base
from datetime import datetime
from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.orm import relationship


class Dog(Base):
    id = Column(Integer, primary_key=True)
    name = Column(String(), nullable=False)
    picture = Column(String(), nullable=False, unique=True)
    is_adopted = Column(Boolean, default=False)
    create_date = Column(DateTime, default=datetime.utcnow())


    id_user = Column(Integer, ForeignKey('user.id'))

    # ORM relationship between Dog and User entity
    user = relationship('User', back_populates='dogs')