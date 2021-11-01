from os import wait
from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from fastapi.params import Depends
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from db.deps import get_dep
from component.crud import crud
from component.Dog.dog_schema import DogCreate, DogUpdate
from fastapi.middleware.cors import CORSMiddleware
from services.req_api import req_picture
from fastapi import HTTPException
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


@app.post('/dog/{name}', status_code=200)
async def add_dog(
    name:str, db:Session = Depends(get_dep)
    ):
    if name.isdigit():
        raise HTTPException(status_code=405, 
                            detail='invali parameter')
    picture = req_picture()
    a = DogCreate(name=name, picture = picture)
    a = jsonable_encoder(a)

    if picture is None:
        raise HTTPException(status_code=503, 
                                detail='503 Service unavailable')

    print("dasdasd")

    print(a)
    print("dasdasd")
    dogpost = crud.create(db, a)
    return JSONResponse("Done")

@app.get('/api/dogs', status_code=200)
def get_all_dog(
    db:Session = Depends(get_dep)
    ):
    dogs = crud.getDogs(db)
    return jsonable_encoder(dogs)

@app.get('/api/dog/{name}', status_code=200)
def get_dog(
    name: str, db:Session = Depends(get_dep)
    ):
    dog = crud.getDog(db, name)
    dog = jsonable_encoder(dog)
    return dog

@app.put('/api/dogs/{name}', status_code=200) 
def update_dog(
    name: str, data:DogUpdate, db:Session = Depends(get_dep)
    ):
    if name.isdigit():
        raise HTTPException(status_code=405, 
                            detail='invali parameter')
    
    dog = crud.updateDog(db, name, data=data)

    return JSONResponse({"Done": "Done"})

    





if __name__=="__main__":
    import uvicorn
     
    uvicorn.run(app, host="0.0.0.0", port=8001, log_level="debug")