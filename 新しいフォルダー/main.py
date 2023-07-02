from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel


class Item(BaseModel):
    name:str
    description:Optional[str]=None
    price:int
    tax:Optional[float]=None

app = FastAPI()

@app.post("/item/")
async def createItem(item:Item):
    return {"message":f"{item.name}ha koredesu"}