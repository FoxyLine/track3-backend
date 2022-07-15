from sqlalchemy import select
from models.theme import Theme

from crud.generic import Crud


class ThemeOrm(Crud):
    model = Theme

    async def all(self):
        stmt = select(self.model)
        result = await self.session.execute(stmt)
        return [r[self.model] for r in result.all()]
    
