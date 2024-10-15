from typing import Type

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import text

from project.schemas.product import ProductSchema
from project.infrastructure.postgres.models import Product

from project.core.config import settings


class UserRepository:
    _collection: Type[Product] = Product

    async def check_connection(
        self,
        session: AsyncSession,
    ) -> bool:
        query = "select 1;"

        result = await session.scalar(text(query))

        return True if result else False

    async def get_all_products(
        self,
        session: AsyncSession,
    ) -> list[ProductSchema]:
        query = f"select * from {settings.POSTGRES_SCHEMA}.product;"

        products = await session.execute(text(query))

        return [ProductSchema.model_validate(obj=product) for product in products.mappings().all()]

