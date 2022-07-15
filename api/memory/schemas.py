from typing import List
from pydantic import BaseModel


from datetime import date, datetime
from pydantic import BaseModel


class MemoryRequestSchema(BaseModel):
    name: str

    class Config:
        orm_mode = True


class PinRequestSchema(BaseModel):
    name: str
    image: str
    x: float
    y: float

    class Config:
        orm_mode = True


class PinResponseSchema(BaseModel):
    id: int
    name: str
    image: str
    x: float
    y: float

    class Config:
        orm_mode = True


class MemoryResponseSchema(BaseModel):
    name: str
    pins: List[PinResponseSchema]
    user_id: int
    aim_id: int
    id: int

    class Config:
        orm_mode = True
