"""
Stock Logic Module for Taiwan Market.
Provides methods to fetch data from TWSE and TPEx OpenAPI.
"""
from typing import Dict, Any, List
from taiwan_finance_mcp_mega.config import Config
from taiwan_finance_mcp_mega.utils.http_client import AsyncHttpClient

class StockLogic:
    @staticmethod
    async def get_day_all() -> List[Dict[str, Any]]:
        """
        獲取台灣證券交易所 (TWSE) 所有上市個股當日即時行情。
        
        Endpoint: /exchangeReport/STOCK_DAY_ALL
        
        Returns:
            List[Dict[str, Any]]: 包含所有上市個股當日成交價、開盤價、最高價、最低價等資訊的列表。
        """
        url = f"{Config.TWSE_BASE}/exchangeReport/STOCK_DAY_ALL"
        return await AsyncHttpClient.fetch_json(url)

    @staticmethod
    async def get_monthly_revenue() -> List[Dict[str, Any]]:
        """
        查詢公開發行公司每月營業收入彙總。
        
        Endpoint: /opendata/t187ap05_P
        
        Returns:
            List[Dict[str, Any]]: 各公司當月營收、上月營收及 YOY 成長數據。
        """
        url = f"{Config.TWSE_BASE}/opendata/t187ap05_P"
        return await AsyncHttpClient.fetch_json(url)

    @staticmethod
    async def get_eps_ranking() -> List[Dict[str, Any]]:
        """
        查詢上市公司每股盈餘 (EPS) 排名。
        
        Returns:
            List[Dict[str, Any]]: 按 EPS 獲利能力排序的公司名單。
        """
        url = f"{Config.TWSE_BASE}/opendata/t187ap14_L"
        return await AsyncHttpClient.fetch_json(url)
