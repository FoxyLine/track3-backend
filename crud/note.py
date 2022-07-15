from sqlalchemy import select
from models.note import Note

from crud.generic import Crud


class NoteOrm(Crud):
    model = Note
