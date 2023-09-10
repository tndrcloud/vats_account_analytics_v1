from fastapi.encoders import jsonable_encoder

from settings import settings

from crud.crud_user import crud_user
from core.security import verify_password
from schemas.user import UserCreate
from tests.conftest import async_session_maker
from tests.utils.utils import random_email
from tests.utils.utils import random_lower_string


async def test_create_user() -> None:
    async with async_session_maker() as session:
        email = random_email()
        password = random_lower_string()

        user_in = UserCreate(
            username=settings.USER_LOGIN,
            email=email, 
            password=password,
            role_id=1,
            is_active=True,
            is_superuser=False,
            is_verified=False
            )
        
        user = await crud_user.create(session, obj_in=user_in)

        assert user.email == email
        assert hasattr(user, "hashed_password")


async def test_authenticate_user() -> None:
    async with async_session_maker() as session:
        email = random_email()
        password = random_lower_string()

        user_in = UserCreate(
            username=settings.USER_LOGIN,
            email=email, 
            password=password,
            role_id=1,
            is_active=True,
            is_superuser=False,
            is_verified=False
            )
        
        user = await crud_user.create(session, obj_in=user_in)
        auth_user = await crud_user.authenticate(
            session, 
            email=email, 
            password=password
            )
        
        assert auth_user
        assert user.email == auth_user.email


async def test_not_authenticate_user() -> None:
    async with async_session_maker() as session:
        email = random_email()
        password = random_lower_string()

        user = await crud_user.authenticate(
            session, 
            email=email, 
            password=password
            )

        assert user is None


async def test_check_if_user_is_active() -> None:
    async with async_session_maker() as session:
        email = random_email()
        password = random_lower_string()

        user_in = UserCreate(
            username=settings.USER_LOGIN,
            email=email, 
            password=password,
            role_id=1,
            is_active=True,
            is_superuser=False,
            is_verified=False
            )
        
        user = await crud_user.create(session, obj_in=user_in)
        is_active = crud_user.is_active(user)

        assert is_active is True


async def test_check_if_user_is_active_inactive() -> None:
    async with async_session_maker() as session:
        email = random_email()
        password = random_lower_string()

        user_in = UserCreate(
            username=settings.USER_LOGIN,
            email=email, 
            password=password,
            role_id=1,
            is_active=True,
            is_superuser=False,
            is_verified=False
            )
        
        user = await crud_user.create(session, obj_in=user_in)
        is_active = crud_user.is_active(user)

        assert is_active


async def test_check_if_user_is_superuser() -> None:
    async with async_session_maker() as session:
        email = random_email()
        password = random_lower_string()

        user_in = UserCreate(
                username=settings.USER_LOGIN,
                email=email, 
                password=password,
                role_id=1,
                is_active=True,
                is_superuser=True,
                is_verified=False
                )
        
        user = await crud_user.create(session, obj_in=user_in)
        is_superuser = crud_user.is_superuser(user)

        assert is_superuser is True


async def test_check_if_user_is_superuser_normal_user() -> None:
    async with async_session_maker() as session:
        email = random_email()
        password = random_lower_string()

        user_in = UserCreate(
                username=settings.USER_LOGIN,
                email=email, 
                password=password,
                role_id=1,
                is_active=True,
                is_superuser=False,
                is_verified=False
                )
        
        user = await crud_user.create(session, obj_in=user_in)
        is_superuser = crud_user.is_superuser(user)

        assert is_superuser is False


async def test_get_user() -> None:
    async with async_session_maker() as session:
        email = random_email()
        password = random_lower_string()
        
        user_in = UserCreate(
                username=settings.USER_LOGIN,
                email=email, 
                password=password,
                role_id=1,
                is_active=True,
                is_superuser=True,
                is_verified=False
                )
        
        created_user = await crud_user.create(session, obj_in=user_in)
        get_user = await crud_user.get(id=created_user.id, session=session)
        
        assert get_user
        assert created_user.email == get_user.email
        assert jsonable_encoder(created_user) == jsonable_encoder(get_user)


async def test_update_user() -> None:
    async with async_session_maker() as session:
        email = random_email()
        password = random_lower_string()
        new_password = random_lower_string()

        user_in = UserCreate(
                username=settings.USER_LOGIN,
                email=email, 
                password=password,
                role_id=1,
                is_active=True,
                is_superuser=True,
                is_verified=False
                )
        
        user = await crud_user.create(session, obj_in=user_in)
        
        user_in_update = UserCreate(
                username=settings.USER_LOGIN,
                email=email, 
                password=new_password,
                role_id=1,
                is_active=True,
                is_superuser=True,
                is_verified=False
                )
        
        await crud_user.update(session, db_obj=user, obj_in=user_in_update)
        get_user = await crud_user.get(id=user.id, session=session)

        assert get_user
        assert user.email == get_user.email
        assert verify_password(new_password, get_user.hashed_password)


async def test_delete_user() -> None:
    async with async_session_maker() as session:
        email = random_email()
        password = random_lower_string()
        
        user_in = UserCreate(
                username=settings.USER_LOGIN,
                email=email, 
                password=password,
                role_id=1,
                is_active=True,
                is_superuser=True,
                is_verified=False
                )
        
        created_user = await crud_user.create(session, obj_in=user_in)
        delete_user = await crud_user.remove(session=session, id=created_user.id)
        get_user = await crud_user.get(id=created_user.id, session=session)
        
        assert created_user and delete_user
        assert jsonable_encoder(created_user) == jsonable_encoder(delete_user)
        assert get_user is None
        