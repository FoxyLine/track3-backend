from crud.user import UserOrm


class UserAlreadyEmailExists(Exception):
    ...


async def apply(db_session, user_data):
    user = await UserOrm(db_session).get_by_email(user_data.email)

    if user:
        raise UserAlreadyEmailExists

    user = await UserOrm(db_session).create_user(user_data.dict())

    return user
