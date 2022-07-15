from fastapi import FastAPI, Depends

from api.auth import auth_router
from api.aim import aim_router
from api.dream import dream_router
from api.idea import idea_router
from api.note import note_router
from api.task import task_router
from api.theme import theme_router
from api.post import post_router
from api.user import user_router
from api.memory import memory_router
from database import DBSessionMiddleware
from middlewares.auth.auth import AuthMiddleware
from middlewares.auth.utils import verify_authorization_header, auth_required

app = FastAPI()

app.add_middleware(
    AuthMiddleware, verify_authorization_header=verify_authorization_header
)
app.add_middleware(DBSessionMiddleware)
app.include_router(auth_router)
app.include_router(
    aim_router, prefix="/api", dependencies=[Depends(auth_required)], tags=["aim"]
)
app.include_router(
    dream_router, prefix="/api", dependencies=[Depends(auth_required)], tags=["dream"]
)
app.include_router(
    idea_router, prefix="/api", dependencies=[Depends(auth_required)], tags=["idea"]
)
app.include_router(
    note_router, prefix="/api", dependencies=[Depends(auth_required)], tags=["note"]
)
app.include_router(
    task_router, prefix="/api", dependencies=[Depends(auth_required)], tags=["task"]
)
app.include_router(
    theme_router, prefix="/api", dependencies=[Depends(auth_required)], tags=["theme"]
)
app.include_router(
    post_router, prefix="/api", dependencies=[Depends(auth_required)], tags=["post"]
)
app.include_router(
    user_router, prefix="/api", dependencies=[Depends(auth_required)], tags=["user"]
)
app.include_router(
    memory_router, prefix="/api", dependencies=[Depends(auth_required)], tags=["memory"]
)


@app.get("/")
async def root():
    return {"message": "Hello World"}
