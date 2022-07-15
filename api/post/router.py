from typing import List
from fastapi import APIRouter, Body, Depends, Request
from fastapi.responses import JSONResponse, Response
from starlette.authentication import requires
from models.user.constants import INSPIRER, DREAMER
from .schemas import PostRequestSchema, PostResponseSchema

from crud.post import PostOrm

router = APIRouter(prefix="/post")


@router.get("/{post_id}", response_model=PostResponseSchema)
async def get_post(request: Request, post_id: int):
    result = await PostOrm(request.state.db_session).get_by_id(post_id)
    return result


@router.post("", response_model=PostResponseSchema)
@requires([INSPIRER])
async def create_post(request: Request, data: PostRequestSchema = Body(...)):
    result = await PostOrm(request.state.db_session).create(
        {**data.dict(), "user_id": request.user.id}
    )
    return result


@router.delete("/{post_id}", response_model=PostResponseSchema)
@requires([INSPIRER])
async def delete_post(request: Request, post_id: int):
    await PostOrm(request.state.db_session).delete(post_id)
    return Response(status_code=201)


@router.get("/{user_id}/user", response_model=List[PostResponseSchema])
async def get_post(request: Request, user_id: int):
    return await PostOrm(request.state.db_session).filter(user_id=user_id)
