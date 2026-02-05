"""
Taiwan Macro-economics & Gov Data Logic - v4.2.1
100% 真實數據對接版本。
新增：中央銀行 (CBC) 基準利率、五大銀行利率、內政部住宅價格指數。
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
    """
    MOL_ECON_API = "https://apiservice.mol.gov.tw/OdService/download/A17000000J-030243-YTl"

    @staticmethod
    async def get_macro_stats(indicator: str = "all") -> Dict[str, Any]:
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
                "indicators": {k: f"{latest.get(v['key'], 'N/A')}%" if k != 'salary' else f"{latest.get(v['key'], 'N/A')} TWD" for k, v in mapping.items()}
            }
        except Exception as e:
            return {"error": f"MOL API 解析異常: {str(e)}", "status": "maintenance"}

    @staticmethod
    async def get_central_bank_rates() -> Dict[str, Any]:
        """獲取中央銀行重貼現率 (NID: 6303)。"""
        url = "https://quality.data.gov.tw/dq_download_json.php?nid=6303&md5_url=59196b0c242337d40236a281691a5f36"
        try:
            data = await AsyncHttpClient.fetch_json(url)
            latest = data[0] if data else {}
            return {
                "source": "中央銀行 (CBC)",
                "indicator": "重貼現率 (Rediscount Rate)",
                "rate": f"{latest.get('重貼現率', 'N/A')}%",
                "effective_date": latest.get("日期", "N/A")
            }
        except:
            return {"error": "央行利率數據暫時無法獲取"}

    @staticmethod
    async def get_five_major_banks_loan_rates() -> Dict[str, Any]:
        """獲取五大銀行新承做放款利率 (NID: 6301)。"""
        # 使用政府 CSV 直接下載路徑以確保穩定
        url = "https://www.cbc.gov.tw/public/data/statistics/rate/5banks.csv"
        try:
            data = await AsyncHttpClient.fetch_csv_as_json(url)
            latest = data[-1] if data else {}
            return {
                "source": "中央銀行 (CBC)",
                "indicator": "五大銀行新承做放款利率",
                "average_mortgage_rate": f"{latest.get('購屋貸款', 'N/A')}%",
                "base_rate": f"{latest.get('基準利率', 'N/A')}%",
                "period": latest.get("日期", "N/A")
            }
        except:
            return {"error": "五大銀行利率數據維護中"}

    @staticmethod
    async def get_housing_price_index() -> Dict[str, Any]:
        """獲取全國住宅價格指數 (NID: 11545)。"""
        url = "https://quality.data.gov.tw/dq_download_json.php?nid=11545&md5_url=59196b0c242337d40236a281691a5f36"
        try:
            data = await AsyncHttpClient.fetch_json(url)
            latest = data[0] if data else {}
            return {
                "source": "內政部地政司",
                "indicator": "全國住宅價格指數",
                "index_value": latest.get("住宅價格指數", "N/A"),
                "period": latest.get("季別", "N/A"),
                "change_yoy": latest.get("年增率(%)", "N/A")
            }
        except:
            return {"error": "住宅指數數據暫時無法獲取"}

class PublicServiceLogic:
    """公共服務邏輯：油價、時間。"""
    CPC_PRICE_API = "https://vipmbr.cpc.com.tw/openData/MainProdListPrice"

    @staticmethod
    async def get_fuel_prices() -> Dict[str, Any]:
        try:
            data = await AsyncHttpClient.fetch_json(PublicServiceLogic.CPC_PRICE_API)
            if not data or not isinstance(data, list):
                return {"status": "Maintenance", "source": "台灣中油", "message": "中油牌價介面維護中。"}
            prices = {item.get("產品名稱"): item.get("參考牌價_金額") for item in data}
            return {"source": "台灣中油 (CPC)", "prices": prices, "effective_date": data[0].get("牌價生效日期")}
        except:
            return {"status": "Maintenance", "message": "中油牌價暫時無法獲取"}

    @staticmethod
    async def get_current_time():
        tz = pytz.timezone('Asia/Taipei')
        now = datetime.now(tz)
        return {
            "timezone": "Asia/Taipei",
            "current_time": now.strftime("%Y-%m-%d %H:%M:%S"),
            "iso": now.isoformat()
        }
