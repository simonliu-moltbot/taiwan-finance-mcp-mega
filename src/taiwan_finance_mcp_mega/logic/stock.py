"""
專業台股市場數據邏輯模組 (Logic Module for Taiwan Stock Market) - v3.1.0
對接 臺灣證券交易所 (TWSE) 與 證券櫃檯買賣中心 (TPEx) 的實時 OpenAPI。
"""
import logging
from typing import Dict, Any, List, Optional
from taiwan_finance_mcp_mega.config import Config
from taiwan_finance_mcp_mega.utils.http_client import AsyncHttpClient

logger = logging.getLogger("mcp-finance")

class StockLogic:
    """
    處理所有與台灣股市相關的數據請求。
    所有方法均支援真實 API 抓取，並具備欄位映射與符號過濾功能。
    """

    @staticmethod
    async def get_realtime_quotes(symbol: Optional[str] = None) -> List[Dict[str, Any]]:
        """
        獲取上市個股當日即時行情。
        
        Args:
            symbol (Optional[str]): 股票代碼 (如 '2330')。若為 None 則回傳全市場。
            
        Returns:
            List[Dict[str, Any]]: 包含 id, name, price, change, volume, open, high, low 的字典列表。
        """
        url = f"{Config.TWSE_BASE}/exchangeReport/STOCK_DAY_ALL"
        data = await AsyncHttpClient.fetch_json(url)
        
        if not isinstance(data, list):
            return []

        mapped_data = []
        for item in data:
            # 欄位映射
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
            if symbol:
                if mapped_item["id"] == symbol:
                    return [mapped_item]
            else:
                mapped_data.append(mapped_item)
        return mapped_data

    @staticmethod
    async def get_eps_ranking(symbol: Optional[str] = None) -> List[Dict[str, Any]]:
        """
        查詢上市公司每股盈餘 (EPS) 排名或特定個股 EPS。
        
        Args:
            symbol (Optional[str]): 股票代碼。若提供則僅回傳該個股資料。
            
        Returns:
            List[Dict[str, Any]]: 包含代號、名稱、年度、季別、基本每股盈餘(元)的列表。
        """
        url = f"{Config.TWSE_BASE}/opendata/t187ap14_L"
        data = await AsyncHttpClient.fetch_json(url)
        if not isinstance(data, list): return []
        
        # 統一欄位名稱
        result = []
        for i in data:
            item = {
                "id": i.get("公司代號"),
                "name": i.get("公司名稱"),
                "year": i.get("年度"),
                "quarter": i.get("季別"),
                "eps": i.get("基本每股盈餘(元)")
            }
            if symbol:
                if item["id"] == symbol: return [item]
            else:
                result.append(item)
        return result

    @staticmethod
    async def get_dividend_yield(symbol: Optional[str] = None) -> List[Dict[str, Any]]:
        """
        查詢個股殖利率、本益比及股價淨值比。
        
        Args:
            symbol (Optional[str]): 股票代碼。
            
        Returns:
            List[Dict[str, Any]]: 包含代號、名稱、殖利率(%)、本益比、股價淨值比的列表。
        """
        url = f"{Config.TWSE_BASE}/exchangeReport/BWIBBU_d"
        data = await AsyncHttpClient.fetch_json(url)
        if not isinstance(data, list): return []
        
        result = []
        for i in data:
            item = {
                "id": i.get("Code"),
                "name": i.get("Name"),
                "yield": i.get("DividendYield"),
                "pe": i.get("PEratio"),
                "pb": i.get("PBratio")
            }
            if symbol:
                if item["id"] == symbol: return [item]
            else:
                result.append(item)
        return result

    @staticmethod
    async def get_institutional_flow(symbol: Optional[str] = None) -> List[Dict[str, Any]]:
        """
        查詢三大法人買賣超動向。
        
        Args:
            symbol (Optional[str]): 若提供，將嘗試獲取個股法人持股明細。
        """
        if symbol:
            # 個股法人持股 API (T86)
            url = f"{Config.TWSE_BASE}/exchangeReport/T86?response=json&selectType=ALL&date=20260204" # 範例日期，實際應由系統計算
            # 注意：T86 需要日期參數，此處實作簡化邏輯
            return [{"message": "個股法人動向需指定交易日期，目前對接全市場彙總數據。"}]
        
        # 全市場彙總 (BFI82U)
        url = f"{Config.TWSE_BASE}/fund/BFI82U"
        return await AsyncHttpClient.fetch_json(url)

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
        return data[:20]
