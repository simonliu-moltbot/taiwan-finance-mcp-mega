"""
匯率與大宗商品邏輯模組 (Logic Module for Forex and Commodities)
對接 即時匯率 API 與 國際行情數據。
"""
from typing import Dict, Any, Optional
from taiwan_finance_mcp_mega.config import Config
from taiwan_finance_mcp_mega.utils.http_client import AsyncHttpClient

class ForexLogic:
    """
    提供全球匯率對台幣 (TWD) 的即時換算與分析。
    """

    @staticmethod
    async def get_latest_rates() -> Dict[str, Any]:
        """
        獲取日幣 (JPY) 為基準的所有即時匯率表。
        """
        return await AsyncHttpClient.fetch_json(Config.FOREX_API)

    @classmethod
    async def get_pair(cls, base: str, target: str = "TWD") -> Dict[str, Any]:
        """
        計算特定貨幣對的即時匯率。
        
        Args:
            base (str): 原始幣別代碼 (如 'USD', 'JPY', 'EUR')。
            target (str): 目標幣別代碼。預設為 'TWD'。
            
        Returns:
            Dict[str, Any]: 包含匯率數值與來源資訊。
        """
        data = await cls.get_latest_rates()
        if "error" in data:
            return data
        
        rates = data.get("rates", {})
        try:
            # 由於來源 API 以 JPY 為基準，需進行交叉換算
            jpy_to_target = rates.get(target)
            jpy_to_base = rates.get(base)
            
            if not jpy_to_target or not jpy_to_base:
                return {"error": f"不支援的幣別對: {base}/{target}"}
                
            rate = jpy_to_target / jpy_to_base
            return {
                "pair": f"{base}/{target}",
                "rate": round(rate, 4),
                "source": "Real-time ExchangeRate-API",
                "info": f"1 {base} 約可兌換 {round(rate, 2)} {target}"
            }
        except Exception as e:
            return {"error": f"匯率換算異常: {str(e)}"}
