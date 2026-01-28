from fastapi.params import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.db import get_db
from app.modules.expenses.repository import ExpenseRepository

def get_expense_repository(db: AsyncSession = Depends(get_db)) -> ExpenseRepository:
    return ExpenseRepository(session=db)