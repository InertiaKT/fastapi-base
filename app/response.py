from typing import Any
from pydantic import BaseModel, Field


class BaseResponse(BaseModel):
    code: int
    msg: str
    data: Any = None


class SuccessResponse(BaseResponse):
    code: int = Field(default=200)
    msg: str = Field(default="success")


class ErrorResponse(BaseResponse):
    code: int = Field(default=500)
    msg: str = Field(default="error")
