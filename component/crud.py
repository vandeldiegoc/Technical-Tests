from component.Dog.dog_schema import DogResponse, DogCreate
from component.Dog.dog_crud import crudDog
from component.Dog.dog_model import Dog


class CRUD(crudDog[Dog, DogCreate, DogResponse]):
    ...


crud = CRUD(Dog)