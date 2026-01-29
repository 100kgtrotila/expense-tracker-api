from fastapi import FastAPI, status
from h11 import Request
from starlette.responses import JSONResponse

from app.core.exceptions import NotFoundException, AlreadyExistsException, PermissionDeniedException, BaseAppException


def register_exeption_handlers(app: FastAPI):
    @app.exception_handler(NotFoundException)
    async def not_found_handler(request: Request, exc: NotFoundException):
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND,
            content={
                "detail": str(exc)
            }
        )

    @app.exception_handler(AlreadyExistsException)
    async def conflict_handler(request: Request, exc: AlreadyExistsException):
        return JSONResponse(
            status_code=status.HTTP_409_CONFLICT,
            content={"detail": str(exc)}
        )

    @app.exception_handler(PermissionDeniedException)
    async def permission_exception_handler(request: Request, exc: PermissionDeniedException):
        return JSONResponse(
            status_code=status.HTTP_401_UNAUTHORIZED,
            content={"detail": str(exc)}
        )

    @app.exception_handler(BaseAppException)
    async def base_exception_handler(request: Request, exc: BaseAppException):
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={"detail": str(exc)}
        )