import os
import sys

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

sys.path.append(f"{os.getcwd()}/..")
from crud import DatabaseAdapter, BaseDatabase, CRUD, BaseManagerImpl
from db import get_async_session
from models import Product


async def get_car_db(session: AsyncSession = Depends(get_async_session)):
    yield DatabaseAdapter[Product, int](session, Product)


async def get_manager(car_db: BaseDatabase[Product, int] = Depends(get_car_db)):
    yield BaseManagerImpl(car_db)


crud = CRUD(get_manager)
