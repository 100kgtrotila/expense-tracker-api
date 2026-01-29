from app.core.exceptions import AlreadyExistsException
from app.core.security import get_password_hash, verify_password
from app.modules.user.models import User
from app.modules.user.repository import UserRepository
from app.modules.user.schemas import CreateUser


class UserService:
    def __init__(self, repository: UserRepository):
        self.repository = repository

    async def register_new_user(self, user_data: CreateUser) -> User | None:
        if await self.repository.get_by_email(user_data.email):
            raise AlreadyExistsException(f"Email{user_data.email} is alredy taken")

        hashed_password = get_password_hash(user_data.password)
        new_user = await self.repository.create(user_data, hashed_password)
        try:
            await self.repository.session.commit()
            await self.repository.session.refresh(new_user)
            return new_user
        except Exception:
            await self.repository.session.rollback()

    async def authenticate_user(self, email: str, password: str) -> User | None:
        user = await self.repository.get_by_email(email)
        if not user:
            return None

        if not verify_password(password, user.password):
            return None

        return user



