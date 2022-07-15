from typing import List
from pydantic import BaseModel, Field
from pydantic.typing import Literal
from models.user.constants import DREAMER, INSPIRER
from api.theme.schemas import ThemeResponseSchema

UserRoles = Literal[DREAMER, INSPIRER]


class InspirerResponseSchema(BaseModel):
    username: str
    email: str
    role: UserRoles
    id: int

    class Config:
        orm_mode = True


class UserResponseSchema(BaseModel):
    id: int
    username: str
    email: str
    role: UserRoles
    themes: List[ThemeResponseSchema] = Field(alias="user_themes")
    liked_inspirer: List[InspirerResponseSchema] = Field(alias="user_inspirer")

    class Config:
        orm_mode = True
