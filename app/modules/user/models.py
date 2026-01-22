from operator import index

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from app.core.db import Base


class User(Base):
    __tablename__ = "users"

    id=Column(Integer, primary_key=True, index=True)
    email=Column(String, index=True, uniq=True, nullable=False)
    password=Column(String, nullable=False)

    Espenses = relationship("Expense", back_populates="owner")


