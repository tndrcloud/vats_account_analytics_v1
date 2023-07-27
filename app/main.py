import uvicorn
from typing import List
from settings import settings
from fastapi import FastAPI, Request, status, Depends
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import ResponseValidationError
from fastapi.responses import JSONResponse
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from database.session import get_async_session
from schemas.schemas import User
from models.models import user
from api.api_v1.api import api_router
from auth.manager import auth_router, current_superuser


app = FastAPI(
    title="VATS Analytics",
    version="v1",
    description="REST API сервис для проверки настроек и вызовов ЛК ВАТС"
)


@app.exception_handler(ResponseValidationError)
async def validation_exception_handler(request: Request, exc: ResponseValidationError):
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content=jsonable_encoder({"detail": exc.errors()})
    )


@app.get("/get_users_db", response_model=List[User])
async def get_users_db(username: str, session: AsyncSession = Depends(get_async_session)) -> List[User]:
    query = select(user).where(user.c.username == username)
    result = await session.execute(query)
    return result.all()


app.include_router(
    auth_router,
    prefix=settings.API_AUTH,
    tags=["Authorization"],
)

app.include_router(
    api_router,
    prefix=settings.API_V1,
    dependencies=[Depends(current_superuser)]
)


if __name__ == '__main__':
    uvicorn.run(
        "main:app",
        host=settings.APP_HOST,
        port=settings.APP_PORT
    )
