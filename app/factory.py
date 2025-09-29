from fastapi import FastAPI

from app.api.v1.router import register_v1_router
from app.middlewares import register_middlewares
from app.exceptions.handlers import register_exception_handlers


def factory() -> FastAPI:
    app = FastAPI(
        title="algo platform"
    )

    register_middlewares(app)

    register_exception_handlers(app)

    register_v1_router(app)

    return app
