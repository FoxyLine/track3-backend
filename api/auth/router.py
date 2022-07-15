from fastapi import APIRouter, Body, Depends, Request
from fastapi.responses import JSONResponse
from use_cases.user.register import apply as register_user, UserAlreadyEmailExists
from use_cases.user.login import apply as login_user, UserDoesntExistsException


from .schemas import UserLoginRequestSchema, UserRequestSchema, UserResponseSchema, UserLoginResponseSchema

router = APIRouter(prefix="/auth")


@router.post("/register", response_model=UserResponseSchema)
async def register(request: Request, user_data: UserRequestSchema = Body(...)):
    request.user
    try:
        user = await register_user(request.state.db_session, user_data=user_data)
    except UserAlreadyEmailExists:
        return JSONResponse(
            content="Пользователь с таким email уже существует", status_code=400
        )

    return user


@router.post("/login", response_model=UserLoginResponseSchema)
async def login(request: Request, user_data: UserLoginRequestSchema = Body(...)):
    try:
        user, token = await login_user(request.state.db_session, user_data)
        return {"user": user, "token": token}
    except UserDoesntExistsException:
        return JSONResponse(content="Пароль или email не верный")
