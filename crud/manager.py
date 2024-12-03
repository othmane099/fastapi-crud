from typing import Generic, Any, Dict, Optional

from crud.types import Entity, ID
from crud.base import BaseDatabase


class BaseManager(Generic[Entity, ID]):

    async def get(self, id: ID) -> Optional[Entity]:
        raise NotImplementedError()

    async def save(self, save_dict: Dict[str, Any]) -> Entity:
        raise NotImplementedError()

    async def delete(self, id: ID) -> None:
        raise NotImplementedError()


class BaseManagerImpl(BaseManager[Entity, ID]):

    def __init__(self, db: BaseDatabase[Entity, ID]):
        self.db = db

    async def get(self, id: ID) -> Optional[Entity]:
        return await self.db.get(id)

    async def save(self, save_dict: Dict[str, Any]) -> Entity:
        if save_dict.get("id", None):
            entity = await self.get(save_dict.get("id"))
            return await self.db.update(entity, save_dict)
        else:
            return await self.db.create(save_dict)

    async def delete(self, id: ID) -> None:
        entity = await self.get(id)
        await self.db.delete(entity)
