import uvicorn
from settings import settings
from fastapi import FastAPI, Request, status, Depends
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import ResponseValidationError
from fastapi.responses import JSONResponse
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
