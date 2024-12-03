from typing import Generic, Callable, Type

from fastapi import APIRouter

from crud.routers.create import get_create_router
from crud.routers.delete import get_delete_router
from crud.routers.read import get_read_router
from crud.routers.update import get_update_router
from crud.types import Entity, ID, Schema


class CRUD(Generic[Entity, ID]):
    def __init__(self, get_manager: Callable):
        self.get_manager = get_manager

    def get_read_router(self, base_name: str) -> APIRouter:
        return get_read_router(self.get_manager, base_name)

    def get_create_router(self, base_name: str, schema: Type[Schema]) -> APIRouter:
        return get_create_router(self.get_manager, base_name, schema)

    def get_update_router(self, base_name: str, schema: Type[Schema]) -> APIRouter:
        return get_update_router(self.get_manager, base_name, schema)

    def get_delete_router(self, base_name: str) -> APIRouter:
        return get_delete_router(self.get_manager, base_name)
