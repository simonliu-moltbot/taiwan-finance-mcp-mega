"""
Taiwan Finance MCP Mega v3.8.1
[The Semantic Engine]
Optimized tool naming and rich metadata dispatching.
100% Real-world mapping for 300+ financial indicators.
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
    
    # 🌿 ESG
    "get_stock_esg_greenhouse_gas_emissions": "/opendata/t187ap46_L_1",
    "get_stock_esg_energy_management_efficiency": "/opendata/t187ap46_L_2",
    "get_stock_esg_water_resource_usage": "/opendata/t187ap46_L_3",
    "get_stock_esg_waste_management_data": "/opendata/t187ap46_L_4",
    "get_stock_esg_human_capital_development": "/opendata/t187ap46_L_5",
    "get_stock_esg_board_diversity_structure": "/opendata/t187ap46_L_6",
    "get_stock_esg_investor_communication_index": "/opendata/t187ap46_L_7",
    "get_stock_esg_climate_change_governance": "/opendata/t187ap46_L_8",
    "get_stock_esg_functional_committee_status": "/opendata/t187ap46_L_9",
    "get_stock_esg_fuel_management_stats": "/opendata/t187ap46_L_10",
    "get_stock_esg_product_life_cycle_management": "/opendata/t187ap46_L_11",
    "get_stock_esg_food_safety_verification": "/opendata/t187ap46_L_12",
    "get_stock_esg_supply_chain_management_audit": "/opendata/t187ap46_L_13",
    "get_stock_esg_product_quality_safety": "/opendata/t187ap46_L_14",
    "get_stock_esg_local_community_relations": "/opendata/t187ap46_L_15",
    "get_stock_esg_information_security_breach": "/opendata/t187ap46_L_16",
    "get_stock_esg_inclusive_finance_promotion": "/opendata/t187ap46_L_17",
    "get_stock_esg_shareholding_control_power": "/opendata/t187ap46_L_18",
    "get_stock_esg_risk_management_policy": "/opendata/t187ap46_L_19",
    "get_stock_esg_anti_competitive_litigation": "/opendata/t187ap46_L_20",
    "get_stock_esg_occupational_safety_health": "/opendata/t187ap46_L_21",

    # 🏛️ MACRO
    "get_macro_gdp_growth_rate_quarterly": "dgbas_gdp",
    "get_macro_cpi_inflation_rate_tw": "dgbas_cpi",
    "get_macro_unemployment_rate_seasonal_adjusted": "dgbas_unemployment",
    "get_macro_average_monthly_salary_dgbas": "dgbas_salary",
    "get_macro_fuel_price_cpc_retail": "cpc_fuel",
    "get_tax_revenue_collection_monthly": "mof_tax",
    "get_corp_moea_business_registration": "moea_reg",
    "get_corp_industry_production_index": "moea_index",
    
    # 🕒 COMMON
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
        (CRYPTO_LIST, "Crypto"), (COMMON_LIST, "Common")
    ]
    
    for tools, group_name in tool_groups:
        for t_name in tools:
            # 獲取該工具的專屬語義描述，若無則使用預設
            tool_desc = TOOL_METADATA.get(t_name, f"專業級金融數據接口 [{t_name}]。支援代碼或名稱查詢。")
            
            def create_tool(name, desc):
                @mcp.tool(name=name)
                async def mcp_tool_fn(symbol: Optional[str] = None, limit: int = 10) -> str:
                    """[v3.8.1] 專業金融數據接口。支援代碼 (2330) 或名稱查詢。"""
                    res = await dispatch_mega_logic(name, symbol, limit)
                    return json.dumps(res, indent=2, ensure_ascii=False)
                
                # 動態注入富含語義的 Docstring
                mcp_tool_fn.__doc__ = f"{desc}\n\n[v3.8.1] 參數 symbol: 標的代碼或名稱。"
                mcp_tool_fn.__name__ = name
                return mcp_tool_fn
            
            create_tool(t_name, tool_desc)

register_all_tools()

def main():
    parser = argparse.ArgumentParser(description="Taiwan Finance MCP Mega v3.8.1")
    parser.add_argument("--mode", choices=["stdio", "http"], default="stdio")
    parser.add_argument("--port", type=int, default=8005)
    args = parser.parse_args()
    
    if args.mode == "stdio":
        mcp.run()
    else:
        mcp.run(transport="streamable-http", host="0.0.0.0", port=args.port, path="/mcp")

if __name__ == "__main__":
    main()
