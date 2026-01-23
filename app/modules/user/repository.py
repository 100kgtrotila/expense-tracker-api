from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.modules.user.models import User
from app.modules.user.schemas import CreateUser

class UserRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_by_id(self, user_id: int) -> User | None:
        query = select(User).where(User.id == user_id)
        result = await self.session.execute(query)
        return result.scalar_one_or_none()

    async def get_by_email(self, user_email: str) -> User | None:
        query = select(User).where(User.email == user_email)
        result = await self.session.execute(query)
        return result.scalar_one_or_none()

    async def create(self, user_data: CreateUser, hashed_password: str) -> User:
        db_user = User(
            email=user_data.email,
            password=hashed_password
        )

        self.session.add(db_user)
        await self.session.flush()
        return db_user

    async def delete(self, user: User) -> None:
        self.session.delete(user)
        await self.session.flush()
