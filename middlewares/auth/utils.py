from typing import Tuple, List

from fastapi import Request, HTTPException
from fastapi.responses import Response

from crud.user import UserOrm
from .auth import FastAPIUser
from starlette.authentication import BaseUser
from utils.jwt_utils import decode_token


# Takes a string that will look like 'Bearer eyJhbGc...'
async def verify_authorization_header(
    db_session, auth_header: str
) -> Tuple[List[str], BaseUser]:
    user_data = decode_token(auth_header)

    user = await UserOrm(db_session).get_by_id(user_data["user_id"])

    user = FastAPIUser(user)
    if user.instance:
        scopes = [user.instance.role]
    else:
        scopes = []

    return (scopes, user)


async def auth_required(request: Request):
    if not request.user.is_authenticated:
        raise HTTPException(status_code=403)
