import logging
from fastapi import APIRouter
from fastapi.responses import JSONResponse

from app.response import SuccessResponse
from app.service import HelloServiceFactory

logger = logging.getLogger("endpoint.hello")

router = APIRouter()


@router.get("/hello")
async def say_hello():
    logger.info("[Say Hello] Start")
    result = HelloServiceFactory.get_instance().say()
    logger.info(f"[Say Hello] End - result: {result}")
    return JSONResponse(content=SuccessResponse(data=result).model_dump())
