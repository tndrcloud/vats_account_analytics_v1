from sqlalchemy import insert, select
from models.models import role
from tests.conftest import async_session_maker


async def test_add_role():
    async with async_session_maker() as session:
        statement = insert(role).values(id=1, name="admin", permissions=None)
        await session.execute(statement)
        await session.commit()

        query = select(role)
        result = await session.execute(query)
        assert result.all() == [(1, "admin", None)], "role not added"
