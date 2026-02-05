"""
Taiwan Finance MCP Mega v4.4.0
[The Refined Industrial Engine]
Finalized with Industrial Leading Indicators and Debt stats.
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
from taiwan_finance_mcp_mega.logic.derivatives import DerivativesLogic
from taiwan_finance_mcp_mega.logic.global_macro import GlobalMacroLogic, CryptoLogic
from taiwan_finance_mcp_mega.logic.gov_data import EconomicsLogic, PublicServiceLogic, BankLogic
from taiwan_finance_mcp_mega.logic.corporate_logistics import CorporateLogic, IndustryLogic
from taiwan_finance_mcp_mega.utils.http_client import AsyncHttpClient
from taiwan_finance_mcp_mega.constants import (
    STOCK_LIST, FOREX_LIST, BANK_LIST, TAX_LIST, CORP_LIST, MACRO_LIST, CRYPTO_LIST, COMMON_LIST, DERIVATIVES_LIST
)
from taiwan_finance_mcp_mega.metadata import TOOL_METADATA

# Logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("mcp-finance")

mcp = FastMCP(Config.APP_NAME)

# --- 🚀 語義化工具映射矩陣 (Semantic Mapping Matrix) ---

MEGA_ENDPOINT_MAP = {
    # 📈 STOCK
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
    "get_macro_housing_price_index_tw": "housing_index",
    "get_macro_national_debt_clock": "mof_debt",
    "get_corp_industry_electricity_consumption_stats": "moea_elec",
    "get_current_time_taipei": "system_time"
}

# --- 2. 核心分發邏輯 ---

async def dispatch_mega_logic(name: str, symbol: Optional[str], limit: int) -> Any:
    try:
        if "current_time" in name:
            return await PublicServiceLogic.get_current_time()

        # 1. 台灣股市路由
        if name.startswith("get_stock_"):
            endpoint = MEGA_ENDPOINT_MAP.get(name)
            if endpoint and endpoint.startswith("/"):
                return await StockLogic.call_generic_api(endpoint, symbol)
            return await StockLogic.get_realtime_quotes(symbol)

        # 1.5 衍生性商品 (Taifex)
        elif name.startswith("get_futures_"):
            if "institutional" in name: return await DerivativesLogic.get_taifex_institutional_flow()
            if "ranking" in name: return await DerivativesLogic.get_futures_oi_top_list()
            return await DerivativesLogic.get_futures_quotes()

        # 2. 全球匯率與大宗路由
        elif name.startswith("get_forex_") or name.startswith("get_commodity_"):
            if "oil_wti" in name: return await GlobalMacroLogic.get_commodity_price("WTI")
            if "oil_brent" in name: return await GlobalMacroLogic.get_commodity_price("BRENT")
            if "gold_spot" in name: return await GlobalMacroLogic.get_commodity_price("GOLD")
            if "silver_spot" in name: return await GlobalMacroLogic.get_commodity_price("SILVER")
            
            cur = name.split("_")[2].upper() if len(name.split("_")) > 2 else "USD"
            return await ForexLogic.get_pair(cur, "TWD")

        # 3. 宏觀與政府路由
        elif name.startswith("get_macro_") or name.startswith("get_tax_") or name.startswith("get_corp_"):
            if "fuel_price" in name: return await PublicServiceLogic.get_fuel_prices()
            if "housing_price_index" in name: return await EconomicsLogic.get_housing_price_index()
            if "national_debt_clock" in name: return await EconomicsLogic.get_national_debt_clock()
            if "electricity_consumption" in name: return await PublicServiceLogic.get_electricity_consumption_stats()
            if "moea_business_registration" in name: return await CorporateLogic.get_company_basic_info(symbol if symbol else "台積電")
            if "industry_production_index" in name: return await IndustryLogic.get_industry_production_index()
            
            indicator = "all"
            if "gdp" in name: indicator = "gdp"
            elif "cpi" in name: indicator = "cpi"
            elif "unemployment" in name: indicator = "unemployment"
            elif "salary" in name: indicator = "salary"
            return await EconomicsLogic.get_macro_stats(indicator)

        # 4. 加密貨幣路由
        elif name.startswith("get_crypto_"):
            coin = "bitcoin"
            if "btc" in name: coin = "BTC"
            elif "eth" in name: coin = "ETH"
            elif "sol" in name: coin = "SOL"
            return await CryptoLogic.get_price(coin)

        # 5. 銀行數據
        elif name.startswith("get_bank_"):
            if "central_bank_base_rate" in name: return await EconomicsLogic.get_central_bank_rates()
            if "five_major_banks" in name: return await EconomicsLogic.get_five_major_banks_loan_rates()
            if "money_supply" in name: return await EconomicsLogic.get_money_supply_stats()
            if "foreign_exchange_reserves" in name: return await EconomicsLogic.get_fx_reserves()
            return {"error": "銀行細分數據正在對接中"}

        return {"error": f"功能 {name} 尚未完全實體化。"}
    except Exception as e:
        return {"error": f"Dispatcher 異常: {str(e)}"}

# --- 3. 自動註冊系統 ---

def register_all_tools():
    tool_groups = [
        (STOCK_LIST, "Stock"), (FOREX_LIST, "Forex"), (BANK_LIST, "Bank"),
        (TAX_LIST, "Tax"), (CORP_LIST, "Corp"), (MACRO_LIST, "Macro"), 
        (CRYPTO_LIST, "Crypto"), (COMMON_LIST, "Common"), (DERIVATIVES_LIST, "Derivatives")
    ]
    
    for tools, group_name in tool_groups:
        for t_name in tools:
            tool_desc_dict = TOOL_METADATA.get(t_name, {})
            # 構造結構化 Markdown Docstring (無 Emoji 專業版)
            summary = tool_desc_dict.get("summary", "專業級金融數據接口。")
            inputs = tool_desc_dict.get("inputs", "symbol (選填): 代碼或名稱。")
            outputs = tool_desc_dict.get("outputs", "回傳相關金融 JSON 數據。")
            source = tool_desc_dict.get("source", "官方公開資料庫。")
            
            rich_doc = (
                f"{summary}\n\n"
                f"Inputs: {inputs}\n"
                f"Outputs: {outputs}\n"
                f"Source: {source}"
            )

            def create_tool(name, desc):
                async def mcp_tool_raw(symbol: Optional[str] = None, limit: int = 10) -> str:
                    res = await dispatch_mega_logic(name, symbol, limit)
                    return json.dumps(res, indent=2, ensure_ascii=False)
                mcp_tool_raw.__doc__ = f"{desc}"
                mcp_tool_raw.__name__ = name
                mcp.tool(name=name)(mcp_tool_raw)
                return mcp_tool_raw
            create_tool(t_name, rich_doc)

register_all_tools()

def main():
    parser = argparse.ArgumentParser(description="Taiwan Finance MCP Mega v4.4.0")
    parser.add_argument("--mode", choices=["stdio", "http"], default="stdio")
    parser.add_argument("--port", type=int, default=8005)
    args = parser.parse_args()
    if args.mode == "stdio": mcp.run()
    else: mcp.run(transport="streamable-http", host="0.0.0.0", port=args.port, path="/mcp")

if __name__ == "__main__":
    main()
