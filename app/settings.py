from envparse import Env
from pydantic_settings import BaseSettings


env = Env()
env.read_envfile('.env')


class Settings(BaseSettings):
    API_V1: str = "/api/v1"
    API_AUTH: str = "/api/auth"

    DB_HOST: str = env("DB_HOST")
    DB_PORT: int = env("DB_PORT")
    DB_NAME: str = env("DB_NAME")
    DB_USER: str = env("DB_USER")
    DB_PASSWORD: str = env("DB_PASSWORD")

    DATABASE_URL: str = f"postgresql+asyncpg://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

    APP_HOST: str = env("SERVER_HOST")
    APP_PORT: int = env("SERVER_PORT")

    JWT_SECRET: str = env("JWT_SECRET")
    RESET_VERIF_SECRET: str = env("RESET_VERIF_SECRET")


settings = Settings()
