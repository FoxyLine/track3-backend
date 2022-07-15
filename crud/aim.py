from sqlalchemy import select, delete
from sqlalchemy.orm import selectinload
from models.aim import Aim
from models.task import Task

from crud.generic import Crud


class AimOrm(Crud):
    model = Aim

    async def delete(self, id):
        result = await super().delete(id)
        stmt = delete(Task).where(Task.aim_id == id)
        await self.session.execute(stmt)
        return result

    async def get_by_user_id(self, user_id):
        stmt = (
            select(self.model)
            .options(
                selectinload(self.model.tasks),
            )
            .where(self.model.user_id == user_id)
        )
        result = await self.session.execute(stmt)
        return [r[self.model] for r in result.all()]

    async def get_by_id(self, id):
        stmt = (
            select(self.model)
            .options(
                selectinload(self.model.tasks),
            )
            .where(self.model.id == id)
        )
        result = await self.session.execute(stmt)
        user = result.one_or_none()
        if user:
            return user[self.model]
        return None
