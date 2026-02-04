import httpx
import logging
from ..config import Config

logging.basicConfig(level=Config.LOG_LEVEL)
logger = logging.getLogger(Config.APP_NAME)

class AsyncHttpClient:
    _client: httpx.AsyncClient = None

    @classmethod
    async def get_client(cls) -> httpx.AsyncClient:
        if cls._client is None or cls._client.is_closed:
            cls._client = httpx.AsyncClient(timeout=15.0, follow_redirects=True)
        return cls._client

    @classmethod
    async def fetch_json(cls, url: str):
        client = await cls.get_client()
        try:
            logger.debug(f"Fetching: {url}")
            response = await client.get(url)
            response.raise_for_status()
            return response.json()
        except Exception as e:
            logger.error(f"Request failed: {url} - {str(e)}")
            return {"error": f"API request failed: {str(e)}"}

    @classmethod
    async def close(cls):
        if cls._client:
            await cls._client.aclose()
