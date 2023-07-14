from typing  import Optional
from pydantic import BaseModel,Field

class TaskBase(BaseModel):
    title:Optional[str] =Field(None,example="aaa")


class Task(TaskBase):
    id:int
    done:bool =Field(False,description="ssss")

    class Config:
        orm_mode= True

class TaskCreate(TaskBase):
    pass

class TaskCreateResponse(TaskCreate):
    id:int

    class Config:
        orm_mode:True