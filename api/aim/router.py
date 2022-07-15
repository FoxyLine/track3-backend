from typing import List
from fastapi import APIRouter, Body, Depends, Request
from fastapi.responses import JSONResponse, Response
from api.aim.schemas import AimRequestSchema, AimResponseSchema

from crud.aim import AimOrm

router = APIRouter(prefix="/aim")


@router.post("", response_model=AimResponseSchema)
async def create_aim(request: Request, data: AimRequestSchema = Body(...)):
    result = await AimOrm(request.state.db_session).create(
        {**data.dict(), "user_id": request.user.id}
    )
    return result


@router.put("/{aim_id}", response_model=AimResponseSchema)
async def update_aim(request: Request, aim_id: int, data: AimRequestSchema = Body(...)):
    await AimOrm(request.state.db_session).update(aim_id, data.dict())
    return await AimOrm(request.state.db_session).get_by_user_id(request.user.id)


@router.delete("/{aim_id}", response_model=AimResponseSchema)
async def delete_aim(request: Request, aim_id: int):
    await AimOrm(request.state.db_session).delete(aim_id)
    return Response(status_code=201)


@router.get("", response_model=List[AimResponseSchema])
async def get_aim(request: Request):
    return await AimOrm(request.state.db_session).get_by_user_id(request.user.id)
