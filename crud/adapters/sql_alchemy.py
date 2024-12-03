from typing import Generic, Type, Optional, Any

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from crud.types import Entity, ID
from crud.base import BaseDatabase


class DatabaseAdapter(Generic[Entity, ID], BaseDatabase[Entity, ID]):

    def __init__(self, session: AsyncSession, entity: Type[Entity]):
        self.session = session
        self.entity = entity

    async def get(self, id: ID) -> Optional[Entity]:
        stmt = select(self.entity).where(self.entity.id == id)
        results = await self.session.execute(stmt)
        return results.unique().scalar_one_or_none()

    async def create(self, create_dict: dict[str, Any]) -> Entity:
        entity = self.entity(**create_dict)
        self.session.add(entity)
        await self.session.commit()
        await self.session.refresh(entity)
        return entity

    async def update(self, entity: Entity, update_dict: dict[str, Any]) -> Entity:
        for key, value in update_dict.items():
            setattr(entity, key, value)
        self.session.add(entity)
        await self.session.commit()
        await self.session.refresh(entity)
        return entity

    async def delete(self, entity: Entity) -> None:
        await self.session.delete(entity)
        await self.session.commit()
