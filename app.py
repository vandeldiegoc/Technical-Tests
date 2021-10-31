from fastapi import FastAPI
from fastapi import responses
from fastapi.encoders import jsonable_encoder
from fastapi.params import Body, Depends
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from sqlalchemy.sql.sqltypes import String
from component.Dog.dog_model import Dog
from db.deps import get_dep
from component.crud import crud
from component.Dog.dog_schema import DogCreate, DogResponse
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post('/dog', status_code=200, response_model=DogResponse)
def add_dog(
    data:DogCreate, db:Session = Depends(get_dep)
    ):
    data = jsonable_encoder(data)
    dogpost = crud.create(db, data)
    return JSONResponse(data)

@app.get('/dog/{name}', status_code=200)
def get_dog(
    name: str, db:Session = Depends(get_dep)
    ):
    dog = crud.getDog(db, name)
    dog = jsonable_encoder(dog)
    return dog




if __name__=="__main__":
    import uvicorn
     
    uvicorn.run(app, host="0.0.0.0", port=8001, log_level="debug")