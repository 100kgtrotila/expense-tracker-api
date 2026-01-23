from sqlalchemy import Select
from sqlalchemy.orm import session

from app.modules.category.models import Category


class CategoryRepository:
    def __init__(self):
        self.session = session

    async def get_by_id(self, category_id: int):
        query = Select(Category).where(Category.id == category_id)
        result = await self.session.execute(query)
        return result.scalar_one_or_none()

    async def create(self, category_name: str) -> Category:
        db_category = Category(
            name=category_name
        )
        self.session.add(db_category)
        await self.session.flush()
        return db_category

    async def delete(self, category: Category) -> None:
        await self.session.delete(category)

    async def update(self, category_id: int, updated_category_name: str) -> Category:
        query = Select(Category).where(Category.id == category_id)
        result = await self.session.execute(query)
        category = result.scalar_one_or_none()

        category.name = updated_category_name

        await self.session.commit()
        await self.session.refresh(category)
        return category




