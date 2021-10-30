from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from fastapi.params import Body, Depends
from sqlalchemy.orm import Session
from db.deps import get_dep
from component.crud import crud
from component.Dog.dog_schema import DogCreate

app = FastAPI()

@app.post('/dog', status_code=200, response_model=DogCreate)
def add_dog(
    data:DogCreate, db:Session = Depends(get_dep)
    ):
    dogpost = crud.create(db, jsonable_encoder(data))
    return dogpost



if __name__=="__main__":
    import uvicorn
     
    uvicorn.run(app, host="0.0.0.0", port=8001, log_level="debug")