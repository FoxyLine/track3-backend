from sqlalchemy.pool import NullPool
from starlette.middleware.base import BaseHTTPMiddleware
from config import ASYNC_DATABASE_URL
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.orm import sessionmaker


from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

engine = create_async_engine(
    ASYNC_DATABASE_URL,
    poolclass=NullPool,
    # echo=True,
)

async_session = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)


class DBSessionMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        async with async_session() as session:
            async with session.begin():
                request.state.db_session = session
                return await call_next(request)
