import asyncio
import pytest
from httpx import AsyncClient
from typing import AsyncGenerator
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.pool import NullPool
from sqlalchemy.orm import sessionmaker
from database.session import get_async_session
from models.models import metadata
from settings import settings
from main import app


engine_test = create_async_engine(settings.DATABASE_URL_TEST, poolclass=NullPool)
async_session_maker = sessionmaker(engine_test, class_=AsyncSession, expire_on_commit=False)


metadata.bind = engine_test


async def override_get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_maker() as session:
        yield session


app.dependency_overrides[get_async_session] = override_get_async_session


@pytest.fixture(autouse=True, scope="session")
async def prepare_test_database():
    async with engine_test.begin() as connection:
        await connection.run_sync(metadata.create_all)
    yield
    async with engine_test.begin() as connection:
        await connection.run_sync(metadata.drop_all)


@pytest.fixture(scope="session")
async def event_loop(request) -> AsyncGenerator[AsyncClient, None]:
    async with AsyncClient(app=app, base_url="http://test") as event_loop:
        yield event_loop
        