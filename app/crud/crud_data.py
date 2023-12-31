from typing import List
from typing import Any
from typing import Dict
from typing import Union

from sqlalchemy.ext.asyncio import AsyncSession

from crud.crud_base import CRUDBase
from schemas.data import DomainData


class CRUDData(CRUDBase[DomainData]):
    async def create(
        self, session: AsyncSession, *, obj_in: DomainData
        ) -> List[DomainData]:
        ...

    async def get(
        self, session: AsyncSession, *, domain_name: str    
        ) -> List[DomainData]:
        ...

    async def update(
        self, session: AsyncSession, *, 
        db_obj: DomainData, obj_in: Union[DomainData, Dict[str, Any]]
        ) -> List[DomainData]:
        ...

    async def delete(
        self, session: AsyncSession, *, domain_name: str   
        ) -> List[DomainData]:
        ...


data = CRUDData(DomainData)