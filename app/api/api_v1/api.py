from fastapi import APIRouter

from api.api_v1.endpoints import data 
from api.api_v1.endpoints import analytics
from api.api_v1.endpoints import calls


api_router = APIRouter()


api_router.include_router(
    data.router,
    prefix="/domain",
    tags=["Domain"],
    )


api_router.include_router(
    calls.router,
    prefix="/calls",
    tags=["Calls"],
    )


api_router.include_router(
    analytics.router,
    prefix="/analytics",
    tags=["Analytics"],
    )
