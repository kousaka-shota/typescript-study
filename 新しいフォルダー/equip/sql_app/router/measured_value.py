from fastapi import APIRouter

router = APIRouter()

@router.get("/measuredValue/")
async def get_measured_value():
    return {"measured":"value"}