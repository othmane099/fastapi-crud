from typing import Generic, Optional, Any

from crud.types import Entity, ID


class BaseDatabase(Generic[Entity, ID]):

    async def get(self, id: ID) -> Optional[Entity]:
        raise NotImplementedError()

    async def create(self, create_dict: dict[str, Any]) -> Entity:
        raise NotImplementedError()

    async def update(self, entity: Entity, update_dict: dict[str, Any]) -> Entity:
        raise NotImplementedError()

    async def delete(self, entity: Entity) -> None:
        raise NotImplementedError()
