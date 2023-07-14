from pydantic import BaseModel,Field
import datetime

class EquipmentBase(BaseModel):
    equip_name:str
    equip_asset_No:str

class EquipmentCreate(EquipmentBase):
    pass

class Equipment(EquipmentBase):
    equip_id:int
    equip_create_date:datetime.datetime=Field(default=datetime.datetime.now)

    class Config:
        orm_mode = True

class Sensor(BaseModel):
    equip_id:int
    sensor_id:int
    sensor_name:str

    class Config:
        orm_mode = True
    
class MeasuredData(BaseModel):
    timestamp:datetime.datetime
    equip_id:int
    sensor_id:int
    measured_value:float

    class Config:
        orm_mode = True