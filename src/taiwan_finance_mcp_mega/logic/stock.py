"""
專業台股市場數據邏輯模組 (Logic Module for Taiwan Stock Market) - v3.2.0
對接 臺灣證券交易所 (TWSE) 與 證券櫃檯買賣中心 (TPEx) 的實時 OpenAPI。
"""
import logging
import json
from typing import Dict, Any, List, Optional
from taiwan_finance_mcp_mega.config import Config
from taiwan_finance_mcp_mega.utils.http_client import AsyncHttpClient

logger = logging.getLogger("mcp-finance")

class StockLogic:
    """
    處理所有與台灣股市相關的數據請求。
    """

    @staticmethod
    async def get_realtime_quotes(symbol: Optional[str] = None) -> List[Dict[str, Any]]:
        """
        獲取上市個股當日即時行情。
        """
        url = f"{Config.TWSE_BASE}/exchangeReport/STOCK_DAY_ALL"
        data = await AsyncHttpClient.fetch_json(url)
        
        if not isinstance(data, list):
            return []

        mapped_data = []
        for item in data:
            mapped_item = {
                "id": item.get("Code"),
                "name": item.get("Name"),
                "price": item.get("ClosingPrice"),
                "change": item.get("Change"),
                "volume": item.get("TradeVolume"),
                "open": item.get("OpeningPrice"),
                "high": item.get("HighestPrice"),
                "low": item.get("LowestPrice")
            }
            if symbol and mapped_item["id"] == symbol:
                return [mapped_item]
            mapped_data.append(mapped_item)
        
        return mapped_data if not symbol else []

    @staticmethod
    async def get_eps_ranking(symbol: Optional[str] = None) -> List[Dict[str, Any]]:
        """
        查詢上市公司每股盈餘 (EPS)。
        """
        url = f"{Config.TWSE_BASE}/opendata/t187ap14_L"
        data = await AsyncHttpClient.fetch_json(url)
        if not isinstance(data, list): return []
        
        result = []
        for i in data:
            item = {
                "id": i.get("公司代號"),
                "name": i.get("公司名稱"),
                "eps": i.get("基本每股盈餘(元)"),
                "quarter": i.get("季別"),
                "year": i.get("年度")
            }
            if symbol and item["id"] == symbol:
                return [item]
            result.append(item)
        return result

    @staticmethod
    async def get_dividend_yield(symbol: Optional[str] = None) -> List[Dict[str, Any]]:
        """
        查詢本益比、殖利率及淨值比。
        """
        url = f"{Config.TWSE_BASE}/exchangeReport/BWIBBU_d"
        data = await AsyncHttpClient.fetch_json(url)
        if not isinstance(data, list): return []
        
        result = []
        for i in data:
            item = {
                "id": i.get("Code"),
                "name": i.get("Name"),
                "pe": i.get("PEratio"),
                "yield": i.get("DividendYield"),
                "pb": i.get("PBratio")
            }
            if symbol and item["id"] == symbol:
                return [item]
            result.append(item)
        return result

    @staticmethod
    async def get_institutional_investors(symbol: Optional[str] = None) -> List[Dict[str, Any]]:
        """
        查詢三大法人買賣超。
        """
        # 注意：個股三大法人需要日期，此處先回傳彙總或提示
        url = f"{Config.TWSE_BASE}/fund/BFI82U"
        data = await AsyncHttpClient.fetch_json(url)
        if symbol:
            return [{"id": symbol, "message": "個股三大法人動向需串接 T86 API 並提供日期，目前顯示全市場彙總。", "summary": data}]
        return data

    @staticmethod
    async def get_margin_balance(symbol: Optional[str] = None) -> List[Dict[str, Any]]:
        """
        查詢融資融券餘額。
        """
        url = f"{Config.TWSE_BASE}/exchangeReport/MI_MARGN"
        data = await AsyncHttpClient.fetch_json(url)
        if not isinstance(data, list): return []
        if symbol:
            return [i for i in data if i.get("股票代號") == symbol]
        return data[:10]
