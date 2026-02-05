"""
專業台股市場數據邏輯模組 (Logic Module for Taiwan Stock Market) - v3.4.0
對接 臺灣證券交易所 (TWSE) 與 證券櫃檯買賣中心 (TPEx) 的實時 OpenAPI。
符合 MLOps 規格之詳細文件化版本。
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
        內部數據過濾引擎。
        
        功能：從大量 API 回傳數據中根據代碼精確過濾。
        輸入 (Input)：
            url (str): 目標 API 端點。
            symbol (Optional[str]): 股票代碼 (例如 '2330')。
            code_key (str): 原始 JSON 中代表代碼的 Key。
        輸出 (Output)：
            List[Dict]: 過濾後的 JSON 列表。
        """
        data = await AsyncHttpClient.fetch_json(url)
        if not isinstance(data, list):
            return []
        
        if symbol:
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
        獲取上市個股當日即時行情。
        
        解釋：獲取集中市場所有個股在交易日當下的最新報價、漲跌幅度及成交量。
        使用時機：交易時段 (09:00 - 13:30) 獲取最新動態；收盤後獲取今日總結。
        輸入 (Input)：
            symbol (str): 股票代碼，如 '2330'。留空則獲取全市場。
        輸出 (Output)：
            List[Dict]: 包含 id, name, price, change, volume, open, high, low 等。
        """
        url = f"{Config.TWSE_BASE}/exchangeReport/STOCK_DAY_ALL"
        return await StockLogic._fetch_and_filter(url, symbol)

    @staticmethod
    async def get_odd_lot_quotes(symbol: Optional[str] = None) -> List[Dict[str, Any]]:
        """
        獲取盤中零股交易即時行情。
        
        解釋：專為小資族設計，查詢非張數交易（1-999股）的即時撮合價格。
        使用時機：當使用者想以較低金額參與權值股投資時。
        輸入 (Input)：
            symbol (str): 股票代碼。
        輸出 (Output)：
            List[Dict]: 包含零股成交價、成交股數與買賣價量。
        """
        url = f"{Config.TWSE_BASE}/exchangeReport/TWT53U"
        return await StockLogic._fetch_and_filter(url, symbol)

    # --- 2. 財務類 (Financials) ---

    @staticmethod
    async def get_eps_ranking(symbol: Optional[str] = None) -> List[Dict[str, Any]]:
        """
        查詢上市公司每股盈餘 (EPS) 排名。
        
        解釋：從官方數據中提取各公司的季度/年度獲利能力指標。
        使用時機：進行基本面分析、比較同產業獲利能力時。
        輸入 (Input)：
            symbol (str): 公司代號。
        輸出 (Output)：
            List[Dict]: 包含 year, quarter, name, eps (基本每股盈餘) 等欄位。
        """
        url = f"{Config.TWSE_BASE}/opendata/t187ap14_L"
        return await StockLogic._fetch_and_filter(url, symbol, "公司代號")

    @staticmethod
    async def get_dividend_yield(symbol: Optional[str] = None) -> List[Dict[str, Any]]:
        """
        查詢個股殖利率、本益比及淨值比。
        
        解釋：提供估值核心三指標：Dividend Yield (%), PE ratio, PB ratio。
        使用時機：評估股價是否過高 (PE/PB) 以及長期存股價值 (Yield) 時。
        輸入 (Input)：
            symbol (str): 股票代碼。
        輸出 (Output)：
            List[Dict]: 包含 yield (殖利率), pe (本益比), pb (淨值比) 等數值。
        """
        url = f"{Config.TWSE_BASE}/exchangeReport/BWIBBU_d"
        return await StockLogic._fetch_and_filter(url, symbol)

    # --- 3. 籌碼類 (Chips) ---

    @staticmethod
    async def get_institutional_flow(symbol: Optional[str] = None) -> List[Dict[str, Any]]:
        """
        查詢三大法人買賣超動向。
        
        解釋：追蹤外資、投信、自營商在市場中的買進與賣出金額。
        使用時機：收盤後 (約 15:00 後) 觀察主力資金流向，判斷明日趨勢。
        輸入 (Input)：
            symbol (str): 選填。若提供則嘗試查詢個股法人明細（需特定日期）。
        輸出 (Output)：
            List[Dict]: 法人別、買進金額、賣出金額、買賣超合計。
        """
        if symbol:
            url = f"{Config.TWSE_BASE}/exchangeReport/T86" # 實際需配合日期參數
            return await StockLogic._fetch_and_filter(url, symbol)
        return await AsyncHttpClient.fetch_json(f"{Config.TWSE_BASE}/fund/BFI82U")

    # --- 4. 萬用接口 (Generic Engine) ---

    @staticmethod
    async def call_generic_api(endpoint: str, symbol: Optional[str] = None) -> Any:
        """
        根據動態端點調用證交所 300+ 個 API。
        
        解釋：此為核心分發接口，將 ID 映射至官方 Swagger 定義的任意端點。
        使用時機：當系統呼叫細分專業工具（如 ESG, 職安, 融資券）時。
        輸入 (Input)：
            endpoint (str): API 路徑 (例如 /opendata/t187ap46_L_1)。
            symbol (str): 過濾代碼。
        輸出 (Output)：
            Any: 由原始 API 回傳並經過欄位映射的 JSON 資料。
        """
        url = f"{Config.TWSE_BASE}{endpoint}"
        return await StockLogic._fetch_and_filter(url, symbol)
