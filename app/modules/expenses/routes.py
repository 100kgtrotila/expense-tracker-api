from typing import Optional

from fastapi import APIRouter, status
from fastapi.params import Depends

from app.modules.expenses.dependencies import get_expense_service
from app.modules.expenses.schemas import ExpenseResponse, PaginatedResponse, CreateExpense, UpdateExpense
from app.modules.expenses.services import ExpenseService
from app.modules.user.dependencies import get_current_user
from app.modules.user.models import User

router = APIRouter(prefix="/expenses", tags=["Expenses"])

@router.get("/{expense_id}", response_model=ExpenseResponse)
async def get_expense_by_id(expense_id: int, service: ExpenseService = Depends(get_expense_service)):
    return await service.get_expense_by_id(expense_id=expense_id)

@router.get("/", response_model=PaginatedResponse)
async def get_my_expenses(page: int = 1,
    limit: int = 10,
    search: Optional[str] = None,
    service: ExpenseService = Depends(get_expense_service),
    current_user: User = Depends(get_current_user)):

    skip = (page - 1) * limit

    expenses = await service.get_expenses_by_user(user_id=current_user.id, limit=limit, skip=skip, search=search)
    return {
        "data": expenses,
        "page": page,
        "limit": limit
    }

@router.post("/", response_model=ExpenseResponse, status_code=status.HTTP_201_CREATED)
async def create_expense(expense_data: CreateExpense, service: ExpenseService = Depends(get_expense_service), current_user: User = Depends(get_current_user)):
    return await service.create_expense(expense_data=expense_data, user_id=current_user.id)

@router.patch("/{expense_id}", response_model=ExpenseResponse, status_code=status.HTTP_200_OK)
async def update_expense(expense_id: int, expense_data: UpdateExpense, service: ExpenseService = Depends(get_expense_service)):
    return await service.update_expense(expense_id=expense_id, expense_data=expense_data)

@router.delete("/{expense_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_expense(espense_id: int, service: ExpenseService = Depends(get_expense_service)):
    await service.delete_expense(expense_id=espense_id)




