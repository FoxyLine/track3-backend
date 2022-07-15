from sqlalchemy import select
from models.task import Task

from crud.generic import Crud


class TaskOrm(Crud):
    model = Task

    async def get_tasks_by_aim_and_user(self, user_id, aim_id):
        stmt = select(self.model).where(
            self.model.user_id == user_id, self.model.aim_id == aim_id
        )
        result = await self.session.execute(stmt)
        return [r[self.model] for r in result.all()]
