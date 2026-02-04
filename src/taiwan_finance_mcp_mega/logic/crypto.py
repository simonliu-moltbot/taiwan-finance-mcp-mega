from ..config import Config
from ..utils.http_client import AsyncHttpClient

class CryptoLogic:
    @staticmethod
    async def get_price(coin_id: str = "bitcoin"):
        url = f"{Config.COINGECKO_BASE}/simple/price?ids={coin_id}&vs_currencies=twd,usd&include_24hr_change=true"
        return await AsyncHttpClient.fetch_json(url)

    @staticmethod
    async def get_trending():
        url = f"{Config.COINGECKO_BASE}/search/trending"
        return await AsyncHttpClient.fetch_json(url)
