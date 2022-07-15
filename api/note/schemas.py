from pydantic import BaseModel


from datetime import date, datetime
from pydantic import BaseModel


class NoteRequestSchema(BaseModel):
    name: str

    class Config:
        orm_mode = True


class NoteResponseSchema(BaseModel):
    name: str
    user_id: int
    id: int

    class Config:
        orm_mode = True
