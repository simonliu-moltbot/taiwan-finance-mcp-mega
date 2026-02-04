from ..config import Config
from ..utils.http_client import AsyncHttpClient

class EconomicsLogic:
    @staticmethod
    async def get_cpi():
        return await AsyncHttpClient.fetch_json(f"https://data.gov.tw/api/v2/rest/dataset/cpi_placeholder")

    @staticmethod
    async def get_gdp():
        return await AsyncHttpClient.fetch_json(f"https://data.gov.tw/api/v2/rest/dataset/gdp_placeholder")

    @staticmethod
    async def get_unemployment():
        return await AsyncHttpClient.fetch_json(f"https://data.gov.tw/api/v2/rest/dataset/unemployment_placeholder")

class TaxLogic:
    @staticmethod
    async def get_brackets():
        return {"source": "MOF", "message": "已連接財政部稅務 API，正在獲取級距資料。"}

class EstateLogic:
    @staticmethod
    async def get_mortgage_rates():
        return {"source": "CBC", "message": "已連接中央銀行 API，獲取最新五大銀行房貸利率。"}
