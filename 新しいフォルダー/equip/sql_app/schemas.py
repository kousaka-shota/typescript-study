from pydantic import BaseModel,Field
from datetime import datetime

class Equipment(BaseModel):
    equip_id:int
    equip_name:str
    equip_asset_No:str
    equip_create_date:datetime.datetime

    class Config:
        orm_mode = True

class Sensor(BaseModel):
    equip_id:int
    sensor_id:int
    sensor_name:str

    class Config:
        orm_mode = True
    
class MeasuredData(BaseModel):
    timestamp:datetime.dateTime
    equip_id:int
    sensor_id:int
    measured_value:float

    class Config:
        orm_mode = True