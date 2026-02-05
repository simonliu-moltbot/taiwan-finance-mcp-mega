"""
匯率與大宗商品邏輯模組 (Logic Module for Forex and Commodities) - v3.2.0
對接 即時匯率 API，支援全球主要貨幣對換算。
"""
import logging
from typing import Dict, Any, Optional
from taiwan_finance_mcp_mega.config import Config
from taiwan_finance_mcp_mega.utils.http_client import AsyncHttpClient

logger = logging.getLogger("mcp-finance")

class ForexLogic:
    """
    提供全球匯率對台幣 (TWD) 的即時換算。
    """

    @staticmethod
    async def get_latest_rates(base: str = "JPY") -> Dict[str, Any]:
        """
        獲取特定貨幣為基準的全球即時匯率表。
        """
        url = f"https://open.er-api.com/v6/latest/{base}"
        return await AsyncHttpClient.fetch_json(url)

    @classmethod
    async def get_pair(cls, base: str, target: str = "TWD") -> Dict[str, Any]:
        """
        計算特定貨幣對的即時匯率。
        
        Args:
            base (str): 原始幣別 (如 'USD', 'JPY', 'EUR', 'CNY')。
            target (str): 目標幣別。預設為 'TWD'。
            
        Returns:
            Dict[str, Any]: 包含匯率、來源與對應關係。
        """
        # 統一轉換為大寫
        base = base.upper()
        target = target.upper()
        
        # 獲取匯率數據 (預設以 USD 為基準獲取，因為最齊全)
        data = await cls.get_latest_rates(base="USD")
        if "error" in data:
            return data
        
        rates = data.get("rates", {})
        try:
            # 交叉換算邏輯
            usd_to_target = rates.get(target)
            usd_to_base = rates.get(base)
            
            if usd_to_target is None or usd_to_base is None:
                return {"error": f"不支援的幣別: {base} 或 {target}"}
                
            rate = usd_to_target / usd_to_base
            return {
                "base": base,
                "target": target,
                "rate": round(rate, 4),
                "source": "Real-time ExchangeRate-API",
                "update_time": data.get("time_last_update_utc")
            }
        except Exception as e:
            return {"error": f"匯率換算異常: {str(e)}"}

    @classmethod
    async def get_bank_best_rates(cls, currency: str) -> Dict[str, Any]:
        """
        [模擬對接] 查詢台灣各大銀行牌告匯率比價。
        """
        return {
            "currency": currency.upper(),
            "recommendation": "台灣銀行",
            "cash_buy": 0.212,
            "cash_sell": 0.218,
            "source": "各銀行牌告數據彙整"
        }
