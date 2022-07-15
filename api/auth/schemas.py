from typing import List
from pydantic import BaseModel, Field
from pydantic.typing import Literal
from models.user.constants import DREAMER, INSPIRER
from api.theme.schemas import ThemeResponseSchema

UserRoles = Literal[DREAMER, INSPIRER]


class UserRequestSchema(BaseModel):
    username: str
    email: str
    password: str
    role: UserRoles = Field(default=DREAMER)

    class Config:
        orm_mode = True


class InspirerResponseSchema(BaseModel):
    username: str
    email: str
    role: UserRoles

    class Config:
        orm_mode = True


class UserResponseSchema(BaseModel):
    username: str
    email: str
    role: UserRoles

    class Config:
        orm_mode = True


class UserLoginResponseSchema(BaseModel):
    token: str
    user: UserResponseSchema


class UserLoginRequestSchema(BaseModel):
    email: str
    password: str
