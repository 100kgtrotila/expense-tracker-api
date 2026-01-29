from datetime import datetime
from decimal import Decimal
from typing import Optional, List

from pydantic import BaseModel, Field, ConfigDict


class ExpenseBase(BaseModel):
    category_id: int = Field(..., description="Category ID")
    name: str = Field(..., min_length=3, max_length=50, description="Expense Name")
    spent: Decimal = Field(..., gt=0, decimal_places=2, description="Amount spent")

class CreateExpense(ExpenseBase):
    pass

class ExpenseResponse(ExpenseBase):
    id: int
    user_id: int
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class UpdateExpense(ExpenseBase):
    name: Optional[str] = None
    spent: Optional[Decimal] = None
    category_id: Optional[int] = None

class PaginatedResponse(BaseModel):
    data: List[ExpenseResponse]
    page: int
    limit: int
    total: int