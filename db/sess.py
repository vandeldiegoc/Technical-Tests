from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from ..core.config import Settings
 
from base_class import Base

engine = create_engine(Settings.db_URI)


Base.metadata.create_all(bind=engine)

SessionLocal = sessionmaker(autocommit=False,
                            autoflush=False,
                            bind=engine)