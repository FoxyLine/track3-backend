from sqlalchemy import delete, insert, update, select
from sqlalchemy.ext.asyncio import AsyncSession


class Crud:
    model: None

    def __init__(self, session: AsyncSession):
        self.session = session

    async def create(self, data):
        stmt = insert(self.model).values(data)
        result = await self.session.execute(stmt)
        return await self.get_by_id(result.inserted_primary_key.id)

    async def delete(self, id):
        stmt = delete(self.model).where(self.model.id == id)
        await self.session.execute(stmt)

    async def get_by_user_id(self, user_id):
        stmt = select(self.model).where(self.model.user_id == user_id)
        result = await self.session.execute(stmt)
        return [r[self.model] for r in result.all()]

    async def update(self, id, data):
        stmt = update(self.model).where(self.model.id == id).values(**data)
        await self.session.execute(stmt)
        return await self.get_by_id(id)

    async def get_by_id(self, id):
        stmt = select(self.model).where(self.model.id == id)
        result = await self.session.execute(stmt)
        user = result.one_or_none()
        if user:
            return user[self.model]
        return None

    async def filter(self, /, **kwargs):
        conds = [getattr(self.model, k) == v  for k,v in kwargs.items()]
        stmt = select(self.model).where(*conds)
        result = await self.session.execute(stmt)
        return [r[self.model] for r in result.all()]

    async def get_by_ids(self, ids):
        stmt = select(self.model).where(self.model.id.in_(ids))
        result = await self.session.execute(stmt)
        return [r[self.model] for r in result.all()]
