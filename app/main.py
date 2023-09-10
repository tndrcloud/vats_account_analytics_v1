import uvicorn

from fastapi import FastAPI
from fastapi import Request
from fastapi import status
from fastapi import Depends

from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import ResponseValidationError
from fastapi.responses import JSONResponse

from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend

from redis import asyncio as async_redis

from settings import settings
from api.api_v1.api import api_router
from database.utils import init_db

from auth.manager import auth_router
from auth.manager import register_router
from auth.manager import current_superuser


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


@app.on_event("startup")
async def startup():
    init_db()
    redis = async_redis.from_url(
        f"redis://{settings.REDIS_HOST}:{settings.REDIS_PORT}", 
        encoding="utf8", 
        decode_responses=True)
    
    FastAPICache.init(RedisBackend(redis), prefix="fastapi-cache")


app.include_router(
    auth_router,
    prefix=settings.API_AUTH,
    tags=["Authorization"],
)

app.include_router(
    register_router,
    prefix=settings.API_AUTH,
    tags=["Authorization"],
)

app.include_router(
    api_router,
    prefix=settings.API_V1,
    dependencies=[Depends(current_superuser)]
)


if __name__ == "__main__":
    uvicorn.run(
        app=settings.APP_NAME, 
        host=settings.APP_HOST, 
        port=settings.APP_PORT,
        workers=settings.WORKERS
        )