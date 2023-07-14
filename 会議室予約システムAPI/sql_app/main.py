import datetime
from fastapi import FastAPI , Depends
from pydantic import BaseModel, Field
from sqlalchemy.orm import Session
from . import schemas,crud,models
from .database import SessionLocal , engine
from typing import List
import uvicorn

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()


# read
#responseModel 返り値の型定義 
@app.get("/users",response_model=List[schemas.User])
#db:Session 規定値で.databaseで起動しているDBを引数として渡してあげる(Depends(関数)となっているのが気になる)
async def read_users(skip:int=0,limit:int=100,db:Session=Depends(get_db)):
    users = crud.get_users(db,skip=skip,limit=limit)
    return users


@app.get("/rooms",response_model=List[schemas.Room])
async def read_rooms(skip:int=0,limit:int=100,db:Session=Depends(get_db)):
    rooms = crud.get_rooms(db,skip=skip,limit=limit)
    return rooms


@app.get("/bookings",response_model=List[schemas.Booking])
async def read_booking(skip:int=0,limit:int=100,db:Session = Depends(get_db)):
    bookings = crud.get_bookings(db,skip=skip,limit=limit)
    return bookings

@app.get("/room/{name}",response_model=schemas.Room)
async def search_room(db:Session=Depends(get_db),name:str=""):
    room = crud.get_search_room(db,name)
    return room

# create
@app.post("/users",response_model=schemas.User)
async def create_user(user:schemas.UserCreate,db:Session=Depends(get_db)):
    return crud.create_user(db=db,user=user)

@app.post("/rooms",response_model=schemas.Room)
async def create_room(room:schemas.RoomCreate,db:Session=Depends(get_db)):
    return crud.create_room(db=db,room=room)


@app.post("/bookings",response_model=schemas.Booking)
async def booking(booking:schemas.BookingCreate,db:Session=Depends(get_db)):
    return crud.create_booking(booking=booking,db=db)


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)