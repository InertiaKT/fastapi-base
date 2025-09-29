import uvicorn

from app import factory as app_factory
from app.settings import settings

if __name__ == '__main__':
    uvicorn.run(app_factory, host=settings.server_host, port=settings.server_port)
