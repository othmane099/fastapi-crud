from typing import Callable

from fastapi import APIRouter, Depends

from crud.manager import BaseManager
from crud.types import ID


def get_delete_router(get_manager: Callable, base_name: str) -> APIRouter:
    router = APIRouter()

    @router.delete("/"+str(base_name)+"/{entity_id}")
    async def delete(entity_id: ID, manager: BaseManager = Depends(get_manager)):
        return await manager.delete(entity_id)

    return router

