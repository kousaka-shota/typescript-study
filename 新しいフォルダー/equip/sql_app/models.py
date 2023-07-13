from .database import Base
from sqlalchemy import Column,String,DateTime,Integer,Float,ForeignKey
from datetime import datetime

class Equipment(Base):
    __tablename__ = "equipments"
    equip_id=Column(Integer,primary_key=True,autoincrement=True,index=True)
    equip_name=Column(String)
    equip_asset_No=Column(String(8),unique=True)
    equip_create_date=Column(DateTime,nullable=False,default=datetime.now)

class Sensor(Base):
    __tablename__ = "sensors"
    equip_id=Column(Integer,ForeignKey("equipments.equip_id"),primary_key=True)
    sensor_id=Column(Integer,primary_key=True)
    sensor_name=Column(String)

class MeasuredData(Base):
    __tablename__  = "Measured_Data"
    timestamp = Column(DateTime,default=datetime.now,primary_key=True)
    equip_id = Column(Integer,ForeignKey("equipments.equip_id"))
    sensor_id = Column(Integer,ForeignKey("sensors.sensor_id"),primary_key=True)
    measured_value = Column(Float)

