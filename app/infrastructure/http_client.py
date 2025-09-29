from logging import exception

import httpx
import logging
import asyncio
from typing import Optional


http_client_logger = logging.getLogger("infra.http_client")

class MaxRetryError(Exception):
     pass


class AsyncHttpClient:
    """
        异步 HTTP 客户端封装，支持基于 httpx.Request 的重试逻辑
        可以同时支持普通请求和 stream=True 的流式请求
        """

    def __init__(self, base_url: str, max_retries: int = 3, backoff_factor: float = 0.5, timeout: Optional[float] = 10.0):
        self.base_url = base_url
        self.max_retries = max_retries
        self.backoff_factor = backoff_factor
        self.timeout = timeout
        self.client = httpx.AsyncClient(base_url=self.base_url, timeout=self.timeout)

    def build_request(self, method: str, url: str, **kwargs) -> httpx.Request:
        """
        构建请求对象
        :param method: 请求方法
        :param url: 请求 URL
        :param kwargs: 请求参数
        :return: httpx.Request
        """
        return self.client.build_request(method, url, **kwargs)

    async def send(self, request: httpx.Request, stream: bool = False) -> httpx.Response:
        """
        发送请求，自动重试
        :param request: httpx.Request 对象
        :param stream: 是否开启流式响应
        :return: httpx.Response
        """
        for attempt in range(1, self.max_retries + 1):
            try:
                resp = await self.client.send(request, stream=stream)
                resp.raise_for_status()
                return resp
            except (httpx.RequestError, httpx.HTTPStatusError) as e:
                wait_time = self.backoff_factor * (2 ** (attempt - 1))
                http_client_logger.warning(f"[send] Attempt {attempt} failed: {e}, retrying in {wait_time}s...")
                await asyncio.sleep(wait_time)
        raise MaxRetryError("[send] Max retries exceeded")


