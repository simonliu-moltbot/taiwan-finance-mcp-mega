"""
Taiwan Macro-economics & Gov Data Logic - v3.9.4
對接穩定性強化：正式切換至勞動部年度指標 API (NID: 130489)。
解決 NID 6647 連結不穩定導致的數據抓取失敗問題。
"""
import logging
import json
from datetime import datetime
import pytz
from typing import Dict, Any, List, Optional
from taiwan_finance_mcp_mega.utils.http_client import AsyncHttpClient

logger = logging.getLogger("mcp-finance")

class EconomicsLogic:
    """
    處理台灣宏觀經濟指標：薪資、失業率、CPI、GDP 等。
    數據源：勞動部年度國內主要經濟指標 (對接主計總處數據)。
    """

    # 穩定數據源連結 (NID: 130489)
    MOL_ECON_API = "https://apiservice.mol.gov.tw/OdService/download/A17000000J-030243-YTl"

    @staticmethod
    async def get_macro_stats(indicator: str = "all") -> Dict[str, Any]:
        """
        [v3.9.4] 獲取台灣主要宏觀經濟指標。
        切換至勞動部 API，解決 NID 6647 轉跳連結不穩定的問題。
        """
        try:
            data = await AsyncHttpClient.fetch_json(EconomicsLogic.MOL_ECON_API)
            if not data or not isinstance(data, list):
                return {"error": "無法從勞動部 API 獲取數據", "status": "maintenance"}

            # 取最後一筆 (通常是最新年度或預測值)
            latest = data[-1]
            
            # 定義精確的欄位映射 (針對 NID 130489 結構)
            mapping = {
                "gdp": {"key": "經濟成長率", "name": "GDP Growth Rate (%)"},
                "cpi": {"key": "消費者物價-年增率", "name": "CPI Inflation Rate (%)"},
                "unemployment": {"key": "失業率（百分比）", "name": "Unemployment Rate (%)"},
                "salary": {"key": "工業及服務業平均月薪資（元）", "name": "Average Monthly Salary (TWD)"}
            }

            if indicator in mapping:
                target = mapping[indicator]
                return {
                    "indicator": target["name"],
                    "value": latest.get(target["key"], "N/A"),
                    "year": latest.get("年度", "N/A"),
                    "source": "行政院主計總處 / 勞動部 (MOL API)",
                    "note": "目前提供最新年度實測值或初步估計值。"
                }

            # 回傳全部指標摘要
            return {
                "source": "勞動部年度主要經濟指標",
                "year": latest.get("年度", "N/A"),
                "indicators": {
                    "GDP成長率": f"{latest.get('經濟成長率', 'N/A')}%",
                    "CPI年增率": f"{latest.get('消費者物價-年增率', 'N/A')}%",
                    "失業率": f"{latest.get('失業率（百分比）', 'N/A')}%",
                    "平均月薪資": f"{latest.get('工業及服務業平均月薪資（元）', 'N/A')} TWD"
                }
            }
        except Exception as e:
            logger.error(f"MOL Economics API Error: {str(e)}")
            return {"error": "宏觀經濟數據解析異常", "status": "maintenance"}

class TaxLogic:
    """處理稅務數據。"""
    @staticmethod
    async def get_tax_revenue_stats() -> Dict[str, Any]:
        # NID: 7331 (目前維持主計總處 JSON，若未來不穩可再切換至財政部專屬 API)
        url = "https://quality.data.gov.tw/dq_download_json.php?nid=7331&md5_url=e59196b0c242337d40236a281691a5f3"
        try:
            data = await AsyncHttpClient.fetch_json(url)
            latest = data[-1] if data else {}
            return {
                "source": "財政部統計處",
                "tax_revenue": latest.get("實徵淨額", "N/A"),
                "period": latest.get("年月", "N/A")
            }
        except:
            return {"error": "稅務數據暫時無法獲取"}

class PublicServiceLogic:
    """公共服務邏輯：油價、時間。"""
    @staticmethod
    async def get_fuel_prices() -> Dict[str, Any]:
        url = "https://data.cpc.com.tw/opendata/api/ReadTable/GetPrice"
        try:
            data = await AsyncHttpClient.fetch_json(url)
            prices = {item.get("產品名稱"): item.get("參考零售價") for item in data if isinstance(data, list)}
            return {"source": "台灣中油 (CPC)", "prices": prices, "update_time": data[0].get("牌價生效時間") if data else "N/A"}
        except:
            return {"status": "Maintenance", "source": "台灣中油", "message": "API 更新中，請參考中油官網。"}

    @staticmethod
    async def get_current_time():
        tz = pytz.timezone('Asia/Taipei')
        now = datetime.now(tz)
        return {
            "timezone": "Asia/Taipei",
            "current_time": now.strftime("%Y-%m-%d %H:%M:%S"),
            "iso": now.isoformat()
        }
