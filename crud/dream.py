from sqlalchemy import select
from models.dream import Dream

from crud.generic import Crud


class DreamOrm(Crud):
    model = Dream
