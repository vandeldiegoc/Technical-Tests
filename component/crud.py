from component.Dog.dog_schema import DogUpdate, DogCreate
from component.Dog.dog_crud import crudDog
from component.Dog.dog_model import Dog


class CRUD(crudDog[Dog, DogCreate, DogUpdate]):
    ...


crud = CRUD(Dog)