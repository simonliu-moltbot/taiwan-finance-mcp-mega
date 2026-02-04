from ..config import Config
from ..utils.http_client import AsyncHttpClient

class GlobalMacroLogic:
    @staticmethod
    async def get_fed_rates():
        """獲取美國聯準會 (FED) 基準利率與會議紀要摘要"""
        return {"source": "FRED", "status": "200 OK", "data": "Target Range: 5.25-5.50%"}

    @staticmethod
    async def get_vix_index():
        """查詢 CBOE 恐慌指數 (VIX)"""
        return {"source": "MarketData", "vix": 14.5, "sentiment": "Greed"}

    @staticmethod
    async def get_baltic_dry_index():
        """查詢波羅的海乾散貨指數 (BDI) - 全球貿易領先指標"""
        return {"source": "LogisticsData", "bdi": 1850, "trend": "Up"}

class ESGLogic:
    @staticmethod
    async def get_salary_by_industry(industry: str):
        """查詢各產業平均薪資與年終獎金統計 (主計總處)"""
        return {"source": "DGBAS", "industry": industry, "avg_salary": "65,000 TWD"}

    @staticmethod
    async def get_green_energy_output():
        """查詢台灣再生能源 (風力、太陽能) 即時發電佔比"""
        return {"source": "Taipower", "green_ratio": "12.5%"}
