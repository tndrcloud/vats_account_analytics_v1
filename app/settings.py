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

    APP_HOST: str = "0.0.0.0"
    APP_PORT: int = 8088

    JWT_SECRET: str = env("JWT_SECRET")
    RESET_VERIF_SECRET: str = env("RESET_VERIF_SECRET")
    ACCESS_TOKEN_EXPIRE: int = 3600

    REDIS_PORT: str = env("REDIS_PORT")
    REDIS_PASSWORD: str = env("REDIS_PASSWORD")
    REDIS_DATABASE: str = env("REDIS_DATABASE")

    ROOT_LOGIN: str = env("ROOT_LOGIN")
    ROOT_PASSWORD: str = env("ROOT_PASSWORD")

    USER_LOGIN: str = "ambakadabra@rt-dc.ru"
    USER_PASSWORD: str = "7r9Lw3MHiAbgpcqV"

    SAMPLE_DOMAIN_NAME: str = "S001.14.rt.ru"
    SAMPLE_INCOMING_LINE: str = "74957777777"
    SAMPLE_PREFIX: str = "^(74957777777)"
    SAMPLE_INNER_NUMBER: int = 6152
    SAMPLE_GROUP: str = "1.5 ЛТП ВАТС (GMT+3)"
    SAMPLE_IVR_NAME: str = "ЛЦК"
    SAMPLE_IVR_ID: int = 21050
    SAMPLE_FILTER: str = "Cписок фильтрации для входящей линии 74957777777"


settings = Settings()
