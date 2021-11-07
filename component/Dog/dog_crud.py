from component.User.user_model import User
from core.base_crud import crudRecipe
from component.Dog.dog_model import Dog
from component.Dog.dog_schema import DogCreate, DogUpdate
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.orm import Session
from fastapi import HTTPException


class crudDog(crudRecipe[Dog, DogCreate, DogUpdate]):
    def getDogsAdopted(self, db: Session):
        dogs = db.query(self.model).filter(self.model.is_adopted == True).all()
        return dogs

DOG = crudDog(Dog)
