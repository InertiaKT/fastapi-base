class CustomException(Exception):
    code: int = 1000
    message: str = "应用内部错误"
    detail: str | None = None

    def __init__(self, *, code: int | None = None, message: str | None = None, detail: str | None = None):
        if code is not None:
            self.code = code
        if message is not None:
            self.message = message
        if detail is not None:
            self.detail = detail
        super().__init__(self.message)

class ArgumentsValidationException(CustomException):
    code: int = 1001
    message: str = "参数验证错误"


