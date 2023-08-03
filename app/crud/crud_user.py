from typing import Any, Dict, Optional, Union
from core.security import get_password_hash, verify_password
from crud.base import CRUDBase
from auth.user import User
from fastapi import Depends
from database.session import get_async_session
from sqlalchemy.ext.asyncio import AsyncSession
from app.auth.user_schemas import UserCreate, UserUpdate


class CRUDUser(CRUDBase[User, UserCreate, UserUpdate]):
    async def get_by_email(
            self, session: AsyncSession = Depends(get_async_session), *, email: str
            ) -> Optional[User]:
        return await session.query(User).filter(User.email == email).first()

    async def create(
            self, session: AsyncSession = Depends(get_async_session), *, obj_in: UserCreate
            ) -> User:
        db_obj = User(
            email=obj_in.email,
            hashed_password=get_password_hash(obj_in.password),
            username=obj_in.full_name,
            is_superuser=obj_in.is_superuser,
        )
        await session.add(db_obj)
        await session.commit()
        await session.refresh(db_obj)
        return db_obj

    async def update(
            self, session: AsyncSession = Depends(get_async_session), *, 
            db_obj: User, obj_in: Union[UserUpdate, Dict[str, Any]]
            ) -> User:
        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.dict(exclude_unset=True)
        if update_data["password"]:
            hashed_password = get_password_hash(update_data["password"])
            del update_data["password"]
            update_data["hashed_password"] = hashed_password
        return await super().update(session, db_obj=db_obj, obj_in=update_data)

    async def authenticate(
            self, session: AsyncSession = Depends(get_async_session), *, 
            email: str, password: str
            ) -> Optional[User]:
        user = await self.get_by_email(session, email=email)
        
        if not user:
            return None
        if not verify_password(password, user.hashed_password):
            return None
        return user

    def is_active(self, user: User) -> bool:
        return user.is_active

    def is_superuser(self, user: User) -> bool:
        return user.is_superuser


user = CRUDUser(User)