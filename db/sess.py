from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from core.config import Settings
from component.Dog.dog_model import Base

engine = create_engine(Settings.db_URI)

Base.metadata.create_all(bind=engine)

SessionLocal = sessionmaker(autocommit=False,
                            autoflush=False,
                            bind=engine)