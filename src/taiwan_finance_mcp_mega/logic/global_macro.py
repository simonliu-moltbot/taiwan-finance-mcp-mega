"""
Global Macro-economics Logic - v4.1.0
100% 真實數據對接版本。
移除 VIX 與 FED 指標，專注於原油與 Crypto。
"""
import logging
import json
from typing import Dict, Any, Optional
from taiwan_finance_mcp_mega.utils.http_client import AsyncHttpClient

logger = logging.getLogger("mcp-finance")

class GlobalMacroLogic:
    """
    處理全球宏觀數據：大宗商品與加密貨幣。
    """

    @staticmethod
    async def get_commodity_price(symbol: str) -> Dict[str, Any]:
        """
        [v3.9.2] 獲取國際原油價格。
        數據源：經濟部能源署 (NID: 6029)。
        """
        # 經濟部能源署 - 國際原油價格 (CSV 下載)
        url = "https://www2.moeaea.gov.tw/oil111/csv/GlobalOilOpenData.csv"
        
        try:
            data = await AsyncHttpClient.fetch_csv_as_json(url)
            if not data:
                return {"error": "無法從經濟部能源署獲取數據", "status": "maintenance"}
            
            latest = data[0]
            mapping = {
                "WTI": {"key": "西德州(美元/桶)", "name": "WTI Crude Oil"},
                "BRENT": {"key": "布蘭特(美元/桶)", "name": "Brent Crude Oil"},
                "DUBAI": {"key": "杜拜(美元/桶)", "name": "Dubai Crude Oil"}
            }
            
            info = mapping.get(symbol.upper())
            if info:
                return {
                    "indicator": info["name"],
                    "value": f"{latest.get(info['key'], 'N/A')} USD",
                    "period": latest.get("日期", "N/A"),
                    "source": "經濟部能源署 (MOEA)",
                    "status": "Authentic Government Data"
                }
            return {"error": f"不支援的油價指標: {symbol}"}
        except Exception as e:
            logger.error(f"Oil Price Sync Error: {str(e)}")
            return {"error": "數據解析異常", "status": "maintenance"}

class CryptoLogic:
    """處理加密貨幣市場即時行情 (免 Token)。"""
    @staticmethod
    async def get_price(coin: str = "bitcoin") -> Dict[str, Any]:
        coin_map = {"BTC": "bitcoin", "ETH": "ethereum", "SOL": "solana"}
        coin_id = coin_map.get(coin.upper(), coin.lower())
        url = f"https://api.coingecko.com/api/v3/simple/price?ids={coin_id}&vs_currencies=twd,usd&include_24hr_change=true"
        try:
            data = await AsyncHttpClient.fetch_json(url)
            if coin_id in data:
                stats = data[coin_id]
                return {
                    "coin": coin_id.capitalize(),
                    "price_twd": f"{stats['twd']:,} TWD",
                    "price_usd": f"{stats['usd']:,} USD",
                    "change_24h": f"{stats['usd_24h_change']:.2f}%",
                    "source": "CoinGecko (Public API)"
                }
            return {"error": f"找不到貨幣 {coin}"}
        except:
            return {"error": "Crypto API 異常"}
