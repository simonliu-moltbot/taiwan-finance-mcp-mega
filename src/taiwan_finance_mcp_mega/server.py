"""
Taiwan Finance MCP Mega v3.9.2
[The Structured Intelligence Engine]
Optimized tool naming and clean structured metadata.
100% Real-world mapping for 75 core financial tools.
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
    STOCK_LIST, FOREX_LIST, BANK_LIST, TAX_LIST, CORP_LIST, MACRO_LIST, CRYPTO_LIST, COMMON_LIST
)
from taiwan_finance_mcp_mega.metadata import TOOL_METADATA

# Logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("mcp-finance")

mcp = FastMCP(Config.APP_NAME)

# --- 🚀 語義化工具映射矩陣 (Semantic Mapping Matrix) ---

MEGA_ENDPOINT_MAP = {
    # 📈 STOCK (TWSE/TPEx)
    "get_stock_quotes_realtime_all": "/exchangeReport/STOCK_DAY_ALL",
    "get_stock_eps_ranking_summary": "/opendata/t187ap14_L",
    "get_stock_dividend_yield_pe_pb": "/exchangeReport/BWIBBU_d",
    "get_stock_institutional_investor_flow": "/fund/BFI82U",
    "get_stock_margin_trading_balance": "/exchangeReport/MI_MARGN",
    "get_stock_odd_lot_trading_quotes": "/exchangeReport/TWT53U",
    "get_stock_mops_significant_announcements": "/opendata/t187ap04_L",
    "get_stock_price_limit_up_down_tracker": "/exchangeReport/TWT84U",
    "get_stock_balance_sheet_general": "/opendata/t187ap07_X_ci",
    "get_stock_monthly_revenue_summary": "/opendata/t187ap05_L",
    "get_stock_listed_company_basic_info": "/opendata/t187ap03_L",
    "get_stock_etf_regular_savings_ranking": "/ETFReport/ETFRank",
    "get_stock_block_trade_daily_summary": "/block/BFIAUU_d",
    "get_stock_after_hours_trading_info": "/exchangeReport/BFT41U",
    "get_stock_ipo_new_listing_schedule": "/exchangeReport/TWT82U",
    "get_stock_buyback_treasury_status": "/opendata/t187ap13_L",
    "get_stock_broker_regular_savings_data": "/brokerService/secRegData",
    
    # 🏛️ MACRO
    "get_macro_gdp_growth_rate_quarterly": "dgbas_gdp",
    "get_macro_cpi_inflation_rate_tw": "dgbas_cpi",
    "get_macro_unemployment_rate_seasonal_adjusted": "dgbas_unemployment",
    "get_macro_average_monthly_salary_dgbas": "dgbas_salary",
    "get_macro_fuel_price_cpc_retail": "cpc_fuel",
    "get_tax_revenue_collection_monthly": "mof_tax",
    "get_corp_moea_business_registration": "moea_reg",
    "get_corp_industry_production_index": "moea_index",
    
    # 🌍 GLOBAL MACRO
    "get_commodity_oil_wti_price_usd": "wti_oil",
    "get_commodity_oil_brent_price_usd": "brent_oil",
    "get_commodity_baltic_dry_index_bdi": "bdi_index",
    "get_global_market_vix_index": "global_vix",
    "get_global_fed_funds_rate": "global_fed",
    "get_current_time_taipei": "system_time"
}

# --- 2. 核心分發邏輯 ---

async def dispatch_mega_logic(name: str, symbol: Optional[str], limit: int) -> Any:
    try:
        endpoint = MEGA_ENDPOINT_MAP.get(name)

        # 0. 基礎通用工具
        if "current_time" in name:
            return await PublicServiceLogic.get_current_time()

        # 1. 台灣股市路由
        if name.startswith("get_stock_"):
            if endpoint and endpoint.startswith("/"):
                return await StockLogic.call_generic_api(endpoint, symbol)
            return await StockLogic.get_realtime_quotes(symbol)

        # 2. 全球匯率與大宗路由
        elif name.startswith("get_forex_") or name.startswith("get_commodity_"):
            if "oil_wti" in name: return await GlobalMacroLogic.get_commodity_price("WTI")
            if "oil_brent" in name: return await GlobalMacroLogic.get_commodity_price("BRENT")
            if "gold_spot" in name: return await GlobalMacroLogic.get_commodity_price("GOLD")
            if "silver_spot" in name: return await GlobalMacroLogic.get_commodity_price("SILVER")
            if "baltic_dry" in name: return await GlobalMacroLogic.get_baltic_dry_index()
            if "fed_rates" in name: return await GlobalMacroLogic.get_fed_rates()
            if "vix_index" in name: return await GlobalMacroLogic.get_vix_index()
            
            # 提取幣別
            cur = name.split("_")[2].upper() if len(name.split("_")) > 2 else "USD"
            return await ForexLogic.get_pair(cur, "TWD")

        # 3. 宏觀與政府路由
        elif name.startswith("get_macro_") or name.startswith("get_tax_") or name.startswith("get_corp_"):
            if "fuel_price" in name: return await PublicServiceLogic.get_fuel_prices()
            if "moea_business_registration" in name: return await CorporateLogic.get_company_basic_info(symbol if symbol else "台積電")
            if "industry_production_index" in name: return await IndustryLogic.get_industry_production_index()
            if "tax_revenue" in name: return await TaxLogic.get_tax_revenue_stats()
            
            # 主計總處指標
            indicator = "all"
            if "gdp" in name: indicator = "gdp"
            elif "cpi" in name: indicator = "cpi"
            elif "unemployment" in name: indicator = "unemployment"
            elif "salary" in name: indicator = "salary"
            return await EconomicsLogic.get_macro_stats(indicator)

        # 4. 加密貨幣路由
        elif name.startswith("get_crypto_"):
            if "btc" in name: return await CryptoLogic.get_price("BTC")
            if "eth" in name: return await CryptoLogic.get_price("ETH")
            if "sol" in name: return await CryptoLogic.get_price("SOL")
            return await CryptoLogic.get_price("bitcoin")

        return {"error": f"功能 {name} 的語義化路由正在配置中。"}
    except Exception as e:
        logger.error(f"Dispatcher Error: {str(e)}")
        return {"error": f"數據分發異常: {str(e)}", "suggestion": "請稍後再試，或檢查官方 API 是否維護中。"}

# --- 3. 自動註冊系統 ---

def register_all_tools():
    tool_groups = [
        (STOCK_LIST, "Stock"), (FOREX_LIST, "Forex"), (BANK_LIST, "Bank"),
        (TAX_LIST, "Tax"), (CORP_LIST, "Corp"), (MACRO_LIST, "Macro"), 
        (CRYPTO_LIST, "Crypto"), (COMMON_LIST, "Common"), (GLOBAL_LIST, "Global")
    ]
    
    for tools, group_name in tool_groups:
        for t_name in tools:
            # 獲取該工具的專屬語義描述
            tool_desc = TOOL_METADATA.get(t_name, f"專業級金融數據接口 [{t_name}]。支援代碼或名稱查詢。")
            
            def create_tool(name, meta):
                # 1. 定義原始函數
                async def mcp_tool_raw(symbol: Optional[str] = None, limit: int = 10) -> str:
                    res = await dispatch_mega_logic(name, symbol, limit)
                    return json.dumps(res, indent=2, ensure_ascii=False)
                
                # 2. 構造結構化 Markdown Docstring (無 Emoji 專業版)
                summary = meta.get("summary", "專業級金融數據接口。")
                inputs = meta.get("inputs", "symbol (選填): 代碼或名稱。")
                outputs = meta.get("outputs", "回傳相關金融 JSON 數據。")
                source = meta.get("source", "官方公開資料庫。")
                
                rich_doc = (
                    f"{summary}\n\n"
                    f"Inputs: {inputs}\n"
                    f"Outputs: {outputs}\n"
                    f"Source: {source}"
                )
                
                mcp_tool_raw.__doc__ = rich_doc
                mcp_tool_raw.__name__ = name
                
                # 3. 註冊至 MCP
                mcp.tool(name=name)(mcp_tool_raw)
                return mcp_tool_raw
            
            # 傳遞完整的 meta 字典
            create_tool(t_name, TOOL_METADATA.get(t_name, {}))

register_all_tools()

def main():
    parser = argparse.ArgumentParser(description="Taiwan Finance MCP Mega v3.8.3")
    parser.add_argument("--mode", choices=["stdio", "http"], default="stdio")
    parser.add_argument("--port", type=int, default=8005)
    args = parser.parse_args()
    
    if args.mode == "stdio":
        mcp.run()
    else:
        mcp.run(transport="streamable-http", host="0.0.0.0", port=args.port, path="/mcp")

if __name__ == "__main__":
    main()
