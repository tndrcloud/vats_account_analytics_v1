from typing import List, Any, Dict, Union
from app.crud.crud_base import CRUDBase
from sqlalchemy.ext.asyncio import AsyncSession
from schemas.data import DomainData


class CRUDData(CRUDBase[DomainData]):
    async def create(
        self, session: AsyncSession, *, obj_in: DomainData
        ) -> List[DomainData]:
        ...

    async def get(
        self, session: AsyncSession    
        ) -> List[DomainData]:
        ...

    async def update(
        self, session: AsyncSession, *, 
        db_obj: DomainData, obj_in: Union[DomainData, Dict[str, Any]]
        ) -> List[DomainData]:
        ...

    async def delete(
        self, session: AsyncSession   
        ) -> None:
        ...


data = CRUDData(DomainData)