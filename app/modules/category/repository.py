from sqlalchemy import select, Sequence
from sqlalchemy.ext.asyncio import AsyncSession
from app.modules.category.models import Category

class CategoryRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_by_id(self, category_id: int):
        query = select(Category).where(Category.id == category_id)
        result = await self.session.execute(query)
        return result.scalar_one_or_none()

    async def get_all(self) -> Sequence[Category]:
        query = select(Category).order_by(Category.id)
        result = await self.session.execute(query)
        return result.scalars().all()

    async def create(self, category_name: str) -> Category:
        db_category = Category(name=category_name)
        self.session.add(db_category)
        await self.session.flush()
        return db_category

    async def delete(self, category: Category) -> None:
        self.session.delete(category)
        await self.session.flush()

    async def update(self, category: Category, update_data: dict) -> Category:
        for key, value in update_data.items():
            setattr(category, key, value)
        await self.session.flush()
        await self.session.refresh(category)
        return category

    async def get_by_name(self, category_name: str):
        query = select(Category).where(Category.name == category_name)
        result = await self.session.execute(query)
        return result.scalar_one_or_none()