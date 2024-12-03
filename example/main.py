from contextlib import asynccontextmanager

from fastapi import FastAPI

import products
import schemas
from db import create_db_and_tables


@asynccontextmanager
async def lifespan(app: FastAPI):
    await create_db_and_tables()
    yield


app = FastAPI(lifespan=lifespan)


app.include_router(products.crud.get_create_router("products", schemas.CreateProduct))
app.include_router(products.crud.get_delete_router("products"))
app.include_router(products.crud.get_update_router("products", schemas.UpdateProduct))
app.include_router(products.crud.get_read_router("products"))
