"""
專業匯率與大宗商品邏輯模組 (Logic Module for Forex and Commodities) - v4.0.0
對接 即匯站 (tw.rter.info) API，支援 OOO to OOO 匯率換算。
"""
import logging
from typing import Dict, Any, Optional
from taiwan_finance_mcp_mega.config import Config
from taiwan_finance_mcp_mega.utils.http_client import AsyncHttpClient

logger = logging.getLogger("mcp-finance")

class ForexLogic:
    """
    提供全球匯率換算與行情，數據源自 tw.rter.info。
    """

    @staticmethod
    async def get_latest_rates_raw() -> Dict[str, Any]:
        """
        獲取 tw.rter.info 的原始匯率數據 (以 USD 為基準)。
        """
        return await AsyncHttpClient.fetch_json(Config.FOREX_API)

    @classmethod
    async def get_pair(cls, base: str, target: str = "TWD") -> Dict[str, Any]:
        """
        計算並獲取特定貨幣對的即時匯率 (OOO to OOO)。
        
        解釋：執行精確的交叉換算邏輯，獲取當下市場的即時匯率。
        輸入 (Input)：
            base (str): 原始幣別 (如 'JPY', 'EUR', 'USD')。
            target (str): 目標幣別 (如 'TWD', 'HKD')。
        輸出 (Output)：
            Dict[str, Any]: 包含 pair, rate, source 與 update_time。
        """
        data = await cls.get_latest_rates_raw()
        if not data or not isinstance(data, dict):
            return {"error": "無法獲取匯率數據"}
        
        base = base.upper()
        target = target.upper()
        
        try:
            # 取得基準匯率 (相對於 USD)
            # tw.rter.info 格式為 "USDXXX"
            usd_base_key = f"USD{base}"
            usd_target_key = f"USD{target}"
            
            rate_to_usd_base = 1.0 if base == "USD" else data.get(usd_base_key, {}).get("Exrate")
            rate_to_usd_target = 1.0 if target == "USD" else data.get(usd_target_key, {}).get("Exrate")
            
            if rate_to_usd_base is None:
                return {"error": f"不支援的原始幣別: {base}"}
            if rate_to_usd_target is None:
                return {"error": f"不支援的目標幣別: {target}"}
                
            # 換算公式: 1 Base = (1/rate_to_usd_base) USD = (rate_to_usd_target / rate_to_usd_base) Target
            final_rate = rate_to_usd_target / rate_to_usd_base
            
            return {
                "pair": f"{base}/{target}",
                "rate": round(final_rate, 6),
                "update_time": data.get(usd_target_key if target != "USD" else usd_base_key, {}).get("UTC"),
                "source": "tw.rter.info (即匯站)",
                "note": "數據經由 USD 交叉換算得出。"
            }
        except Exception as e:
            logger.error(f"Forex calculation error: {str(e)}")
            return {"error": f"匯率計算失敗: {str(e)}"}

    @staticmethod
    async def get_latest_rates(base: str = "USD") -> Dict[str, Any]:
        """
        [Legacy Support] 獲取全球即時匯率表。
        """
        data = await ForexLogic.get_latest_rates_raw()
        if base.upper() == "USD":
            return data
        
        # 轉換為以 base 為基準的表
        base = base.upper()
        usd_base_key = f"USD{base}"
        rate_to_usd_base = 1.0 if base == "USD" else data.get(usd_base_key, {}).get("Exrate")
        
        if not rate_to_usd_base:
            return {"error": f"不支援的基準幣別: {base}"}
            
        converted_rates = {}
        for key, val in data.items():
            if key.startswith("USD"):
                currency = key[3:]
                converted_rates[currency] = round(val["Exrate"] / rate_to_usd_base, 6)
                
        return {
            "base": base,
            "rates": converted_rates,
            "source": "tw.rter.info (Cross-rate calculation)"
        }
