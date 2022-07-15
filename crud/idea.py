from sqlalchemy import select
from models.idea import Idea, IdeaComment

from crud.generic import Crud


class IdeaOrm(Crud):
    model = Idea

class IdeaCommentOrm(Crud):
    model = IdeaComment