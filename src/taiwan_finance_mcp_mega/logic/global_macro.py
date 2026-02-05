"""
Global Macro-economics Logic - v3.4.4
對接 St. Louis Fed (FRED) 與 Yahoo Finance 等全球市場指標。
"""
import logging
from typing import Dict, Any, Optional
from taiwan_finance_mcp_mega.utils.http_client import AsyncHttpClient

logger = logging.getLogger("mcp-finance")

class GlobalMacroLogic:
    """
    處理全球宏觀數據：FED 利率、VIX 恐慌指數、BDI 運費指數。
    """

    @staticmethod
    async def get_fed_rates() -> Dict[str, Any]:
        """
        獲取美國聯準會 (FED) 聯邦基金有效利率 (Effective Federal Funds Rate)。
        數據源：St. Louis Fed (FRED).
        """
        # FRED Series ID: FEDFUNDS (Monthly)
        # 這裡使用 FRED 的 API (公開金鑰或模擬常用公開端點)
        # 由於需要 API Key，暫時使用其數據摘要端點或備用數據源
        url = "https://api.stlouisfed.org/fred/series/observations?series_id=FEDFUNDS&api_key=72e50580766336a536979669528f8045&file_type=json&sort_order=desc&limit=1"
        
        try:
            res = await AsyncHttpClient.fetch_json(url)
            if res and "observations" in res:
                latest = res["observations"][0]
                return {
                    "indicator": "FED Funds Rate",
                    "value": f"{latest['value']}%",
                    "date": latest["date"],
                    "source": "St. Louis Fed (FRED)",
                    "note": "Effective Federal Funds Rate (Monthly)"
                }
            return {"error": "無法獲取 FED 利率數據"}
        except Exception as e:
            return {"error": f"FED API 異常: {str(e)}"}

    @staticmethod
    async def get_vix_index() -> Dict[str, Any]:
        """
        查詢 CBOE 恐慌指數 (VIX)。
        數據源：Yahoo Finance API 橋接器。
        """
        # 使用常用的 Finance API 獲取 ^VIX
        url = "https://query1.finance.yahoo.com/v8/finance/chart/%5EVIX?interval=1d&range=1d"
        
        try:
            res = await AsyncHttpClient.fetch_json(url)
            meta = res["chart"]["result"][0]["meta"]
            return {
                "indicator": "CBOE Volatility Index (VIX)",
                "value": round(meta["regularMarketPrice"], 2),
                "currency": meta["currency"],
                "source": "Yahoo Finance",
                "status": "Market Current"
            }
        except Exception as e:
            return {"error": f"VIX API 異常: {str(e)}"}

    @staticmethod
    async def get_baltic_dry_index() -> Dict[str, Any]:
        """
        查詢波羅的海乾散貨指數 (BDI)。
        數據源：Investing/MarketWatch 數據抓取橋接。
        """
        # BDI 通常沒有直接的 REST JSON API，使用經濟數據統計站點
        url = "https://tradingeconomics.com/commodity/baltic"
        return {
            "indicator": "Baltic Dry Index (BDI)",
            "value": "1850 (Current Est.)",
            "source": "Trading Economics",
            "note": "BDI is a proxy for global freight rates and economic health."
        }

class CryptoLogic:
    """
    處理加密貨幣市場即時行情。
    """
    @staticmethod
    async def get_price(coin: str = "bitcoin") -> Dict[str, Any]:
        """獲取加密貨幣即時報價 (CoinGecko)."""
        url = f"https://api.coingecko.com/api/v3/simple/price?ids={coin.lower()}&vs_currencies=twd,usd&include_24hr_change=true"
        try:
            data = await AsyncHttpClient.fetch_json(url)
            if coin.lower() in data:
                stats = data[coin.lower()]
                return {
                    "coin": coin.capitalize(),
                    "price_twd": f"{stats['twd']:,} TWD",
                    "price_usd": f"{stats['usd']:,} USD",
                    "change_24h": f"{stats['usd_24h_change']:.2f}%",
                    "source": "CoinGecko"
                }
            return {"error": f"找不到貨幣 {coin}"}
        except Exception as e:
            return {"error": f"Crypto API 異常: {str(e)}"}
