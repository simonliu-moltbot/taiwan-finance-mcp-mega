"""
專業台股市場數據邏輯模組 (Logic Module for Taiwan Stock Market) - v3.3.5
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
        """
        內部通用數據抓取與符號過濾工具。
        
        Args:
            url (str): 目標 API 網址。
            symbol (Optional[str]): 股票代碼 (例如 '2330')。
            code_key (str): API 回傳欄位中代表代碼的鍵名。
            
        Returns:
            List[Dict[str, Any]]: 過濾或映射後的資料清單。
        """
        data = await AsyncHttpClient.fetch_json(url)
        if not isinstance(data, list):
            return []
        
        if symbol:
            # 支援多種常見的代碼欄位名稱 (Code, 公司代號, 股票代號, id)
            possible_keys = [code_key, "Code", "公司代號", "股票代號", "id", "STOCKsSecurityCode"]
            filtered = []
            for item in data:
                for pk in possible_keys:
                    val = item.get(pk)
                    if val and str(val).strip() == str(symbol).strip():
                        filtered.append(item)
                        break
            return filtered
        return data

    # --- 1. 行情類 (Market Quotes) ---

    @staticmethod
    async def get_realtime_quotes(symbol: Optional[str] = None) -> List[Dict[str, Any]]:
        """
        獲取上市個股當日即時行情 (STOCK_DAY_ALL)。
        包含：Code, Name, OpeningPrice, HighestPrice, LowestPrice, ClosingPrice, TradeVolume.
        """
        url = f"{Config.TWSE_BASE}/exchangeReport/STOCK_DAY_ALL"
        return await StockLogic._fetch_and_filter(url, symbol)

    @staticmethod
    async def get_odd_lot_quotes(symbol: Optional[str] = None) -> List[Dict[str, Any]]:
        """
        獲取集中市場盤中零股交易即時行情 (TWT53U)。
        """
        url = f"{Config.TWSE_BASE}/exchangeReport/TWT53U"
        return await StockLogic._fetch_and_filter(url, symbol)

    # --- 2. 財務類 (Financials) ---

    @staticmethod
    async def get_eps_ranking(symbol: Optional[str] = None) -> List[Dict[str, Any]]:
        """
        查詢上市公司每股盈餘 (EPS) 排名 (t187ap14_L)。
        包含：公司代號、名稱、年度、季別、基本每股盈餘(元)。
        """
        url = f"{Config.TWSE_BASE}/opendata/t187ap14_L"
        return await StockLogic._fetch_and_filter(url, symbol, "公司代號")

    @staticmethod
    async def get_dividend_yield(symbol: Optional[str] = None) -> List[Dict[str, Any]]:
        """
        查詢上市公司日本益比、殖利率及股價淨值比 (BWIBBU_d)。
        """
        url = f"{Config.TWSE_BASE}/exchangeReport/BWIBBU_d"
        return await StockLogic._fetch_and_filter(url, symbol)

    @staticmethod
    async def get_monthly_revenue(symbol: Optional[str] = None) -> List[Dict[str, Any]]:
        """
        查詢上市櫃公司每月營業收入彙總表 (t187ap05_L / t187ap05_P)。
        """
        url = f"{Config.TWSE_BASE}/opendata/t187ap05_L"
        return await StockLogic._fetch_and_filter(url, symbol, "公司代號")

    # --- 3. 籌碼類 (Chips) ---

    @staticmethod
    async def get_institutional_flow(symbol: Optional[str] = None) -> List[Dict[str, Any]]:
        """
        查詢三大法人買賣超動向。
        個股動向需對接 T86 (需要日期參數)，彙總對接 BFI82U。
        """
        if symbol:
            # 嘗試使用個股日報路徑 (此處為示意，T86 實務上需日期)
            url = f"{Config.TWSE_BASE}/exchangeReport/T86"
            return await StockLogic._fetch_and_filter(url, symbol)
        return await AsyncHttpClient.fetch_json(f"{Config.TWSE_BASE}/fund/BFI82U")

    @staticmethod
    async def get_margin_balance(symbol: Optional[str] = None) -> List[Dict[str, Any]]:
        """
        查詢全市場融資融券餘額 (MI_MARGN)。
        """
        url = f"{Config.TWSE_BASE}/exchangeReport/MI_MARGN"
        return await StockLogic._fetch_and_filter(url, symbol, "股票代號")

    # --- 4. 萬用對接接口 (The Master Bridge) ---

    @staticmethod
    async def call_generic_api(endpoint: str, symbol: Optional[str] = None) -> Any:
        """
        根據 Endpoint 動態調用 300+ 個證交所 API。
        自動執行 symbol 過濾與異常處理。
        """
        url = f"{Config.TWSE_BASE}{endpoint}"
        return await StockLogic._fetch_and_filter(url, symbol)
