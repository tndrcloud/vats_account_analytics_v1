from fastapi_users.authentication import BearerTransport 
from fastapi_users.authentication import JWTStrategy
from fastapi_users.authentication import AuthenticationBackend

from settings import settings


bearer_transport = BearerTransport(tokenUrl="/api/auth/login")


def get_jwt_strategy() -> JWTStrategy:
    return JWTStrategy(secret=settings.JWT_SECRET, lifetime_seconds=3600)


auth_backend = AuthenticationBackend(
    name="jwt",
    transport=bearer_transport,
    get_strategy=get_jwt_strategy,
)
