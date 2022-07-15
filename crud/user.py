from models import User, UserFavoriteInspirer, UserFavoriteTheme
from crud.generic import Crud
from sqlalchemy import delete, insert, select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload


class UserFavoriteInspirerOrm(Crud):
    model = UserFavoriteInspirer


class UserFavoriteThemeOrm(Crud):
    model = UserFavoriteTheme


class UserOrm(Crud):
    model = User

    def __init__(self: "UserOrm", session: AsyncSession):
        self.session = session

    async def get_by_id(self, id):
        stmt = (
            select(self.model)
            .options(
                selectinload(self.model.user_inspirer),
                selectinload(self.model.user_themes),
            )
            .where(self.model.id == id)
        )
        result = await self.session.execute(stmt)
        user = result.one_or_none()
        if user:
            u = user[self.model]
            await self.session.refresh(u)
            return u
        return None

    async def get_by_email(self, email: str):

        stmt = select(self.model).where(self.model.email == email)
        result = await self.session.execute(stmt)
        user = result.one_or_none()
        if user:
            return user[self.model]
        return None

    async def create_user(self, data):
        stmt = insert(self.model).values(data)

        result = await self.session.execute(stmt)

        stmt = select(self.model).where(
            self.model.password == data["password"], self.model.email == data["email"]
        )
        result = await self.session.execute(stmt)
        return result.one()[self.model]

    async def get_by_email_and_password(self, email, password):
        stmt = select(self.model).where(
            self.model.email == email, self.model.password == password
        )
        result = await self.session.execute(stmt)
        user = result.one_or_none()
        if user:
            return user[self.model]
        return None

    async def add_favorite(self, user_id, favorite_id):
        stmt = insert(UserFavoriteInspirer).values(
            {"user_id": user_id, "inspirer_id": favorite_id}
        )
        await self.session.execute(stmt)

    async def remove_favorite(self, user_id, favorite_id):
        stmt = delete(UserFavoriteInspirer).where(
            UserFavoriteInspirer.inspirer_id == favorite_id,
            UserFavoriteInspirer.user_id == user_id,
        )
        await self.session.execute(stmt)

    async def add_theme(self, user_id, theme_id):
        stmt = insert(UserFavoriteTheme).values(
            {"user_id": user_id, "theme_id": theme_id}
        )
        await self.session.execute(stmt)

    async def filter(self, /, **kwargs):
        conds = [getattr(self.model, k) == v for k, v in kwargs.items()]
        stmt = (
            select(self.model)
            .options(
                selectinload(self.model.user_inspirer),
                selectinload(self.model.user_themes),
            )
            .where(*conds)
        )
        result = await self.session.execute(stmt)
        return [r[self.model] for r in result.all()]

    async def remove_theme(self, user_id, theme_id):
        stmt = delete(UserFavoriteTheme).where(
            UserFavoriteTheme.theme_id == theme_id,
            UserFavoriteTheme.user_id == user_id,
        )
        await self.session.execute(stmt)
