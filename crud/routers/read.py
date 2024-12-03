from typing import Callable

from fastapi import APIRouter, Depends

from crud.manager import BaseManager
from crud.types import ID


def get_read_router(get_manager: Callable, base_name: str) -> APIRouter:
    router = APIRouter()

    @router.get("/"+str(base_name)+"/{entity_id}")
    async def get(entity_id: ID, manager: BaseManager = Depends(get_manager)):
        return await manager.get(entity_id)

    return router

