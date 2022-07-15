from pydantic import BaseModel


from datetime import date, datetime
from pydantic import BaseModel


class TaskRequestSchema(BaseModel):
    name: str
    deadline: datetime
    status: str

    class Config:
        orm_mode = True


class TaskResponseSchema(BaseModel):
    name: str
    deadline: datetime
    status: str
    user_id: int
    aim_id: int
    id: int

    class Config:
        orm_mode = True
