from crud.user import UserOrm
from utils.jwt_utils import get_user_token


class UserDoesntExistsException(Exception):
    ...


async def apply(db_session, data):

    user = await UserOrm(db_session).get_by_email_and_password(
        email=data.email, password=data.password
    )

    if user is None:
        raise UserDoesntExistsException

    return user, get_user_token(user)
