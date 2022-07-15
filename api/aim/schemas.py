from datetime import date, datetime
from typing import Dict, List, Optional
from pydantic import BaseModel, validator, root_validator
from api.task.schemas import TaskResponseSchema


class AimRequestSchema(BaseModel):
    name: str
    deadline: datetime

    class Config:
        orm_mode = True


class AimResponseSchema(BaseModel):
    name: str
    deadline: datetime
    user_id: int
    tasks: List[TaskResponseSchema]
    memory_id: Optional[int]
    id: int
    is_done: Optional[bool]

    @validator("is_done", pre=False, always=True)
    def valid_is_done(cls, v, values, **kwargs) -> bool:
        if len(values["tasks"]) == 0:
            return False

        for task in values["tasks"]:
            if task.status != "Done":
                return False
        return True

    class Config:
        orm_mode = True
