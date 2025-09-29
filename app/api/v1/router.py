from fastapi import APIRouter, FastAPI

from app.api.v1.endpoints.base import router as base_router
from app.api.v1.endpoints.hello import router as hello_router


def register_v1_router(app: FastAPI):
    v1_router = APIRouter()

    v1_router.include_router(base_router)
    v1_router.include_router(hello_router)

    app.include_router(v1_router, prefix="/v1")
