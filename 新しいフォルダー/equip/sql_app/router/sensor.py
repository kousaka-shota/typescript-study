from fastapi import APIRouter

router = APIRouter()

@router.get("/sensor/")
async def get_sensors():
    return {"sensor":"aari"}