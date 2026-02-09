import httpx
import logging
import asyncio
import csv
import io
from typing import Any, Dict, Optional, List
from cachetools import TTLCache
from taiwan_finance_mcp_mega.config import Config

logging.basicConfig(level=Config.LOG_LEVEL)
logger = logging.getLogger(Config.APP_NAME)

class AsyncHttpClient:
    """
    [v3.9.2] 帶有時效性緩存與 CSV 解析支援的異步 HTTP 客戶端。
    """
    _client: httpx.AsyncClient = None
    _cache = TTLCache(maxsize=100, ttl=300)
    _lock = asyncio.Lock()

    @classmethod
    async def get_client(cls) -> httpx.AsyncClient:
        if cls._client is None or cls._client.is_closed:
            cls._client = httpx.AsyncClient(
                timeout=45.0, 
                follow_redirects=True,
                headers={"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"}
            )
        return cls._client

    @classmethod
    async def fetch_json(cls, url: str, params: Optional[Dict[str, Any]] = None, headers: Optional[Dict[str, str]] = None):
        cache_key = f"json_{url}_{sorted(params.items()) if params else ''}_{sorted(headers.items()) if headers else ''}"
        if cache_key in cls._cache:
            return cls._cache[cache_key]

        async with cls._lock:
            if cache_key in cls._cache: return cls._cache[cache_key]
            client = await cls.get_client()
            try:
                response = await client.get(url, params=params, headers=headers)
                response.raise_for_status()
                data = response.json()
                cls._cache[cache_key] = data
                return data
            except Exception as e:
                logger.error(f"JSON Fetch Error: {url} - {str(e)}")
                return {"error": str(e), "status": "failed"}

    @classmethod
    async def fetch_csv_as_json(cls, url: str) -> List[Dict[str, Any]]:
        """抓取 CSV 並轉換為 JSON 格式 (List of Dicts)"""
        cache_key = f"csv_{url}"
        if cache_key in cls._cache:
            return cls._cache[cache_key]

        async with cls._lock:
            if cache_key in cls._cache: return cls._cache[cache_key]
            client = await cls.get_client()
            try:
                response = await client.get(url)
                response.raise_for_status()
                # 處理編碼 (政府資料常使用 Big5 或 UTF-8 with BOM)
                content = response.content.decode('utf-8-sig')
                f = io.StringIO(content)
                reader = csv.DictReader(f)
                data = list(reader)
                cls._cache[cache_key] = data
                return data
            except Exception as e:
                logger.error(f"CSV Fetch Error: {url} - {str(e)}")
                return []

    @classmethod
    async def close(cls):
        if cls._client:
            await cls._client.aclose()
