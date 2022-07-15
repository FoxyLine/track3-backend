from typing import List
from pydantic import BaseModel

from api.auth.schemas import UserResponseSchema
from datetime import date, datetime
from pydantic import BaseModel


class CommentResponseSchema(BaseModel):
    author: UserResponseSchema
    body: str
    id: int

    class Config:
        orm_mode = True


class IdeaRequestSchema(BaseModel):
    name: str

    class Config:
        orm_mode = True


class IdeaResponseSchema(BaseModel):
    name: str
    user: UserResponseSchema
    comments: List[CommentResponseSchema]
    id: int

    class Config:
        orm_mode = True


class CommentRequestSchema(BaseModel):
    body: str
