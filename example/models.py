from sqlalchemy import INTEGER, String
from sqlalchemy.orm import Mapped, mapped_column

from db import Base


class Product(Base):
    __tablename__ = "products"

    id: Mapped[int] = mapped_column(INTEGER, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String, nullable=False)

