from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from fastapi.params import Depends
from fastapi.responses import JSONResponse
from pydantic.networks import EmailStr
from sqlalchemy.orm import Session
from db.deps import get_dep
from component.Dog.dog_schema import DogCreate, DogUpdate
from component.User.user_schema import (UserCreate,
                                        UserResponse,
                                        Token, UserUpdate,
                                        ListUserResponse)
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import (OAuth2PasswordBearer,
                              OAuth2PasswordRequestForm)
from services.req_api import req_picture
from core.auth import (check_username_password,
                       decode_auth, hash_password)
from fastapi import HTTPException, UploadFile, File
from core.auth import create_access_token, decode_auth
from component.User.user_crud import USER
from component.Dog.dog_crud import DOG


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

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/token",)


@app.post('/dog/{name}', status_code=200)
async def add_dog(
    name: str, db: Session=Depends(get_dep),
    token=Depends(oauth2_scheme)
):
    if name.isdigit():
        raise HTTPException(status_code=405,
                            detail='invali parameter')
    user = decode_auth(token)
    user = jsonable_encoder(USER.get_user_by_email(db, user))
    picture = req_picture()
    new_dog = DogCreate(name=name, picture=picture, id_user=user["id"])
    new_dog = jsonable_encoder(new_dog)
    if picture is None:
        raise HTTPException(status_code=503,
                            detail='503 Service unavailable')
    dogpost = DOG.create(db, new_dog)
    return JSONResponse("Done")


@app.get('/api/dogs', status_code=200)
def get_all_dog(
    db: Session = Depends(get_dep)
):
    dogs = DOG.get_all(db)
    return jsonable_encoder(dogs)


@app.get("/api/dogs/is_adopted", status_code=200)
def get_all_dog_adopted(
    db: Session = Depends(get_dep)
):
    dogs = DOG.getDogsAdopted(db)
    return dogs


@app.get('/api/dog/{name}', status_code=200)
def get_dog(
    name: str, db: Session = Depends(get_dep)
):
    dog = DOG.get(db, name)
    dog = jsonable_encoder(dog)
    return dog


@app.put('/api/dogs/{name}', status_code=200)
def update_dog(
    name: str, data: DogUpdate, db: Session = Depends(get_dep)
):
    if name.isdigit():
        raise HTTPException(status_code=405,
                            detail='invali parameter')
    dog = DOG.update(db, name, data=data)
    return JSONResponse({"Done": "Done"})


@app.delete("/api/dogs/{name}", status_code=200)
def delete_dog(
    name: str, db: Session = Depends(get_dep)
):
    DOG.delete(db, name)
    return JSONResponse({"Done": "Done"})


@app.post("/api/user/")
def create_user(
    data: UserCreate, db: Session = Depends(get_dep)
):
    data.password = hash_password(data.password)
    user = USER.create(db, jsonable_encoder(data))
    return JSONResponse("Done")


@app.get('/api/users', status_code=200, response_model=ListUserResponse)
def get_all_user(
    db: Session = Depends(get_dep)
):
    users = USER.get_all(db)
    users = jsonable_encoder(users)
    return users


@app.get('/api/user/{name}', status_code=200, response_model=UserResponse)
def get_user(
    name: str, db: Session = Depends(get_dep)
):
    user = USER.get(db, name)
    user = jsonable_encoder(user)
    return user


@app.get('/api/user/email/{email}', status_code=200,
         response_model=UserResponse)
def get_user_by_email(
    email: EmailStr, db: Session = Depends(get_dep)
):
    user = USER.get_user_by_email(db, email)
    user = jsonable_encoder(user)
    return user


@app.post("/token", status_code=200, response_model=Token)
async def route_login_access_token(
    db: Session=Depends(get_dep),
    form_data: OAuth2PasswordRequestForm=Depends()
):
    db_user = \
        USER.get_user_by_email(db=db,
                               email=jsonable_encoder(form_data.username))
    if db_user is None:
        raise HTTPException(status_code=400, detail="Username not existed")
    valic = check_username_password(form_data.password, db_user.password)
    if valic is False:
        raise HTTPException(
                status_code=401,
                detail="Could not validate token credentials.",
                headers={"WWW-Authenticate": "Bearer"},
            )
    access_token = create_access_token(
        data={"sub": db_user.email},
    )
    return {"access_token": access_token, "token_type": "bearer"}


@app.delete("/api/user/{name}", status_code=200)
def delete_user(
    name: str, db: Session = Depends(get_dep)
):
    USER.delete(db, name)
    return JSONResponse({"Done": "Done"})


@app.put('/api/User/{name}', status_code=200)
def update_user(
    name: str, data: UserUpdate, db: Session = Depends(get_dep)
):
    if name.isdigit():
        raise HTTPException(status_code=405,
                            detail='invali parameter')
    dog = USER.update(db, name, data=data)
    return JSONResponse({"Done": "Done"})


@app.post("/uploadfile/")
async def post_file(file: UploadFile=File(...)):
    file = file.read()
    return JSONResponse({"Done": "Done"})

if __name__ == "__main__":
    import uvicorn

    uvicorn.run("app:app", host="0.0.0.0",
                port=8001, reload=True,
                log_level="debug")
