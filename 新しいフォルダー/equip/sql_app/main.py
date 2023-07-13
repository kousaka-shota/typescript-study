from fastapi import FastAPI
from .router import equipment,measured_value,sensor

app = FastAPI()

app.include_router(equipment.router)
app.include_router(measured_value.router)
app.include_router(sensor.router)


@app.get("/")
def sendMessage():
    return {"message":"ooo"}