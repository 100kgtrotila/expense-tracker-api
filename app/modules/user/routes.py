from email.policy import HTTP
from http.client import HTTPException

from fastapi import APIRouter, status
from fastapi.params import Depends
from fastapi.security import OAuth2PasswordRequestForm

from app.core.security import create_access_token
from app.modules.user.dependencies import get_user_service
from app.modules.user.schemas import UserResponse, CreateUser, Token
from app.modules.user.services import UserService

router = APIRouter(prefix="/user", tags=["User"])

@router.post("/register", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
async def register_user(user_data: CreateUser, service: UserService = Depends(get_user_service)):
    return await service.register_new_user(user_data=user_data)

@router.post("/login", response_model=Token)
async def login_user(form_data: OAuth2PasswordRequestForm = Depends(), service: UserService = Depends(get_user_service)):
    user = await service.authenticate_user(email=form_data.username, password=form_data.password)

    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or pass",
            headers={"WWW-Authenticate": "Bearer"},
        )

    access_token = create_access_token(data={"sub": user.email})

    return {"access_token": access_token, "token_type": "bearer"}

