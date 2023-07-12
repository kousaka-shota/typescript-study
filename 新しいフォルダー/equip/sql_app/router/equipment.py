from fastapi import APIRouter

router = APIRouter()

@router.get("/equipment/")
async def get_equipments():
    return {"equipments":"aaa"}