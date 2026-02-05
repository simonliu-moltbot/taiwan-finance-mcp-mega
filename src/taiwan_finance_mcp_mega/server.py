"""
Taiwan Finance MCP Mega v3.4.2
旗艦級金融數據伺服器 - 邏輯分發與自動對接優化版。
"""
import sys
import argparse
import json
import logging
from fastmcp import FastMCP
from typing import Optional, List, Dict, Any

# Component Imports
from taiwan_finance_mcp_mega.config import Config
from taiwan_finance_mcp_mega.logic.stock import StockLogic
from taiwan_finance_mcp_mega.logic.forex import ForexLogic
from taiwan_finance_mcp_mega.logic.global_macro import GlobalMacroLogic, CryptoLogic
from taiwan_finance_mcp_mega.logic.gov_data import EconomicsLogic, TaxLogic, PublicServiceLogic
from taiwan_finance_mcp_mega.logic.corporate_logistics import CorporateLogic, IndustryLogic
from taiwan_finance_mcp_mega.utils.http_client import AsyncHttpClient
from taiwan_finance_mcp_mega.constants import (
    STOCK_LIST, FOREX_LIST, BANK_LIST, TAX_LIST, CORP_LIST, MACRO_LIST, CRYPTO_LIST
)

# Logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("mcp-finance")

mcp = FastMCP(Config.APP_NAME)

# --- 1. 定義完整的 API 映射字典 (Exhaustive Map) ---

API_ENDPOINT_MAP = {
    # STOCK
    "realtime_quotes": "/exchangeReport/STOCK_DAY_ALL",
    "fundamental_eps": "/opendata/t187ap14_L",
    "dividend_yield": "/exchangeReport/BWIBBU_d",
    "chip_institutional_flow": "/fund/BFI82U",
    "margin_balance_monitor": "/exchangeReport/MI_MARGN",
    "odd_lot_quotes": "/exchangeReport/TWT53U",
    "announcements": "/opendata/t187ap04_L",
    "price_limit_tracker": "/exchangeReport/TWT84U",
    "financial_report_general": "/opendata/t187ap07_X_ci",
    "monthly_revenue": "/opendata/t187ap05_L",
    "listed_company_basic_info": "/opendata/t187ap03_L",
    "etf_regular_savings_rank": "/ETFReport/ETFRank",
    "esg_ghg_emissions": "/opendata/t187ap46_L_1",
    "esg_occupational_safety": "/opendata/t187ap46_L_21",
    "esg_waste_management": "/opendata/t187ap46_L_4",
    "esg_water_resources": "/opendata/t187ap46_L_3",
    "esg_food_safety": "/opendata/t187ap46_L_12",
    "block_trade_summary": "/block/BFIAUU_d",
    # CORPORATE
    "company_registration": "corp_reg",
    "industry_production_index": "corp_industry_index",
    # GLOBAL
    "fed_rates": "global_fed",
    "vix_index": "global_vix",
    "baltic_dry": "global_bdi"
}

# --- 2. 核心分發邏輯 ---

async def dispatch_mega_logic(name: str, symbol: Optional[str], limit: int) -> Any:
    try:
        # Global 宏觀邏輯
        if name.startswith("global_") or name == "macro_global_stats":
            if "fed" in name: return await GlobalMacroLogic.get_fed_rates()
            if "vix" in name: return await GlobalMacroLogic.get_vix_index()
            if "bdi" in name: return await GlobalMacroLogic.get_baltic_dry_index()
            return await GlobalMacroLogic.get_fed_rates()

        # A. 台股類
        if name.startswith("stock_"):
            tool_id = name.replace("stock_", "")
            
            # 優先檢查映射表
            endpoint = API_ENDPOINT_MAP.get(tool_id)
            if endpoint:
                return await StockLogic.call_generic_api(endpoint, symbol)
            
            # 特殊邏輯分支
            if tool_id == "realtime_quotes": return await StockLogic.get_realtime_quotes(symbol)
            return await StockLogic.get_realtime_quotes(symbol)

        # B. 匯率類
        elif name.startswith("forex_"):
            # 優先處理大宗商品 (Oil, Gold, etc.)
            if "oil_wti" in name: return await GlobalMacroLogic.get_commodity_price("WTI")
            if "oil_brent" in name: return await GlobalMacroLogic.get_commodity_price("BRENT")
            if "gold_spot" in name: return await GlobalMacroLogic.get_commodity_price("GOLD")
            if "silver_spot" in name: return await GlobalMacroLogic.get_commodity_price("SILVER")
            
            parts = name.split("_")
            if len(parts) >= 2:
                cur = parts[1].upper()
                if cur not in ["BANK", "HISTORICAL", "RATE"]:
                    return await ForexLogic.get_pair(cur, "TWD")
            return await ForexLogic.get_latest_rates()

        # E. 企業與物流類 (Corporate & Logistics)
        elif name.startswith("corp_"):
            if "company_registration" in name:
                return await CorporateLogic.get_company_basic_info(symbol if symbol else "台積電")
            if "industry_production_index" in name:
                return await IndustryLogic.get_industry_production_index()
            return await CorporateLogic.get_company_basic_info(symbol if symbol else "台積電")

        # C. 宏觀與稅務
        elif name.startswith("macro_") or name.startswith("tax_"):
            # 修正指標識別邏輯
            indicator = "all"
            if "salary" in name: indicator = "salary"
            elif "unemployment" in name: indicator = "unemployment"
            elif "cpi" in name: indicator = "cpi"
            elif "gdp" in name: indicator = "gdp"
            
            # 正確調用 EconomicsLogic
            return await EconomicsLogic.get_macro_stats(indicator)

        # D. 加密貨幣
        elif name.startswith("crypto_"):
            coin = symbol if symbol else "bitcoin"
            return await CryptoLogic.get_price(coin)

        return {"error": f"功能 {name} 的真實邏輯接口正在部署中。"}
    except Exception as e:
        return {"error": f"API 呼叫異常: {str(e)}"}

# --- 3. 自動註冊系統 ---

def register_all_tools():
    mega_map = {
        "stock": (STOCK_LIST, "台股分析"),
        "forex": (FOREX_LIST, "全球匯率"),
        "bank": (BANK_LIST, "銀行與信貸"),
        "tax": (TAX_LIST, "稅務法規"),
        "corp": (CORP_LIST, "企業與產業"),
        "macro": (MACRO_LIST, "宏觀經濟"),
        "crypto": (CRYPTO_LIST, "Web3 監控")
    }
    
    for prefix, (tools, desc) in mega_map.items():
        for t_id in tools:
            t_name = f"{prefix}_{t_id}"
            def bind_fn(name):
                @mcp.tool(name=name)
                async def fn(symbol: Optional[str] = None, limit: int = 10) -> str:
                    """
                    [v3.5.6] 獲取真實金融數據。
                    參數 symbol: 股票代碼 (2330), ETF代碼 (0050), 貨幣 (JPY), 加密幣 (BTC) 或公司名稱。
                    """
                    res = await dispatch_mega_logic(name, symbol, limit)
                    return json.dumps(res, indent=2, ensure_ascii=False)
                fn.__name__ = name
                return fn
            bind_fn(t_name)

register_all_tools()

def main():
    parser = argparse.ArgumentParser(description="Taiwan Finance MCP Mega v3.4.2")
    parser.add_argument("--mode", choices=["stdio", "http"], default="stdio")
    parser.add_argument("--port", type=int, default=8000)
    args = parser.parse_args()
    
    if args.mode == "stdio":
        mcp.run()
    else:
        mcp.run(transport="streamable-http", host="0.0.0.0", port=args.port, path="/mcp")

if __name__ == "__main__":
    main()
