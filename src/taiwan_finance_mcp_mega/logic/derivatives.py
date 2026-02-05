"""
Derivatives & Futures Logic - v4.2.0
對接 臺灣期貨交易所 (Taifex) OpenAPI。
提供期貨、選擇權與三大法人留倉數據。
"""
import logging
from typing import Dict, Any, List, Optional
from taiwan_finance_mcp_mega.utils.http_client import AsyncHttpClient

logger = logging.getLogger("mcp-finance")

class DerivativesLogic:
    """
    處理期貨與衍生性商品數據。
    數據源：臺灣期貨交易所 (Taifex)。
    """
    TAIFEX_BASE = "https://openapi.taifex.com.tw/v1"

    @staticmethod
    async def get_futures_quotes() -> List[Dict[str, Any]]:
        """獲取期貨每日收盤行情 (DailyQuotes)。"""
        url = f"{DerivativesLogic.TAIFEX_BASE}/DailyQuotes"
        return await AsyncHttpClient.fetch_json(url)

    @staticmethod
    async def get_taifex_institutional_flow() -> List[Dict[str, Any]]:
        """獲取三大法人期貨交易量與未平倉量彙總 (InstitutionalInvestorsDaily)。"""
        url = f"{DerivativesLogic.TAIFEX_BASE}/InstitutionalInvestorsDaily"
        return await AsyncHttpClient.fetch_json(url)

    @staticmethod
    async def get_futures_oi_top_list() -> List[Dict[str, Any]]:
        """獲取期貨大額交易人未平倉部位統計。"""
        url = f"{DerivativesLogic.TAIFEX_BASE}/LargeTradersPositionsDaily"
        return await AsyncHttpClient.fetch_json(url)
