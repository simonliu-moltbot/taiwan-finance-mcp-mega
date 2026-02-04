from ..config import Config
from ..utils.http_client import AsyncHttpClient

class StockLogic:
    @staticmethod
    async def get_day_all():
        url = f"{Config.TWSE_BASE}/exchangeReport/STOCK_DAY_ALL"
        return await AsyncHttpClient.fetch_json(url)

    @staticmethod
    async def get_monthly_revenue():
        url = f"{Config.TWSE_BASE}/opendata/t187ap05_P"
        return await AsyncHttpClient.fetch_json(url)

    @staticmethod
    async def get_eps_ranking():
        url = f"{Config.TWSE_BASE}/opendata/t187ap14_L"
        return await AsyncHttpClient.fetch_json(url)
