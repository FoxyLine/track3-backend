from typing import List
from fastapi import APIRouter, Body, Depends, Request
from fastapi.responses import JSONResponse, Response

from .schemas import UserResponseSchema

from crud.user import UserOrm, UserFavoriteInspirerOrm

router = APIRouter(prefix="/user")


@router.get("/ribbon", response_model=UserResponseSchema)
async def get_user(request: Request, user_id: int):
    result = await UserOrm(request.state.db_session).get_by_id(user_id)
    return result


@router.get("", response_model=UserResponseSchema)
async def get_self_info(request: Request):
    return await UserOrm(request.state.db_session).get_by_id(request.user.id)


@router.get("/{role}", response_model=List[UserResponseSchema])
async def get_user_by_roler(request: Request, role: str):
    print(role)
    return await UserOrm(request.state.db_session).filter(role=role)


@router.post("/{inspirer_id}/favorite", response_model=UserResponseSchema)
async def add_favorite_user(request: Request, inspirer_id: int):
    result = await UserFavoriteInspirerOrm(request.state.db_session).filter(
        user_id=request.user.id, inspirer_id=inspirer_id
    )
    if result:
        return JSONResponse(
            content="Данный пользователь уже в фаворитах", status_code=400
        )

    await UserOrm(request.state.db_session).add_favorite(request.user.id, inspirer_id)
    return await UserOrm(request.state.db_session).get_by_id(request.user.id)


@router.delete("/{inspirer_id}/favorite", response_model=UserResponseSchema)
async def del_favorite_user(request: Request, inspirer_id: int):
    await UserOrm(request.state.db_session).remove_favorite(
        request.user.id, inspirer_id
    )
    return await UserOrm(request.state.db_session).get_by_id(request.user.id)
