from typing import List
from fastapi import APIRouter, Body, Depends, Request
from fastapi.responses import JSONResponse, Response
from .schemas import NoteRequestSchema, NoteResponseSchema

from crud.note import NoteOrm

router = APIRouter(prefix="/note")


@router.get("/{note_id}", response_model=NoteResponseSchema)
async def get_note(request: Request, note_id: int):
    result = await NoteOrm(request.state.db_session).get_by_id(note_id)
    return result


@router.post("", response_model=NoteResponseSchema)
async def create_note(request: Request, data: NoteRequestSchema = Body(...)):
    result = await NoteOrm(request.state.db_session).create(
        {**data.dict(), "user_id": request.user.id}
    )
    return result


@router.put("/{note_id}", response_model=NoteResponseSchema)
async def update_note(
    request: Request, note_id: int, data: NoteRequestSchema = Body(...)
):
    result = await NoteOrm(request.state.db_session).update(note_id, data.dict())
    return result


@router.delete("/{note_id}", response_model=NoteResponseSchema)
async def delete_note(request: Request, note_id: int):
    await NoteOrm(request.state.db_session).delete(note_id)
    return Response(status_code=201)


@router.get("", response_model=List[NoteResponseSchema])
async def get_note(request: Request):
    return await NoteOrm(request.state.db_session).get_by_user_id(request.user.id)
