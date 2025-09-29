import logging
from fastapi import APIRouter
from fastapi.responses import JSONResponse

from app.response import SuccessResponse

endpoint_logger = logging.getLogger("endpoint")

router = APIRouter()


@router.get("/ping")
async def ping():
    endpoint_logger.info("[ping] Success")
    return JSONResponse(content=SuccessResponse(data="pong").model_dump())
