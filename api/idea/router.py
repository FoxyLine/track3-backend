from typing import List
from fastapi import APIRouter, Body, Depends, Request
from fastapi.responses import JSONResponse, Response
from .schemas import IdeaRequestSchema, IdeaResponseSchema, CommentRequestSchema

from crud.idea import IdeaOrm, IdeaCommentOrm


router = APIRouter(prefix="/idea")


@router.get("/{idea_id}", response_model=IdeaResponseSchema)
async def get_idea(request: Request, idea_id: int):
    result = await IdeaOrm(request.state.db_session).get_by_id(idea_id)
    return result


@router.post("", response_model=IdeaResponseSchema)
async def create_idea(request: Request, data: IdeaRequestSchema = Body(...)):
    result = await IdeaOrm(request.state.db_session).create(
        {**data.dict(), "user_id": request.user.id}
    )
    return result


@router.put("/{idea_id}", response_model=IdeaResponseSchema)
async def update_idea(
    request: Request, idea_id: int, data: IdeaRequestSchema = Body(...)
):
    result = await IdeaOrm(request.state.db_session).update(idea_id, data.dict())
    return result


@router.delete("/{idea_id}", response_model=IdeaResponseSchema)
async def delete_idea(request: Request, idea_id: int):
    await IdeaOrm(request.state.db_session).delete(idea_id)
    return Response(status_code=201)


@router.get("", response_model=List[IdeaResponseSchema])
async def get_idea(request: Request):
    return await IdeaOrm(request.state.db_session).get_by_user_id(request.user.id)

@router.post("/{idea_id}/comment", response_model=IdeaResponseSchema)
async def update_idea(
    request: Request, idea_id: int, data: CommentRequestSchema = Body(...)
):
    await IdeaCommentOrm(request.state.db_session).create({**data.dict(), "author_id": request.user.id, "idea_id": idea_id})
    result = await IdeaOrm(request.state.db_session).get_by_id(idea_id)
    return result
