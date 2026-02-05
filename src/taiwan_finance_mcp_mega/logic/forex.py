"""
專業匯率與大宗商品邏輯模組 (Logic Module for Forex and Commodities) - v3.3.3
對接 真實世界即時匯率 API，支援全球 160+ 貨幣對台幣之精確換算。
數據來源：ExchangeRate-API (實時市場價).
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
    async def get_latest_rates(base: str = "USD") -> Dict[str, Any]:
        """
        獲取以特定貨幣為基準的全球即時匯率表。
        
        Args:
            base (str): 基準貨幣代碼。預設使用 USD 以獲得最完整數據。
            
        Returns:
            Dict[str, Any]: 包含所有支援貨幣匯率的字典。
        """
        url = f"https://open.er-api.com/v6/latest/{base.upper()}"
        return await AsyncHttpClient.fetch_json(url)

    @classmethod
    async def get_pair(cls, base: str, target: str = "TWD") -> Dict[str, Any]:
        """
        計算並獲取特定貨幣對的即時真實匯率。
        
        Args:
            base (str): 原始幣別 (如 'JPY', 'EUR', 'CNY', 'HKD')。
            target (str): 目標幣別。預設為台幣 'TWD'。
            
        Returns:
            Dict[str, Any]: 包含換算匯率、更新時間與來源說明。
        """
        # 1. 獲取基準數據
        data = await cls.get_latest_rates(base="USD")
        if "error" in data:
            return data
        
        rates = data.get("rates", {})
        try:
            # 2. 執行交叉換算 (Cross Rate Calculation)
            val_target = rates.get(target.upper())
            val_base = rates.get(base.upper())
            
            if val_target is None or val_base is None:
                return {
                    "error": f"不支援的幣別轉換: {base}/{target}",
                    "supported_examples": ["USD", "JPY", "EUR", "CNY", "HKD", "GBP", "AUD"]
                }
                
            final_rate = val_target / val_base
            
            return {
                "pair": f"{base.upper()}/{target.upper()}",
                "rate": round(final_rate, 4),
                "last_update_utc": data.get("time_last_update_utc"),
                "next_update_utc": data.get("time_next_update_utc"),
                "source": "Real-time ExchangeRate-API (Market Spot Rate)",
                "note": f"目前 1 {base.upper()} 可兌換約 {round(final_rate, 2)} {target.upper()}"
            }
        except Exception as e:
            logger.error(f"Forex calculation failed: {str(e)}")
            return {"error": f"匯率計算發生異常: {str(e)}"}
