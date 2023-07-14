from fastapi import APIRouter,Depends
from .. import crud,schemas,database
from typing import List
from sqlalchemy.orm import Session

router = APIRouter()

# def get_db():
#     db=database.SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()

@router.get("/equipments/",response_model=List[schemas.Equipment])
async def get_equipments():#db:Session=Depends(get_db)):
    return [schemas.Equipment(equip_id=1,equip_name="a",equip_asset_No="1111")]

# @router.post("/equipments/",response_model=schemas.Equipment)
# async def create_equipment(equipment:schemas.CreateEquipment,db:Session=Depends(get_db)):
#     return crud.add_equipment(db=db,equipment=equipment)