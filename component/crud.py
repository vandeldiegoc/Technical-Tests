from component.Dog.dog_schema import DogUpdate, DogCreate
from component.Dog.dog_crud import crudDog
from component.Dog.dog_model import Dog
from component.User.user_schema import UserCreate, UserUpdate
from component.User.user_crud import crudUser
from component.User.user_model import User


class CRUD(crudDog[Dog, DogCreate, DogUpdate], 
           crudUser[User, UserCreate, UserUpdate]):
    ...


crud = CRUD(User)