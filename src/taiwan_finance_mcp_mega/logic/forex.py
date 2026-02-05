"""
專業匯率與大宗商品邏輯模組 (Logic Module for Forex and Commodities) - v3.4.0
對接 真實世界即時匯率 API，符合 MLOps 標準之註解規範。
"""
import logging
from typing import Dict, Any, Optional
from taiwan_finance_mcp_mega.config import Config
from taiwan_finance_mcp_mega.utils.http_client import AsyncHttpClient

logger = logging.getLogger("mcp-finance")

class ForexLogic:
    """
    提供全球匯率對台幣 (TWD) 的即時換算與行情。
    """

    @staticmethod
    async def get_latest_rates(base: str = "USD") -> Dict[str, Any]:
        """
        獲取全球即時匯率表。
        
        解釋：獲取以特定貨幣為基準（預設 USD）的所有全球主要貨幣最新行情。
        使用時機：需要一次對比多國幣別波動或進行多幣別資產計算時。
        輸入 (Input)：
            base (str): 基準幣別代碼，例如 'USD', 'JPY'。
        輸出 (Output)：
            Dict[str, Any]: 包含 rates 對應表的 JSON 數據。
        """
        url = f"https://open.er-api.com/v6/latest/{base.upper()}"
        return await AsyncHttpClient.fetch_json(url)

    @classmethod
    async def get_pair(cls, base: str, target: str = "TWD") -> Dict[str, Any]:
        """
        計算並獲取特定貨幣對的即時真實匯率。
        
        解釋：執行精確的交叉換算邏輯，獲取當下市場的即時匯率。
        使用時機：換匯決策、進出口成本估算或海外旅遊規劃。
        輸入 (Input)：
            base (str): 原始幣別 (如 'JPY', 'EUR', 'CNY')。
            target (str): 目標幣別。預設為台幣 'TWD'。
        輸出 (Output)：
            Dict[str, Any]: 包含 pair (貨幣對), rate (匯率數值), source (來源) 與 update_time。
        """
        data = await cls.get_latest_rates(base="USD")
        if "error" in data:
            return data
        
        rates = data.get("rates", {})
        try:
            val_target = rates.get(target.upper())
            val_base = rates.get(base.upper())
            
            if val_target is None or val_base is None:
                return {"error": f"不支援的幣別: {base}/{target}"}
                
            final_rate = val_target / val_base
            return {
                "pair": f"{base.upper()}/{target.upper()}",
                "rate": round(final_rate, 4),
                "last_update_utc": data.get("time_last_update_utc"),
                "source": "Real-time ExchangeRate-API (Market Mid-Rate)",
                "usage_tip": f"數據反映市場中間匯率，銀行現鈔買賣請參考牌告價。"
            }
        except Exception as e:
            return {"error": f"匯率計算失敗: {str(e)}"}
