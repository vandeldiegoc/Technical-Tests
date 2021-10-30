from component.Dog.dog_schema import dogUpdate, DogCreate
from component.Dog.dog_crud import crudDog
from component.Dog.dog_model import Dog


class CRUD(crudDog[Dog, DogCreate, dogUpdate]):
    ...


crud = CRUD(Dog)