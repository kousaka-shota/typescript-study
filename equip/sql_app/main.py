from fastapi import FastAPI,Depends
from .router import equipment,measured_value,sensor
from typing import List
from . import schemas,crud,models,database
from sqlalchemy.orm import Session

app = FastAPI()

app.include_router(equipment.router)
app.include_router(measured_value.router)
app.include_router(sensor.router)

@app.get("/")
def sendMessage():
    return {"message":"welcome!"}