from sqlalchemy import select
from models.post import Post, PostTheme
from models.theme import Theme

from crud.generic import Crud
from crud.theme import ThemeOrm


class PostOrm(Crud):
    model = Post

    async def create(self, data):
        themes = data.pop("themes")

        model = self.model(**data)
        model.themes = await ThemeOrm(self.session).get_by_ids(themes)
        self.session.add(model)
        await self.session.flush()
        
        return model
