import datetime
from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI()

@app.get("/")
async def index():
    return {"message": "sss"}


@app.post("/users")
async def users(users: User):
    return {"users": users}


@app.post("/rooms")
async def room(rooms: Room):
    return {"rooms": rooms}


@app.post("/bookings")
async def booking(bookings: Booking):
    return {"bookings": bookings}
