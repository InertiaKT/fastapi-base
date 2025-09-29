from app.service.hello import HelloService


class HelloServiceFactory:
    _hello_service: HelloService | None = None

    @classmethod
    def get_instance(cls) -> HelloService:
        if cls._hello_service is None:
            cls._hello_service = HelloService()
        return cls._hello_service
