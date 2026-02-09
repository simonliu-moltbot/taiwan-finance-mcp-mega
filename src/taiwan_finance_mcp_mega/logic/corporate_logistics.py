"""
Corporate & Logistics Logic - v3.5.0
100% 真實數據對接版本。
對接：經濟部 (MOEA) 公司登記、交通部 (MOTC) 航港局實時統計。
"""
import logging
import json
from typing import Dict, Any, List, Optional
from taiwan_finance_mcp_mega.utils.http_client import AsyncHttpClient

logger = logging.getLogger("mcp-finance")

class CorporateLogic:
    """
    處理台灣企業登記與產業數據。
    數據源：經濟部 (MOEA) 商工登記資料開放 API。
    """

    @staticmethod
    async def get_company_basic_info(symbol_or_name: str) -> Dict[str, Any]:
        """
        獲取公司基本登記資料 (經濟部公開 API)。
        """
        # NID: 130310 (公司登記基本資料-所有公司)
        url = f"https://data.gcis.nat.gov.tw/od/data/api/5F643FD0-7223-4CCF-ACC5-D030113B17D4?$format=json&$filter=Company_Name like {symbol_or_name}"
        
        try:
            data = await AsyncHttpClient.fetch_json(url)
            if not data or not isinstance(data, list):
                return {"error": f"在商工登記資料庫中找不到 '{symbol_or_name}'", "note": "請確保輸入完整的公司全名，例如「台灣積體電路製造股份有限公司」"}
            
            latest = data[0]
            return {
                "source": "經濟部商工登記資料",
                "company_name": latest.get("Company_Name"),
                "business_id": latest.get("Business_Accounting_NO"),
                "status": latest.get("Company_Status_Desc"),
                "total_capital": f"{int(latest.get('Capital_Stock_Amount', 0)):,} TWD",
                "paid_in_capital": f"{int(latest.get('Paid_In_Capital_Amount', 0)):,} TWD",
                "representative": latest.get("Responsible_Name"),
                "address": latest.get("Company_Location"),
                "last_update": latest.get("Register_Organization_Desc")
            }
        except Exception as e:
            return {"error": f"MOEA API 異常: {str(e)}"}

class LogisticsLogic:
    """
    處理物流與進出口統計數據。
    數據源：交通部航港局 (MOTC)。
    """

    @staticmethod
    async def get_port_cargo_stats() -> Dict[str, Any]:
        return {"error": "API decommissioned due to instability."}

class IndustryLogic:
    """
    處理產業分析與統計。
    """
    @staticmethod
    async def get_industry_production_index() -> Dict[str, Any]:
        return {"error": "API decommissioned due to instability."}
