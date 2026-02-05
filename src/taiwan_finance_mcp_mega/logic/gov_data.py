"""
Taiwan Macro-economics & Gov Data Logic - v4.1.0
100% 真實數據對接版本。
更新：中油主產品牌價對接特定穩定 JSON 接口 (NID: 6339)。
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
        """[v3.9.4] 獲取台灣主要宏觀經濟指標。"""
        try:
            data = await AsyncHttpClient.fetch_json(EconomicsLogic.MOL_ECON_API)
            if not data or not isinstance(data, list):
                return {"error": "無法從勞動部 API 獲取數據", "status": "maintenance"}

            latest = data[-1]
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
                    "source": "行政院主計總處 / 勞動部 (MOL API)"
                }

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
            return {"error": f"MOL API 解析異常: {str(e)}", "status": "maintenance"}

class PublicServiceLogic:
    """公共服務邏輯：油價、時間。"""
    
    # 中油主產品牌價 JSON (NID: 6339)
    CPC_PRICE_API = "https://vipmbr.cpc.com.tw/openData/MainProdListPrice"

    @staticmethod
    async def get_fuel_prices() -> Dict[str, Any]:
        """
        [v4.1.0] 獲取台灣中油即時油價 (對接 NID: 6339)。
        """
        try:
            data = await AsyncHttpClient.fetch_json(PublicServiceLogic.CPC_PRICE_API)
            if not data or not isinstance(data, list):
                return {"status": "Maintenance", "source": "台灣中油", "message": "中油牌價介面維護中。"}
            
            # 對接 JSON 欄位：產品名稱, 參考牌價_金額, 牌價生效日期
            prices = {}
            valid_date = "N/A"
            for item in data:
                name = item.get("產品名稱", "")
                price = item.get("參考牌價_金額", "")
                valid_date = item.get("牌價生效日期", valid_date)
                
                if "92" in name: prices["92_unleaded"] = price
                elif "95" in name: prices["95_unleaded"] = price
                elif "98" in name: prices["98_unleaded"] = price
                elif "超級柴油" in name: prices["diesel"] = price
            
            return {
                "source": "台灣中油 (CPC)",
                "prices": prices,
                "effective_date": valid_date,
                "status": "Authentic Data (NID 6339)"
            }
        except Exception as e:
            return {"error": "中油數據抓取異常", "detail": str(e)}

    @staticmethod
    async def get_current_time():
        tz = pytz.timezone('Asia/Taipei')
        now = datetime.now(tz)
        return {
            "timezone": "Asia/Taipei",
            "current_time": now.strftime("%Y-%m-%d %H:%M:%S"),
            "iso": now.isoformat()
        }
