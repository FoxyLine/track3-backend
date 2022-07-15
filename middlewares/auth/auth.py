from typing import Tuple

from fastapi import FastAPI
from starlette.authentication import (
    AuthenticationBackend,
    AuthCredentials,
    BaseUser,
)
from starlette.middleware.authentication import AuthenticationMiddleware
from starlette.requests import HTTPConnection


class FastAPIUser(BaseUser):
    def __init__(self, instance=None):
        self.instance = instance
        self.id = instance and instance.id
        self._is_authenticated = bool(instance)

    @property
    def is_authenticated(self) -> bool:
        return self._is_authenticated

    @property
    def identity(self) -> str:
        return self.instance and self.instance.user.id


class FastAPIAuthBackend(AuthenticationBackend):
    def __init__(self, verify_authorization_header: callable):

        self.verify_authorization_header = verify_authorization_header

    async def authenticate(
        self, conn: HTTPConnection
    ) -> Tuple[AuthCredentials, BaseUser]:
        if "Authorization" not in conn.headers:
            scopes = []
            user = FastAPIUser()
        else:
            authorization_header: str = conn.headers["Authorization"]
            scopes, user = await self.verify_authorization_header(
                conn.state.db_session, authorization_header
            )

        return AuthCredentials(scopes=scopes), user


def AuthMiddleware(app: FastAPI, verify_authorization_header: callable):
    return AuthenticationMiddleware(
        app, backend=FastAPIAuthBackend(verify_authorization_header)
    )
