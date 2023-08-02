from envparse import Env
from pydantic_settings import BaseSettings


env = Env()
env.read_envfile('.env')


class Settings(BaseSettings):
    API_V1: str = "/api/v1"
    API_AUTH: str = "/api/auth"
    DB_DRIVER: str = "postgresql+asyncpg"

    DB_HOST: str = env("DB_HOST")
    DB_PORT: int = env("DB_PORT")
    DB_PORT_TEST: int = env("DB_PORT_TEST")
    DB_NAME: str = env("DB_NAME")
    DB_NAME_TEST: str = env("DB_NAME_TEST")
    DB_USER: str = env("DB_USER")
    DB_PASSWORD: str = env("DB_PASSWORD")

    DATABASE_URL: str = f"{DB_DRIVER}://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    DATABASE_URL_TEST: str = f"{DB_DRIVER}://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT_TEST}/{DB_NAME_TEST}"

    APP_HOST: str = env("APP_HOST")
    APP_PORT: int = env("APP_PORT")

    JWT_SECRET: str = env("JWT_SECRET")
    RESET_VERIF_SECRET: str = env("RESET_VERIF_SECRET")
    ACCESS_TOKEN_EXPIRE: int = env("ACCESS_TOKEN_EXPIRE")

    REDIS_PORT: str = env("REDIS_PORT")

    ROOT_LOGIN: str = env("USER_LOGIN")
    ROOT_PASSWORD: str = env("USER_PASSWORD")
    USER_LOGIN: str = env("USER_LOGIN")
    USER_PASSWORD: str = env("USER_PASSWORD")
    DOMAIN_NAME: str = env("DOMAIN_NAME")

    SAMPLE_INCOMING_LINE: str = env("INCOMING_LINE")
    SAMPLE_PREFIX: str = env("PREFIX")
    SAMPLE_FILTER_LIST: str = env("FILTER_LIST")
    SAMPLE_INNER_NUMBER: int = env("INNER_NUMBER")
    SAMPLE_GROUPS_LIST: str = env("GROUPS_LIST")
    SAMPLE_IVR_NAME: str = env("IVR_NAME")
    SAMPLE_IVR_ID: int = env("IVR_ID")


settings = Settings()
