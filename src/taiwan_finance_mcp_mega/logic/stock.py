"""
專業台股市場數據邏輯模組 (Logic Module for Taiwan Stock Market) - v3.3.0
對接 臺灣證券交易所 (TWSE) 與 證券櫃檯買賣中心 (TPEx) 的 100+ 個實時 OpenAPI。
"""
import logging
from typing import Dict, Any, List, Optional
from taiwan_finance_mcp_mega.config import Config
from taiwan_finance_mcp_mega.utils.http_client import AsyncHttpClient

logger = logging.getLogger("mcp-finance")

class StockLogic:
    """
    處理所有與台灣股市相關的數據請求。
    包含核心行情、財務、籌碼、ESG 及公告數據。
    """

    @staticmethod
    async def _fetch_and_filter(url: str, symbol: Optional[str] = None, code_key: str = "Code") -> List[Dict[str, Any]]:
        """內部通用抓取與過濾工具"""
        data = await AsyncHttpClient.fetch_json(url)
        if not isinstance(data, list):
            return []
        if symbol:
            # 支援多種常見的 Code 鍵名 (Code, 公司代號, id)
            return [i for i in data if str(i.get(code_key, i.get("公司代號", i.get("id")))) == symbol]
        return data

    # --- 1. 行情類 (Market Quotes) ---

    @staticmethod
    async def get_realtime_quotes(symbol: Optional[str] = None) -> List[Dict[str, Any]]:
        """獲取上市個股當日即時行情 (STOCK_DAY_ALL)"""
        url = f"{Config.TWSE_BASE}/exchangeReport/STOCK_DAY_ALL"
        return await StockLogic._fetch_and_filter(url, symbol)

    @staticmethod
    async def get_odd_lot_quotes(symbol: Optional[str] = None) -> List[Dict[str, Any]]:
        """獲取盤中零股交易即時行情 (TWT53U)"""
        url = f"{Config.TWSE_BASE}/exchangeReport/TWT53U"
        return await StockLogic._fetch_and_filter(url, symbol)

    @staticmethod
    async def get_after_hours_trading(symbol: Optional[str] = None) -> List[Dict[str, Any]]:
        """獲取盤後定價交易資訊 (BFT41U)"""
        url = f"{Config.TWSE_BASE}/exchangeReport/BFT41U"
        return await StockLogic._fetch_and_filter(url, symbol)

    # --- 2. 財務類 (Financials) ---

    @staticmethod
    async def get_eps_ranking(symbol: Optional[str] = None) -> List[Dict[str, Any]]:
        """查詢上市公司每股盈餘 (EPS) 排名 (t187ap14_L)"""
        url = f"{Config.TWSE_BASE}/opendata/t187ap14_L"
        return await StockLogic._fetch_and_filter(url, symbol, "公司代號")

    @staticmethod
    async def get_monthly_revenue(symbol: Optional[str] = None) -> List[Dict[str, Any]]:
        """查詢上市櫃公司每月營業收入 (t187ap05_L)"""
        url = f"{Config.TWSE_BASE}/opendata/t187ap05_L"
        return await StockLogic._fetch_and_filter(url, symbol, "公司代號")

    @staticmethod
    async def get_dividend_yield(symbol: Optional[str] = None) -> List[Dict[str, Any]]:
        """查詢個股日本益比、殖利率及淨值比 (BWIBBU_d)"""
        url = f"{Config.TWSE_BASE}/exchangeReport/BWIBBU_d"
        return await StockLogic._fetch_and_filter(url, symbol)

    # --- 3. 籌碼類 (Chips & Institutional) ---

    @staticmethod
    async def get_institutional_investors() -> List[Dict[str, Any]]:
        """查詢三大法人買賣超彙總 (BFI82U)"""
        url = f"{Config.TWSE_BASE}/fund/BFI82U"
        return await AsyncHttpClient.fetch_json(url)

    @staticmethod
    async def get_margin_balance(symbol: Optional[str] = None) -> List[Dict[str, Any]]:
        """查詢全市場融資融券餘額 (MI_MARGN)"""
        url = f"{Config.TWSE_BASE}/exchangeReport/MI_MARGN"
        return await StockLogic._fetch_and_filter(url, symbol, "股票代號")

    # --- 4. ESG 與 公司治理 (Governance) ---

    @staticmethod
    async def get_esg_safety(symbol: Optional[str] = None) -> List[Dict[str, Any]]:
        """查詢上市公司企業 ESG - 職業安全衛生資料 (t187ap46_L_21)"""
        url = f"{Config.TWSE_BASE}/opendata/t187ap46_L_21"
        return await StockLogic._fetch_and_filter(url, symbol, "公司代號")

    @staticmethod
    async def get_esg_ghg_emissions(symbol: Optional[str] = None) -> List[Dict[str, Any]]:
        """查詢上市公司企業 ESG - 溫室氣體排放 (t187ap46_L_1)"""
        url = f"{Config.TWSE_BASE}/opendata/t187ap46_L_1"
        return await StockLogic._fetch_and_filter(url, symbol, "公司代號")

    # --- 5. 其他專業 API (Generic Porting for 100+ Endpoints) ---

    @staticmethod
    async def call_generic_api(endpoint: str, symbol: Optional[str] = None) -> Any:
        """
        萬用接口：根據傳入的 endpoint 動態呼叫證交所 API。
        支援 server.py 中定義的數百種工具路由。
        """
        url = f"{Config.TWSE_BASE}{endpoint}"
        return await StockLogic._fetch_and_filter(url, symbol)
