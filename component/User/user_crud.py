from core.base_crud import crudRecipe
from component.User.user_model import User
from component.User.user_schema import UserCreate, UserUpdate
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.orm import Session
from fastapi import HTTPException


class crudUser(crudRecipe[User, UserCreate, UserUpdate]):
    def get_user_by_email(self, db: Session, email: str):
        try:
            user = db.query(self.model).filter(self.model.email == email).one()
        except NoResultFound:
            raise HTTPException(status_code=406,
                                detail="no record was found in the databases")
        return user
USER = crudUser(User)
