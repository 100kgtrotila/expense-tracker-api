from pydantic import BaseModel, Field, EmailStr, ConfigDict


class UserBase(BaseModel):
    email: EmailStr = Field(..., description="user email")
    password: str = Field(..., gt=5, description="user password")

class CreateUser(UserBase):
    pass

class UserResponse(UserBase):
    id: int
    is_active: bool = True

    model_config = ConfigDict(from_attributes=True)

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: str | None = None