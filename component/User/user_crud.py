
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.exc import IntegrityError
from fastapi import HTTPException
from db.base_class import Base
from typing import TypeVar, Type, Generic
from pydantic import BaseModel
from db.sess import SessionLocal as session

modelType = TypeVar("modelType", bound=Base)
createSchemaType = TypeVar("createSchemaType", bound=BaseModel)
updateSchemaType = TypeVar("updateSchemaType", bound=BaseModel)


class crudUser(Generic[modelType, createSchemaType, updateSchemaType]):
    def __init__(self, model: Type[modelType]):
        self.model = model
    
    def create_user(self, db:session, obj_in: createSchemaType):
        db_obj = self.model(**obj_in)
        try:
            db.add(db_obj)
            db.commit()
            return(db_obj)
        except IntegrityError:
            db.rollback()
            raise HTTPException(status_code=405, 
                                detail='invali parameter or duplicate key value')

    def get_user(self, db:session, email:str):       
        try:
            user = db.query(self.model).filter(self.model.email == email).one()
        except NoResultFound:
            raise HTTPException(status_code=406,
                                detail="no record was found in the databases")
        return user
