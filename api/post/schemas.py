from typing import List
from pydantic import BaseModel

from api.auth.schemas import UserResponseSchema
from datetime import date, datetime
from pydantic import BaseModel
from api.theme.schemas import ThemeResponseSchema


class PostRequestSchema(BaseModel):
    name: str
    body: str

    themes: List[int]

    class Config:
        orm_mode = True


class PostResponseSchema(BaseModel):
    id: int
    name: str
    body: str
    themes: List[ThemeResponseSchema]
    author: UserResponseSchema

    class Config:
        orm_mode = True
