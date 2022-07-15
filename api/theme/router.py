from typing import List
from fastapi import APIRouter, Body, Depends, Request
from fastapi.responses import JSONResponse, Response
from api.user.schemas import UserResponseSchema
from .schemas import ThemeRequestSchema, ThemeResponseSchema

from crud.theme import ThemeOrm
from crud.user import UserOrm, UserFavoriteThemeOrm

router = APIRouter(prefix="/theme")


@router.get("/{theme_id}", response_model=ThemeResponseSchema)
async def get_theme(request: Request, theme_id: int):
    result = await ThemeOrm(request.state.db_session).get_by_id(theme_id)
    return result


@router.post("", response_model=ThemeResponseSchema)
async def create_theme(request: Request, data: ThemeRequestSchema = Body(...)):
    result = await ThemeOrm(request.state.db_session).create(data.dict())
    return result


@router.delete("/{theme_id}", response_model=ThemeResponseSchema)
async def delete_theme(request: Request, theme_id: int):
    await ThemeOrm(request.state.db_session).delete(theme_id)
    return Response(status_code=201)


@router.get("", response_model=List[ThemeResponseSchema])
async def get_theme(request: Request):
    return await ThemeOrm(request.state.db_session).all()


@router.post("/{theme_id}/favorite", response_model=UserResponseSchema)
async def add_favorite_theme(request: Request, theme_id: int):
    result = await UserFavoriteThemeOrm(request.state.db_session).filter(
        user_id=request.user.id, theme_id=theme_id
    )
    if result:
        return JSONResponse(content="Данный жанр уже в фаворитах", status_code=400)

    await UserOrm(request.state.db_session).add_theme(request.user.id, theme_id)
    return await UserOrm(request.state.db_session).get_by_id(request.user.id)


@router.delete("/{theme_id}/favorite", response_model=UserResponseSchema)
async def del_favorite_theme(request: Request, theme_id: int):
    await UserOrm(request.state.db_session).remove_theme(request.user.id, theme_id)
    return await UserOrm(request.state.db_session).get_by_id(request.user.id)
