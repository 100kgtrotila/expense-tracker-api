from typing import List

from fastapi import APIRouter
from fastapi import status
from fastapi.params import Depends

from app.modules.category.dependencies import get_category_service
from app.modules.category.schemas import CategoryResponse, CategoryCreate, CategoryUpdate
from app.modules.category.services import CategoryService

router = APIRouter(prefix="/cats", tags=["Categories"])

@router.get("/", response_model = List[CategoryResponse])
async def get_all_categories(service: CategoryService = Depends(get_category_service)):
    categories = await service.get_all_categories()
    return categories

@router.get("/{category_id}", response_model=CategoryResponse)
async def get_category_by_id(category_id: int, service: CategoryService = Depends(get_category_service)):
    return await service.get_category_by_id(category_id=category_id)

@router.post("/", response_model=CategoryResponse, status_code=status.HTTP_201_CREATED)
async def create_category(category_data: CategoryCreate, service: CategoryService = Depends(get_category_service)):
    return await service.create_category(category_data=category_data)

@router.patch("/{category_id}", response_model=CategoryResponse)
async def update_category(category_id: int, category_data: CategoryUpdate, service: CategoryService = Depends(get_category_service)):
    return await service.update_category(category_id, category_data)

@router.delete("/{category_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_category(category_id: int, service: CategoryService = Depends(get_category_service)):
    await service.delete_category(category_id)





