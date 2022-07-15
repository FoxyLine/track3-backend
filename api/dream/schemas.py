from pydantic import BaseModel


from datetime import date, datetime
from pydantic import BaseModel


class DreamRequestSchema(BaseModel):
    name: str

    class Config:
        orm_mode = True


class DreamResponseSchema(BaseModel):
    name: str
    user_id: int
    id: int

    class Config:
        orm_mode = True
