from fastapi import APIRouter,Depends
from .. import crud,schemas,dependencies
from typing import List



router = APIRouter(dependencies=[Depends(dependencies.get_token_header)])

@router.get("/equipments/",response_model=List[schemas.Equipment])
async def get_equipments():
    equipments = crud.get_equipments()
    return equipments