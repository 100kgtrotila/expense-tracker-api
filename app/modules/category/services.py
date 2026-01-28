from app.modules.category.models import Category
from app.modules.category.repository import CategoryRepository
from app.modules.category.schemas import CategoryCreate, CategoryUpdate


class CategoryService:
    def __init__(self, repository: CategoryRepository):
        self.repository = repository

    async def get_category_by_id(self, category_id) -> Category:
        category = await self.repository.get_by_id(category_id)
        if not category:
            raise Exception("Category not found")
        return category

    async def create_category(self, category_data: CategoryCreate) -> Category | None:
        if await self.repository.get_by_name(category_data.name):
            raise Exception("This name is taken")
        new_category = await self.repository.create(category_data.name)

        try:
            await self.repository.session.commit()
            await self.repository.session.refresh(new_category)
            return new_category
        except Exception:
            await self.repository.session.rollback()

    async def update_category(self, category_id: int, category_data: CategoryUpdate) -> Category | None:
        category = await self.get_category_by_id(category_id)
        update_dict = category_data.model_dump(exclude_unset=True)
        updated_category = await self.repository.update(category, update_dict)

        try:
            await self.repository.session.commit()
            return updated_category
        except Exception:
            await self.repository.session.rollback()

    async def delete_category(self, category_id) -> None:
        category = await self.get_category_by_id(category_id)
        await self.repository.delete(category)
        try:
            await self.repository.session.commit()
        except Exception:
            await  self.repository.session.rollback()
            raise





