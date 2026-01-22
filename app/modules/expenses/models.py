from sqlalchemy import Integer, String, Column, ForeignKey, DECIMAL, DateTime
from datetime import datetime, timezone

from sqlalchemy.orm import relationship

from app.core.db import Base


class Expense(Base):
    __tablename__ = "expenses"

    id=Column(Integer, primary_key=True, index=True)
    category_id = Column(Integer, ForeignKey('categories.id'))
    user_id = Column(Integer, ForeignKey("users.id"))
    name = Column(String, index=True, nullable=False)
    spent = Column(DECIMAL, index=True)
    created_at = Column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc), nullable=False)

    category = relationship("Category", back_populates =True)

    owner = relationship("User", back_populates="expenses")