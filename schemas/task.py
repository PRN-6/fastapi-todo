from typing import Optional
from pydantic import BaseModel, Field

class TaskBase(BaseModel):
    title: str = Field(...,min_length=1,max_length=100,example="buy milk")
    description: Optional[str] = Field(None,max_length=1000)
    completed: bool = False


class TaskCreate(TaskBase):
    pass

class TaskUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    completed: Optional[bool] = None

class TaskResponse(TaskBase):
    id: int

    class Config:
        from_attributes = True

    