from fastapi_users.password import PasswordHelper
from passlib.context import CryptContext


password_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
password_helper = PasswordHelper(password_context)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return password_helper.verify_and_update(plain_password, hashed_password)


def get_password_hash(password: str) -> str:
    return password_helper.hash(password)
