import httpx
import logging
import asyncio
from typing import Any, Dict, Optional
from cachetools import TTLCache
from taiwan_finance_mcp_mega.config import Config

logging.basicConfig(level=Config.LOG_LEVEL)
logger = logging.getLogger(Config.APP_NAME)

class AsyncHttpClient:
    """
    [v3.5.7] 帶有時效性緩存 (LRU Cache) 的異步 HTTP 客戶端。
    優化證交所巨量數據下載，解決 Read Timed Out 與 500 錯誤。
    """
    _client: httpx.AsyncClient = None
    
    # 緩存：最多存 100 個回應，每個有效 300 秒 (5分鐘)
    _cache = TTLCache(maxsize=100, ttl=300)
    _lock = asyncio.Lock()

    @classmethod
    async def get_client(cls) -> httpx.AsyncClient:
        if cls._client is None or cls._client.is_closed:
            # 擴大超時限制至 45 秒以應對巨型 JSON
            cls._client = httpx.AsyncClient(
                timeout=45.0, 
                follow_redirects=True,
                headers={"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"}
            )
        return cls._client

    @classmethod
    async def fetch_json(cls, url: str, params: Optional[Dict[str, Any]] = None):
        # 1. 檢查緩存
        cache_key = f"{url}_{sorted(params.items()) if params else ''}"
        if cache_key in cls._cache:
            logger.info(f"CACHE_HIT: {url}")
            return cls._cache[cache_key]

        # 2. 異步鎖定：避免同時多個請求重複下載大檔案
        async with cls._lock:
            if cache_key in cls._cache:
                return cls._cache[cache_key]

            # 3. 執行真實請求
            client = await cls.get_client()
            try:
                logger.info(f"FETCHING_REAL_DATA: {url}")
                response = await client.get(url, params=params)
                response.raise_for_status()
                data = response.json()
                
                # 4. 寫入緩存
                cls._cache[cache_key] = data
                return data
            except httpx.ReadTimeout:
                logger.error(f"TIMEOUT: {url}")
                return {"error": "遠端伺服器回應超時 (Read Timeout)，數據量過大或證交所繁忙。"}
            except Exception as e:
                logger.error(f"Request failed: {url} - {str(e)}")
                return {"error": f"API 請求失敗: {str(e)}"}

    @classmethod
    async def close(cls):
        if cls._client:
            await cls._client.aclose()
