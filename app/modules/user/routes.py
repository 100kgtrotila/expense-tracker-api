from fastapi import APIRouter, status
from fastapi.params import Depends
from fastapi.security import OAuth2PasswordRequestForm

from app.modules.user.dependencies import get_user_service
from app.modules.user.schemas import UserResponse, CreateUser
from app.modules.user.services import UserService

router = APIRouter(prefix="/user", tags=["User"])

@router.post("/register", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
async def register_user(user_data: CreateUser, service: UserService = Depends(get_user_service)):
    return await service.register_new_user(user_data=user_data)

@router.post("/login", response_model=UserResponse)
async def login_user(form_data: OAuth2PasswordRequestForm = Depends(), service: UserService = Depends(get_user_service)):
    return await service.authenticate_user(email=form_data.username, password=form_data.password)

