from fastapi import Depends
from typing import Any, Dict, Generic, List, Optional, Type, TypeVar, Union
from fastapi.encoders import jsonable_encoder
from database.session import get_async_session
from sqlalchemy.ext.asyncio import AsyncSession
from pydantic import BaseModel
from database.base_class import Base


ModelType = TypeVar("ModelType", bound=Base)
CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=BaseModel)


class CRUDBase(Generic[ModelType, CreateSchemaType, UpdateSchemaType]):
    def __init__(self, model: Type[ModelType]):
        self.model = model

    async def create(
            self, session: AsyncSession = Depends(get_async_session), *, obj_in: CreateSchemaType
            ) -> ModelType:
        obj_in_data = jsonable_encoder(obj_in)
        db_obj = self.model(**obj_in_data)  

        await session.add(db_obj)
        await session.commit()
        await session.refresh(db_obj)
        return db_obj

    async def get(
            self, id: Any, session: AsyncSession = Depends(get_async_session)
            ) -> Optional[ModelType]:
        return await session.query(self.model).filter(self.model.id == id).first()

    async def update(
            self, session: AsyncSession = Depends(get_async_session), *, 
            db_obj: ModelType, obj_in: Union[UpdateSchemaType, Dict[str, Any]]
            ) -> ModelType:
        obj_data = jsonable_encoder(db_obj)

        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.dict(exclude_unset=True)
        for field in obj_data:
            if field in update_data:
                setattr(db_obj, field, update_data[field])

        await session.add(db_obj)
        await session.commit()
        await session.refresh(db_obj)
        return db_obj

    async def remove(
            self, session: AsyncSession = Depends(get_async_session), *, id: int
            ) -> ModelType:
        obj = session.query(self.model).get(id)
        
        await session.delete(obj)
        await session.commit()
        return obj
    