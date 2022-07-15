from pydantic import BaseModel


from datetime import date, datetime
from pydantic import BaseModel


class ThemeRequestSchema(BaseModel):
    name: str

    class Config:
        orm_mode = True


class ThemeResponseSchema(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True
