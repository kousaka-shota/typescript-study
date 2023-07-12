from fastapi import FastAPI
from .router import equipment

app = FastAPI()

app.include_router(equipment.router)

@app.get("/")
def sendMessage():
    return {"message":"ooo"}