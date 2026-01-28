from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.modules.expenses.models import Expense
from app.modules.expenses.schemas import CreateExpense

class ExpenseRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_by_id(self, expense_id: int):
        query = select(Expense).where(Expense.id == expense_id)
        result = await self.session.execute(query)
        return result.scalar_one_or_none()

    async def create(self, expense_data: CreateExpense, user_id: int) -> Expense:
        db_expense = Expense(
            category_id=expense_data.category_id,
            name=expense_data.name,
            spent=expense_data.spent,
            user_id=user_id
        )
        self.session.add(db_expense)
        await self.session.flush()
        await self.session.refresh(db_expense)
        return db_expense

    async def update(self, expense: Expense, update_data: dict) -> Expense:
        for key, value in update_data.items():
            setattr(expense, key, value)
        await self.session.flush()
        await self.session.refresh(expense)
        return expense

    async def delete(self, expense: Expense) -> None:
        self.session.delete(expense)
        await self.session.flush()

    async def get_by_name(self, expense_name: str):
        query = select(Expense).where(Expense.name == expense_name)
        result = await self.session.execute(query)
        return result.scalar_one_or_none()