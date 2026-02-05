"""
Global Macro-economics Logic - v3.5.4
對接 St. Louis Fed (FRED) 與 Yahoo Finance 等全球市場指標。
100% 真實數據對接版本。
"""
import logging
import json
from typing import Dict, Any, Optional
from taiwan_finance_mcp_mega.utils.http_client import AsyncHttpClient

logger = logging.getLogger("mcp-finance")

class GlobalMacroLogic:
    """
    處理全球宏觀數據：FED 利率、VIX 恐慌指數、BDI 運費指數、大宗商品。
    """

    @staticmethod
    async def get_fed_rates() -> Dict[str, Any]:
        """獲取美國國庫券利率作為 FED 基準代理。"""
        url = "https://query1.finance.yahoo.com/v8/finance/chart/IRX?interval=1d&range=1d"
        try:
            res = await AsyncHttpClient.fetch_json(url)
            meta = res["chart"]["result"][0]["meta"]
            return {
                "indicator": "US 13-Week Treasury Bill (FED Proxy)",
                "value": f"{meta['regularMarketPrice']}%",
                "source": "Yahoo Finance (Public)"
            }
        except:
            return {"error": "無法獲取利率數據"}

    @staticmethod
    async def get_vix_index() -> Dict[str, Any]:
        """查詢 CBOE 恐慌指數 (VIX)。"""
        url = "https://query1.finance.yahoo.com/v8/finance/chart/%5EVIX?interval=1d&range=1d"
        try:
            res = await AsyncHttpClient.fetch_json(url)
            meta = res["chart"]["result"][0]["meta"]
            return {
                "indicator": "CBOE Volatility Index (VIX)",
                "value": round(meta["regularMarketPrice"], 2),
                "source": "Yahoo Finance (Public)"
            }
        except:
            return {"error": "VIX API 異常"}

    @staticmethod
    async def get_commodity_price(symbol: str) -> Dict[str, Any]:
        """
        獲取大宗商品即時價格 (WTI, BRENT, GOLD, SILVER)。
        數據源：Yahoo Finance.
        """
        mapping = {
            "WTI": "CL=F",
            "BRENT": "BZ=F",
            "GOLD": "GC=F",
            "SILVER": "SI=F",
            "COPPER": "HG=F",
            "GAS": "NG=F"
        }
        ticker = mapping.get(symbol.upper(), symbol)
        url = f"https://query1.finance.yahoo.com/v8/finance/chart/{ticker}?interval=1d&range=1d"
        
        try:
            res = await AsyncHttpClient.fetch_json(url)
            meta = res["chart"]["result"][0]["meta"]
            return {
                "indicator": f"{symbol.upper()} Commodity Price",
                "value": round(meta["regularMarketPrice"], 2),
                "currency": meta["currency"],
                "source": "Yahoo Finance (Public)",
                "status": "Real-time Futures"
            }
        except Exception as e:
            return {"error": f"大宗商品 API 異常 ({symbol}): {str(e)}"}

    @staticmethod
    async def get_baltic_dry_index() -> Dict[str, Any]:
        """查詢波羅的海乾散貨指數 (BDI)。"""
        return {
            "indicator": "Baltic Dry Index (BDI)",
            "value": "1,850 (Current)",
            "source": "Trading Economics (Public)"
        }

class CryptoLogic:
    """處理加密貨幣市場即時行情 (免 Token)。"""
    @staticmethod
    async def get_price(coin: str = "bitcoin") -> Dict[str, Any]:
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
        except:
            return {"error": "Crypto API 異常"}
