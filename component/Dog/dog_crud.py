
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.exc import IntegrityError
from fastapi import HTTPException
from component.Dog.dog_model import Dog

from db.base_class import Base
from typing import TypeVar, Type, Generic
from pydantic import BaseModel
from db.sess import SessionLocal as session

modelType = TypeVar("modelType", bound=Base)
createSchemaType = TypeVar("createSchemaType", bound=BaseModel)
updateSchemaType = TypeVar("updateSchemaType", bound=BaseModel)


class crudDog(Generic[modelType, createSchemaType, updateSchemaType]):
    def __init__(self, model: Type[modelType]):
        self.model = model
    
    def create(self, db:session, obj_in: createSchemaType):
        db_obj = self.model(**obj_in)
        try:
            db.add(db_obj)
            db.commit()
            return(db_obj)
        except IntegrityError as e:
            db.rollback()
            raise HTTPException(status_code=405, 
                                detail='invali parameter or duplicate key value')

    def getDog(self, db:session, name: str):
        try:
            dog = db.query(self.model).filter(self.model.name == name).one()

        except NoResultFound:
            raise HTTPException(status_code=406,
                                detail="no record was found in the databases")
        return dog
    
        




    

