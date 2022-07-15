from typing import List
from fastapi import APIRouter, Body, Depends, Request
from fastapi.responses import JSONResponse, Response
from .schemas import DreamRequestSchema, DreamResponseSchema

from crud.dream import DreamOrm

router = APIRouter(prefix="/dream")


@router.get("/{dream_id}", response_model=DreamResponseSchema)
async def get_dream(request: Request, dream_id: int):
    result = await DreamOrm(request.state.db_session).get_by_id(dream_id)
    return result


@router.post("", response_model=DreamResponseSchema)
async def create_dream(request: Request, data: DreamRequestSchema = Body(...)):
    result = await DreamOrm(request.state.db_session).create(
        {**data.dict(), "user_id": request.user.id}
    )
    return result


@router.put("/{dream_id}", response_model=DreamResponseSchema)
async def update_dream(
    request: Request, dream_id: int, data: DreamRequestSchema = Body(...)
):
    result = await DreamOrm(request.state.db_session).update(dream_id, data.dict())
    return result


@router.delete("/{dream_id}", response_model=DreamResponseSchema)
async def delete_dream(request: Request, dream_id: int):
    await DreamOrm(request.state.db_session).delete(dream_id)
    return Response(status_code=201)


@router.get("", response_model=List[DreamResponseSchema])
async def get_dream(request: Request):
    return await DreamOrm(request.state.db_session).get_by_user_id(request.user.id)
