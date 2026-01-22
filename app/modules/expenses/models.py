from sqlalchemy import Integer, String, Column, ForeignKey, Float, DateTime
from datetime import datetime, timezone

from sqlalchemy.orm import relationship

from app.core.db import Base


class Expense(Base):
    __tablename__ = "expenses"

    id=Column(Integer, primary_key=True, index=True)
    category_id = Column(Integer, ForeignKey('category_id'))
    name = Column(String, index=True, nullable=False)
    spent = Column(Float, index=True)
    created_at = Column(DateTime(timezone=True), default=datetime.now(timezone.utc), nullable=False)

    category = relationship("Category", back_populates =True)

    owner = relationship("User", back_populates="expenses")