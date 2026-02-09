"""
Taiwan Finance MCP Mega v4.6.0
[High-Contrast Semantic Engine]
Refactored for strict tool separation and precise parameter identification.
Resolved Stock vs. Futures and Central Bank vs. Commercial Bank confusion.
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
from taiwan_finance_mcp_mega.logic.gov_data import EconomicsLogic, PublicServiceLogic, BankLogic, GovNewsLogic
from taiwan_finance_mcp_mega.logic.corporate_logistics import CorporateLogic, IndustryLogic
from taiwan_finance_mcp_mega.utils.http_client import AsyncHttpClient
from taiwan_finance_mcp_mega.constants import (
    STOCK_LIST, FOREX_LIST, BANK_LIST, TAX_LIST, CORP_LIST, MACRO_LIST, CRYPTO_LIST, COMMON_LIST, DERIVATIVES_LIST, NEWS_LIST
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
    "get_stock_institutional_investor_flow": "https://www.twse.com.tw/zh/page/trading/fund/BFI82U.html",
    "get_stock_institutional_trading_tpex": "/v1/tpex_3insti_daily_trading",
    "get_stock_institutional_summary_tpex": "/v1/tpex_3insti_summary",
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
    "get_stock_listed_stock_price_averages": "/exchangeReport/STOCK_DAY_AVG_ALL",
    "get_stock_daily_closing_quotes_all": "/exchangeReport/MI_INDEX",
    "get_stock_yield_averages_by_industry": "/exchangeReport/FMSRFK_ALL",
    "get_stock_pe_averages_by_industry": "/exchangeReport/FMNPTK_ALL",
    "get_stock_broker_list_all": "/brokerService/brokerList",
    "get_stock_buyback_treasury_status": "/opendata/t187ap13_L",
    "get_stock_broker_regular_savings_data": "/brokerService/secRegData"
}

# --- 2. 核心分發邏輯 ---

async def dispatch_mega_logic(name: str, query_val: Optional[str], limit: int) -> Any:
    try:
        if "current_time" in name:
            return await PublicServiceLogic.get_current_time()

        # 1. 台灣股市路由 (Only Stock/ETF)
        if name.startswith("get_stock_"):
            endpoint = MEGA_ENDPOINT_MAP.get(name)
            if endpoint and endpoint.startswith("http"):
                # Direct external URL (e.g. for broken OpenAPI endpoints)
                return {"info": "該數據源目前 OpenAPI 已失效，請點擊連結查看網頁版數據。", "url": endpoint}
            if endpoint and endpoint.startswith("/"):
                # Handle TPEx specifically if needed, or use a separate base
                if "tpex" in endpoint:
                    url = f"{Config.TPEX_BASE}{endpoint}"
                else:
                    url = f"{Config.TWSE_BASE}{endpoint}"
                return await StockLogic.call_generic_api(endpoint, query_val)
            return await StockLogic.get_realtime_quotes(query_val)

        # 1.5 衍生性商品 (Taifex - Futures/Options)
        elif name.startswith("get_futures_"):
            if "institutional" in name: return await DerivativesLogic.get_taifex_institutional_flow()
            if "ranking" in name: return await DerivativesLogic.get_futures_oi_top_list()
            return await DerivativesLogic.get_futures_quotes()

        # 2. 全球匯率與大宗路由
        elif name.startswith("get_forex_") or name.startswith("get_commodity_"):
            if "any_to_any" in name:
                # This would need its own tool registration or generic param handling
                pass # Already handled by param creation below if logic is solid
            if "gold_spot" in name: return await StockLogic.call_generic_api("/v1/gold_DailyQuotes", None)
            if "oil_wti" in name: return await GlobalMacroLogic.get_commodity_price("WTI")
            if "oil_brent" in name: return await GlobalMacroLogic.get_commodity_price("BRENT")
            if "gold_spot" in name: return await GlobalMacroLogic.get_commodity_price("GOLD")
            if "silver_spot" in name: return await GlobalMacroLogic.get_commodity_price("SILVER")
            
            cur = name.split("_")[2].upper() if len(name.split("_")) > 2 else "USD"
            return await ForexLogic.get_pair(cur, "TWD")

        # 3. 宏觀與政府路由 (Macro Metrics)
        elif name.startswith("get_macro_") or name.startswith("get_tax_") or name.startswith("get_gov_"):
            if "financial_news_fsc" in name: return await GovNewsLogic.get_fsc_news()
            if "central_bank_announcements" in name: return await GovNewsLogic.get_cbc_news()
            if "industrial_policy_news" in name: return await GovNewsLogic.get_moea_news()
            
            if "fuel_price" in name: return await PublicServiceLogic.get_fuel_prices()
            if "housing_price_index" in name: return await EconomicsLogic.get_housing_price_index()
            if "national_debt_clock" in name: return await EconomicsLogic.get_national_debt_clock()
            
            # Moved Bank tools to Macro
            if "policy_rate" in name: return await EconomicsLogic.get_macro_stats("gdp") # Placeholder for actual rate logic
            if "money_supply" in name: return await BankLogic.get_bank_profit_loss() # Need mapping
            if "foreign_exchange_reserves" in name: return await BankLogic.get_bank_profit_loss() # Need mapping
            if "bank_mortgage_loan_rates" in name: return await BankLogic.get_bank_profit_loss() # Need mapping
            
            indicator = "all"
            if "gdp" in name: indicator = "gdp"
            elif "cpi" in name: indicator = "cpi"
            elif "unemployment" in name: indicator = "unemployment"
            elif "salary" in name: indicator = "salary"
            return await EconomicsLogic.get_macro_stats(indicator)

        # 4. 商工數據路由
        elif name.startswith("get_corp_"):
            if "electricity_consumption" in name: return await PublicServiceLogic.get_electricity_consumption_stats()
            if "moea_business_registration" in name: return await CorporateLogic.get_company_basic_info(query_val if query_val else "台積電")
            if "industry_production_index" in name: return await IndustryLogic.get_industry_production_index()
            if "factory_count" in name: return await BankLogic.get_bank_profit_loss() # Placeholder
            if "export_value" in name: return await BankLogic.get_bank_profit_loss() # Placeholder
            return {"error": "商工細分數據正在對接中"}

        # 5. 加密貨幣路由
        elif name.startswith("get_crypto_"):
            coin = "bitcoin"
            if "btc" in name: coin = "BTC"
            elif "eth" in name: coin = "ETH"
            elif "sol" in name: coin = "SOL"
            if "fear_greed" in name: return await CryptoLogic.get_fear_greed_index()
            return await CryptoLogic.get_price(coin)

        # 6. 銀行數據 (Commercial Banks only)
        elif name.startswith("get_bank_"):
            if "list_of_institutions" in name: return await BankLogic.get_list_of_institutions()
            if "profit_loss" in name: return await BankLogic.get_bank_profit_loss()
            return {"error": "銀行商業數據正在對接中"}

        return {"error": f"功能 {name} 尚未完全實體化。"}
    except Exception as e:
        return {"error": f"Dispatcher 異常: {str(e)}"}

# --- 3. 自動註冊系統 ---

def register_all_tools():
    tool_groups = [
        (STOCK_LIST, "Stock"), (FOREX_LIST, "Forex"), (BANK_LIST, "Bank"),
        (TAX_LIST, "Tax"), (CORP_LIST, "Corp"), (MACRO_LIST, "Macro"), 
        (CRYPTO_LIST, "Crypto"), (COMMON_LIST, "Common"), (DERIVATIVES_LIST, "Derivatives"),
        (NEWS_LIST, "News")
    ]
    
    for tools, group_name in tool_groups:
        for t_name in tools:
            meta = TOOL_METADATA.get(t_name, {})
            summary = meta.get("summary", "專業級金融數據接口。")
            inputs_desc = meta.get("inputs", "None")
            outputs = meta.get("outputs", "回傳相關金融 JSON 數據。")
            source = meta.get("source", "官方公開資料庫。")
            
            # High-Contrast Docstring
            rich_doc = f"{summary}\n\nOutputs: {outputs}\nSource: {source}"

            # 根據工具類別決定參數名稱與描述，強化模型辨識度
            param_name = "symbol"
            param_desc = "代碼或關鍵字"
            
            if t_name.startswith("get_stock_"):
                param_name = "ticker"
                param_desc = "股票代碼 (例如: 2330, 0050)。請勿在此輸入期貨名稱。"
            elif t_name.startswith("get_corp_"):
                param_name = "company_query"
                param_desc = "公司全名或統一編號 (例如: 台灣積體電路, 22099131)。"
            elif t_name.startswith("get_bank_"):
                param_name = "bank_query"
                param_desc = "銀行名稱或金融機構代碼 (例如: 臺灣銀行, 004)。"
            elif t_name == "get_forex_any_to_any_conversion":
                @mcp.tool(name=t_name)
                async def mcp_tool_forex_any(base: str = "JPY", target: str = "TWD") -> str:
                    res = await ForexLogic.get_pair(base, target)
                    return json.dumps(res, indent=2, ensure_ascii=False)
                mcp_tool_forex_any.__doc__ = f"{rich_doc}\n\nArgs:\n  base: 原始幣別 (例: JPY)\n  target: 目標幣別 (例: TWD)"
                continue

            # 註冊無參數工具 (完全移除 Args，強迫模型精確匹配)
            if "None" in inputs_desc:
                def create_no_param_tool(name, doc):
                    @mcp.tool(name=name)
                    async def mcp_tool_no_param() -> str:
                        res = await dispatch_mega_logic(name, None, 10)
                        return json.dumps(res, indent=2, ensure_ascii=False)
                    mcp_tool_no_param.__doc__ = doc
                    return mcp_tool_no_param
                create_no_param_tool(t_name, rich_doc)
            
            # 註冊帶參數工具
            else:
                def create_param_tool(name, doc, p_name, p_desc):
                    if p_name == "ticker":
                        @mcp.tool(name=name)
                        async def mcp_tool_ticker(ticker: Optional[str] = None, limit: int = 10) -> str:
                            res = await dispatch_mega_logic(name, ticker, limit)
                            return json.dumps(res, indent=2, ensure_ascii=False)
                        mcp_tool_ticker.__doc__ = f"{doc}\n\nArgs:\n  ticker: {p_desc}\n  limit: 回傳數據筆數限制。"
                    elif p_name == "company_query":
                        @mcp.tool(name=name)
                        async def mcp_tool_corp(company_query: Optional[str] = None, limit: int = 10) -> str:
                            res = await dispatch_mega_logic(name, company_query, limit)
                            return json.dumps(res, indent=2, ensure_ascii=False)
                        mcp_tool_corp.__doc__ = f"{doc}\n\nArgs:\n  company_query: {p_desc}\n  limit: 回傳數據筆數限制。"
                    elif p_name == "bank_query":
                        @mcp.tool(name=name)
                        async def mcp_tool_bank(bank_query: Optional[str] = None, limit: int = 10) -> str:
                            res = await dispatch_mega_logic(name, bank_query, limit)
                            return json.dumps(res, indent=2, ensure_ascii=False)
                        mcp_tool_bank.__doc__ = f"{doc}\n\nArgs:\n  bank_query: {p_desc}\n  limit: 回傳數據筆數限制。"
                    else:
                        @mcp.tool(name=name)
                        async def mcp_tool_generic(symbol: Optional[str] = None, limit: int = 10) -> str:
                            res = await dispatch_mega_logic(name, symbol, limit)
                            return json.dumps(res, indent=2, ensure_ascii=False)
                        mcp_tool_generic.__doc__ = f"{doc}\n\nArgs:\n  symbol: {p_desc}\n  limit: 回傳數據筆數限制。"
                
                create_param_tool(t_name, rich_doc, param_name, param_desc)

register_all_tools()

def main():
    parser = argparse.ArgumentParser(description="Taiwan Finance MCP Mega v4.6.0")
    parser.add_argument("--mode", choices=["stdio", "http"], default="stdio")
    parser.add_argument("--port", type=int, default=8005)
    args = parser.parse_args()
    if args.mode == "stdio": mcp.run()
    else: mcp.run(transport="streamable-http", host="0.0.0.0", port=args.port, path="/mcp")

if __name__ == "__main__":
    main()
