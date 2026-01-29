from sqlalchemy.orm.sync import update

from app.core.exceptions import NotFoundException
from app.modules.expenses.models import Expense
from app.modules.expenses.repository import ExpenseRepository
from app.modules.expenses.schemas import CreateExpense, UpdateExpense


class ExpenseService:
    def __init__(self, repository: ExpenseRepository):
        self.repository = repository

    async def get_expense_by_id(self, expense_id) -> Expense:
        expense = await self.repository.get_by_id(expense_id)
        if not expense:
            raise NotFoundException(f"Expense with id{expense_id} not found")
        return expense

    async def create_expense(self, expense_data: CreateExpense, user_id: int) -> Expense:
        new_expense = await self.repository.create(expense_data, user_id)
        try:
            await self.repository.session.commit()
            await self.repository.session.refresh(new_expense)
            return new_expense
        except Exception:
            await self.repository.session.rollback()

    async def update_expense(self, expense_id: int, expense_data: UpdateExpense) -> Expense:
        expense = await self.get_expense_by_id(expense_id)
        update_dict = expense_data.model_dump(exclude_unset=True)
        updated_expense = await self.repository.update(expense, update_dict)
        try:
            await self.repository.session.commit()
            return  updated_expense
        except Exception:
            await  self.repository.session.rollback()

    async def delete_expense(self, expense_id: int) -> None:
        expense = await self.get_expense_by_id(expense_id)
        await self.repository.delete(expense)
        try:
            await self.repository.session.commit()
        except Exception:
            await self.repository.session.rollback()


