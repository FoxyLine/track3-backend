from typing import List
from fastapi import APIRouter, Body, Depends, Request
from fastapi.responses import JSONResponse, Response

from crud.aim import AimOrm
from .schemas import TaskRequestSchema, TaskResponseSchema

from crud.task import TaskOrm

router = APIRouter(prefix="/task")


@router.get("/{task_id}", response_model=TaskResponseSchema)
async def create_task(request: Request, task_id: int):
    result = await TaskOrm(request.state.db_session).get_by_id(task_id)
    return result


@router.post("/{aim_id}/aim", response_model=TaskResponseSchema)
async def create_task(
    request: Request, aim_id: int, data: TaskRequestSchema = Body(...)
):
    aim = await AimOrm(request.state.db_session).get_by_id(aim_id)
    if aim is None:
        return JSONResponse(content="Данной цели не сущствует", status_code=400)

    result = await TaskOrm(request.state.db_session).create(
        {**data.dict(), "user_id": request.user.id, "aim_id": aim_id}
    )
    return result


@router.get("/{aim_id}/aim", response_model=List[TaskResponseSchema])
async def get_aim_tasks(request: Request, aim_id: int):
    aim = await AimOrm(request.state.db_session).get_by_id(aim_id)
    if aim is None:
        return JSONResponse(content="Данной цели не сущствует", status_code=400)

    result = await TaskOrm(request.state.db_session).get_tasks_by_aim_and_user(
        user_id=request.user.id, aim_id=aim_id
    )
    return result


@router.put("/{task_id}", response_model=TaskResponseSchema)
async def update_task(
    request: Request, task_id: int, data: TaskRequestSchema = Body(...)
):
    result = await TaskOrm(request.state.db_session).update(task_id, data.dict())
    return result


@router.delete("/{task_id}", response_model=TaskResponseSchema)
async def delete_task(request: Request, task_id: int):
    await TaskOrm(request.state.db_session).delete(task_id)
    return Response(status_code=201)


@router.get("", response_model=List[TaskResponseSchema])
async def get_task(request: Request):
    return await TaskOrm(request.state.db_session).get_by_user_id(request.user.id)
