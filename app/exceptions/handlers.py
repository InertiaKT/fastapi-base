from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import JSONResponse

from app.response import ErrorResponse
from app.exceptions.custom_exceptions import CustomException

# 3. 编写异常处理函数
async def custom_exception_handler(request: Request, exc: CustomException) -> JSONResponse:
    """
    处理 CustomException 异常的处理函数
    """
    # # 通常这里会记录日志
    # print(f"CustomException occurred: {exc.message}, Detail: {exc.detail}")

    # 返回一个 JSONResponse
    return JSONResponse(
        status_code=500,  # 或者根据 exc.error_code 动态设置，但注意 HTTP 状态码和业务错误码的区别
        content=ErrorResponse(msg=exc.message, data=exc.detail).model_dump()
    )


async def http_exception_handler(request: Request, exc: HTTPException) -> JSONResponse:
    """
    处理 FastAPI/Starlette 的 HTTPException 的处理函数
    """
    # print(f"HTTPException occurred: Status Code {exc.status_code}, Detail: {exc.detail}")
    return JSONResponse(
        status_code=exc.status_code,
        content=ErrorResponse(msg=exc.detail).model_dump()
    )


async def global_exception_handler(request: Request, exc: Exception) -> JSONResponse:
    """
    一个更全局的异常处理函数，用于捕获其他未特殊处理的异常
    """
    # 记录详细的错误日志，这对于调试非常重要
    # print(f"Unexpected exception occurred: {str(exc)}")
    # 注意：在生产环境中，出于安全考虑，不建议向客户端返回详细的异常信息
    return JSONResponse(
        status_code=500,
        content=ErrorResponse(
            code=500,
            msg="Internal Server Error",
            data=str(exc)   # 调试模式下显示详情，生产模式下隐藏
        ).model_dump()
    )

def register_exception_handlers(app: FastAPI):
    # 4. 使用 add_exception_handler 注册异常处理函数
    #    将异常类与处理函数绑定
    app.add_exception_handler(CustomException, custom_exception_handler)
    app.add_exception_handler(HTTPException, http_exception_handler)
    app.add_exception_handler(Exception, global_exception_handler)


