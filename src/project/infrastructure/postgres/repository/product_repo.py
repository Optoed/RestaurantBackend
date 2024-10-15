import string
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

        return [ProductSchema.model_validate(dict(product)) for product in products.mappings().all()]

    async def get_product_by_ID(
            self,
            session: AsyncSession,
            ID: int
    ) -> ProductSchema:
        query = text(f"select * from {settings.POSTGRES_SCHEMA}.product where id = :id")

        result = await session.execute(query, {"id": ID})

        product_row = result.fetchone()

        if product_row:
            return ProductSchema.model_validate(dict(product_row))
        return None

    async def insert_product(
            self,
            session: AsyncSession,
            name: string,
            cost: int
    ) -> ProductSchema:
        query = text(f"""
               INSERT INTO {settings.POSTGRES_SCHEMA}.product (name, cost) 
               VALUES (:name, :cost)
               RETURNING id, name, cost
           """)
        result = await session.execute(query, {"name" : name, "cost" : cost})

        product_row = result.fetchone()

        if product_row:
            return ProductSchema.model_validate(dict(product_row))
        return None


