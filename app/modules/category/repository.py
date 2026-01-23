from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.modules.category.models import Category

class CategoryRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_by_id(self, category_id: int):
        query = select(Category).where(Category.id == category_id)
        result = await self.session.execute(query)
        return result.scalar_one_or_none()

    async def create(self, category_name: str) -> Category:
        db_category = Category(name=category_name)
        self.session.add(db_category)
        await self.session.flush()
        return db_category

    async def delete(self, category: Category) -> None:
        self.session.delete(category)
        await self.session.flush()

    async def update(self, category: Category, updated_name: str) -> Category:
        category.name = updated_name
        await self.session.flush()
        await self.session.refresh(category)
        return category