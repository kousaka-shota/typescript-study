from fastapi import APIRouter,Depends
from .. import crud,schemas,dependencies,database
from typing import List
from sqlalchemy.orm import Session



router = APIRouter()

def get_db():
    db=detabase.SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/equipments/",response_model=List[schemas.Equipment])
async def get_equipments(db:Session=Depends(get_db)):
    equipments = crud.get_equipments(db)
    return equipments

@router.post("/equipments/")
async def create_equipment(db:Session=Depends(get_db)):
    return crud.add_equipment(db=db,equipment={equip_name:"test1",equip_asset_No:"XXXX"})