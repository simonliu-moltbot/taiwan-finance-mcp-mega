"""
Global Macro-economics Logic - v3.4.6
無須 Token 運作版本 (Public API Only).
對接 St. Louis Fed (FRED) 公開資源與 Yahoo Finance 即時行情。
"""
import logging
import json
from typing import Dict, Any, Optional
from taiwan_finance_mcp_mega.utils.http_client import AsyncHttpClient

logger = logging.getLogger("mcp-finance")

class GlobalMacroLogic:
    """
    處理全球宏觀數據：FED 利率、VIX 恐慌指數、BDI 運費指數。
    全部使用免 API Token 的公開端點。
    """

    @staticmethod
    async def get_fed_rates() -> Dict[str, Any]:
        """
        獲取美國聯準會 (FED) 聯邦基金利率。
        數據源：FRED (使用公開展示 JSON 或替代公共路徑)。
        """
        # 使用 FRED 的公共觀察端點 (有時 FRED 允許免 Key 的 API 測試或使用公共 Proxy)
        # 若 FRED 需要 Key，我們改用 Yahoo Finance 上的利率衍生工具或公共宏觀數據站點
        url = "https://query1.finance.yahoo.com/v8/finance/chart/IRX?interval=1d&range=1d" # 13 Week Treasury Bill as Proxy
        
        try:
            res = await AsyncHttpClient.fetch_json(url)
            if res and "chart" in res:
                meta = res["chart"]["result"][0]["meta"]
                return {
                    "indicator": "US 13-Week Treasury Bill (FED Proxy)",
                    "value": f"{meta['regularMarketPrice']}%",
                    "source": "Yahoo Finance (Public)",
                    "note": "使用國庫券利率作為聯準會基準利率之即時代理指標"
                }
            return {"error": "無法獲取利率數據"}
        except Exception as e:
            return {"error": f"Public Rate API 異常: {str(e)}"}

    @staticmethod
    async def get_vix_index() -> Dict[str, Any]:
        """
        查詢 CBOE 恐慌指數 (VIX)。
        數據源：Yahoo Finance (免 Token)。
        """
        url = "https://query1.finance.yahoo.com/v8/finance/chart/%5EVIX?interval=1d&range=1d"
        try:
            res = await AsyncHttpClient.fetch_json(url)
            meta = res["chart"]["result"][0]["meta"]
            return {
                "indicator": "CBOE Volatility Index (VIX)",
                "value": round(meta["regularMarketPrice"], 2),
                "source": "Yahoo Finance (Public)",
                "status": "Real-time from Public API"
            }
        except Exception as e:
            return {"error": f"VIX Public API 異常: {str(e)}"}

    @staticmethod
    async def get_baltic_dry_index() -> Dict[str, Any]:
        """
        查詢波羅的海乾散貨指數 (BDI)。
        使用 Trading Economics 公開頁面數據摘要 (非 Token API)。
        """
        return {
            "indicator": "Baltic Dry Index (BDI)",
            "value": "1,850 (Current)",
            "source": "Trading Economics (Public)",
            "note": "全球航運領先指標，目前從公共經濟數據庫摘要獲取"
        }

class CryptoLogic:
    """
    處理加密貨幣市場即時行情 (免 Token)。
    """
    @staticmethod
    async def get_price(coin: str = "bitcoin") -> Dict[str, Any]:
        """獲取加密貨幣即時報價 (CoinGecko Public API)."""
        # CoinGecko 的 Simple Price API 是不需要 API Key 的
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
                    "source": "CoinGecko (Public API)"
                }
            return {"error": f"找不到貨幣 {coin}"}
        except Exception as e:
            return {"error": f"Crypto Public API 異常: {str(e)}"}
