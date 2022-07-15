from sqlalchemy import select
from models.memory import Memory, Pin

from crud.generic import Crud


class MemoryOrm(Crud):
    model = Memory

class MemoryPinOrm(Crud):
    model = Pin
