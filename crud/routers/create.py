from typing import Callable, Type

from fastapi import APIRouter, Depends

from crud.manager import BaseManager
from crud.types import Schema


def get_create_router(get_manager: Callable, base_name: str, schema: Type[Schema]) -> APIRouter:
    router = APIRouter()

    @router.post("/"+str(base_name))
    async def create(entity: schema, manager: BaseManager = Depends(get_manager)):
        return await manager.save(dict(entity))

    return router

