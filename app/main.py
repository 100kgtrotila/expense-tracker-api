import uvicorn
from fastapi import FastAPI

from app.core.errors import register_exeption_handlers
from app.modules.category.routes import router as category_router
from app.modules.expenses.routes import router as expense_router
from app.modules.user.routes import router as user_router

app = FastAPI(title="Expense Tracker API")
register_exeption_handlers(app)
app.include_router(category_router)
app.include_router(expense_router)
app.include_router(user_router)


if __name__ == "__main__":
    uvicorn.run("app.main:app", host="127.0.0.1", port=8000, reload=True)
