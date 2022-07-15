from typing import List
from fastapi import APIRouter, Body, Depends, Request
from fastapi.responses import JSONResponse, Response

from crud.aim import AimOrm
from .schemas import (
    MemoryRequestSchema,
    MemoryResponseSchema,
    PinRequestSchema,
    PinResponseSchema,
)

from crud.memory import MemoryOrm, MemoryPinOrm


router = APIRouter(prefix="/memory")


@router.get("", response_model=List[MemoryResponseSchema])
async def get_user_memories(request: Request):
    result = await MemoryOrm(request.state.db_session).filter(user_id=request.user.id)
    return result


@router.get("/{memory_id}", response_model=MemoryResponseSchema)
async def get_user_memories(request: Request, memory_id: int):
    result = await MemoryOrm(request.state.db_session).get_by_id(memory_id)
    return result


@router.get("/{aim_id}/aim", response_model=MemoryResponseSchema)
async def get_aim_memory(
    request: Request, aim_id: int, data: MemoryRequestSchema = Body(...)
):
    aim = await AimOrm(request.state.db_session).get_by_id(aim_id)
    if aim is None:
        return JSONResponse(content="Данной цели не сущствует", status_code=400)

    memory = await MemoryOrm(request.state.db_session).filter(
        user_id=request.user.id, aim_id=aim_id
    )

    if not memory:
        return JSONResponse(content="Воспоминание еще не создано", status_code=400)
    return memory[0]


@router.post("/{aim_id}/aim", response_model=MemoryResponseSchema)
async def create_memory(
    request: Request, aim_id: int, data: MemoryRequestSchema = Body(...)
):
    aim = await AimOrm(request.state.db_session).get_by_id(aim_id)
    if aim is None:
        return JSONResponse(content="Данной цели не сущствует", status_code=400)

    memory = await MemoryOrm(request.state.db_session).filter(
        user_id=request.user.id, aim_id=aim_id
    )

    if memory:
        return JSONResponse(
            content="Воспоминание для это цели уже существует", status_code=400
        )

    result = await MemoryOrm(request.state.db_session).create(
        {**data.dict(), "user_id": request.user.id, "aim_id": aim_id}
    )
    return result


@router.post("/{memory_id}/pin", response_model=MemoryResponseSchema)
async def create_memory_pin(
    request: Request, memory_id: int, data: PinRequestSchema = Body(...)
):
    memory = await MemoryOrm(request.state.db_session).get_by_id(memory_id)
    if memory is None:
        return JSONResponse(
            content="Данного воспоминания  не сущствует", status_code=400
        )

    await MemoryPinOrm(request.state.db_session).create(
        {**data.dict(), "memory_id": memory_id}
    )

    memory = await MemoryOrm(request.state.db_session).get_by_id(memory_id)
    await request.state.db_session.refresh(memory)
    return memory 


@router.put("/{memory_id}/pin/{pin_id}", response_model=PinResponseSchema)
async def create_memory_pin(
    request: Request, memory_id: int, pin_id: int, data: PinRequestSchema = Body(...)
):
    memory = await MemoryOrm(request.state.db_session).get_by_id(memory_id)
    if memory is None:
        return JSONResponse(
            content="Данного воспоминания  не сущствует", status_code=400
        )

    pin = await MemoryPinOrm(request.state.db_session).update(pin_id, data.dict())

    return pin


@router.delete("/{memory_id}/pin/{pin_id}", response_model=PinResponseSchema)
async def create_memory_pin(
    request: Request, memory_id: int, pin_id: int):
    memory = await MemoryOrm(request.state.db_session).get_by_id(memory_id)
    if memory is None:
        return JSONResponse(
            content="Данного воспоминания  не сущствует", status_code=400
        )

    await MemoryPinOrm(request.state.db_session).delete(pin_id)
    return Response(status_code=202)
