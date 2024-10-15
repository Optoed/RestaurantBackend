from fastapi import APIRouter

from project.infrastructure.postgres.repository.product_repo import UserRepository
from project.infrastructure.postgres.database import PostgresDatabase
from project.schemas.product import ProductSchema


router = APIRouter()


@router.get("/all_products", response_model=list[ProductSchema])
async def get_all_products() -> list[ProductSchema]:
    user_repo = UserRepository()
    database = PostgresDatabase()

    async with database.session() as session:
        await user_repo.check_connection(session=session)
        all_products = await user_repo.get_all_products(session=session)

    return all_products
