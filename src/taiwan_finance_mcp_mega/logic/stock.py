"""
專業台股市場數據邏輯模組 (Logic Module for Taiwan Stock Market)
對接 臺灣證券交易所 (TWSE) 與 證券櫃檯買賣中心 (TPEx) 的 OpenAPI。
"""
from typing import Dict, Any, List, Optional
from taiwan_finance_mcp_mega.config import Config
from taiwan_finance_mcp_mega.utils.http_client import AsyncHttpClient

class StockLogic:
    """
    處理所有與台灣股市相關的數據請求與格式化。
    """

    @staticmethod
    async def get_realtime_quotes(symbol: Optional[str] = None) -> List[Dict[str, Any]]:
        """
        獲取上市個股當日即時行情。
        
        Args:
            symbol (Optional[str]): 股票代碼 (如 '2330')。若為 None 則回傳全市場。
            
        Returns:
            List[Dict[str, Any]]: 包含代碼、名稱、成交價、漲跌、成交量等映射後的資料。
        """
        url = f"{Config.TWSE_BASE}/exchangeReport/STOCK_DAY_ALL"
        data = await AsyncHttpClient.fetch_json(url)
        
        if not isinstance(data, list):
            return []

        # 映射原始欄位到好懂的名稱
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
            if symbol:
                if mapped_item["id"] == symbol:
                    return [mapped_item]
            else:
                mapped_data.append(mapped_item)
        
        return mapped_data

    @staticmethod
    async def get_institutional_investors() -> List[Dict[str, Any]]:
        """
        查詢三大法人買賣超彙總。
        
        Returns:
            List[Dict[str, Any]]: 法人別、買進金額、賣出金額、買賣超金額。
        """
        url = f"{Config.TWSE_BASE}/fund/BFI82U"
        return await AsyncHttpClient.fetch_json(url)

    @staticmethod
    async def get_eps_ranking() -> List[Dict[str, Any]]:
        """
        獲取上市公司每股盈餘 (EPS) 排名。
        
        Returns:
            List[Dict[str, Any]]: 包含公司名稱、年度、季別、EPS 等資訊。
        """
        url = f"{Config.TWSE_BASE}/opendata/t187ap14_L"
        return await AsyncHttpClient.fetch_json(url)

    @staticmethod
    async def get_dividend_policy(symbol: str) -> List[Dict[str, Any]]:
        """
        查詢特定個股的股利分派情形。
        
        Args:
            symbol (str): 股票代碼。
        """
        url = f"{Config.TWSE_BASE}/opendata/t187ap45_L"
        data = await AsyncHttpClient.fetch_json(url)
        if isinstance(data, list):
            return [i for i in data if i.get("公司代號") == symbol]
        return []

    @staticmethod
    async def get_monthly_revenue(symbol: Optional[str] = None) -> List[Dict[str, Any]]:
        """
        查詢上市櫃公司每月營業收入彙總。
        
        Args:
            symbol (Optional[str]): 股票代碼。
        """
        url = f"{Config.TWSE_BASE}/opendata/t187ap05_P"
        data = await AsyncHttpClient.fetch_json(url)
        if symbol and isinstance(data, list):
            return [i for i in data if i.get("公司代號") == symbol]
        return data
