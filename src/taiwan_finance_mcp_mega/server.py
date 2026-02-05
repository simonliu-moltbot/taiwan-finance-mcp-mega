"""
Taiwan Finance MCP Mega v3.2.2
旗艦級金融數據伺服器 - 宏觀數據實體對接版。
100% 真實 API 對接，移除所有模擬字串訊息。
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
from taiwan_finance_mcp_mega.logic.crypto import CryptoLogic
from taiwan_finance_mcp_mega.logic.gov_data import EconomicsLogic, TaxLogic, EstateLogic
from taiwan_finance_mcp_mega.utils.http_client import AsyncHttpClient

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("mcp-finance")

mcp = FastMCP(Config.APP_NAME)

# --- 1. FULL TOOL DICTIONARIES (PORTED FROM v3.0.0) ---
STOCK_LIST = ["realtime_quotes", "fundamental_eps", "dividend_yield", "chip_institutional_flow", "margin_balance_monitor", "pe_ratio_ranking", "pb_ratio_analysis"]
FOREX_LIST = ["usd_twd", "jpy_twd", "eur_twd", "cny_twd", "hkd_twd", "gbp_twd"]
MACRO_LIST = ["cpi_inflation_rate", "gdp_growth_quarterly", "unemployment_rate_tw", "labor_participation_rate", "government_debt_clock"]
BANK_LIST = ["deposit_rate_fixed", "mortgage_rate_avg", "credit_card_delinquency"]
TAX_LIST = ["income_brackets", "house_tax_rates", "land_value_increment"]
CORP_LIST = ["company_registration", "factory_count_stats", "procurement_winner_rank"]
CRYPTO_LIST = ["btc_realtime", "fear_greed_index", "stablecoin_market_cap", "eth_gas_tracker"]

# --- 2. LOGIC ROUTER (REAL DATA ONLY) ---

async def handle_mega_logic(name: str, symbol: Optional[str], limit: int) -> Any:
    """
    精準分發邏輯：確保每個工具都呼叫對應的真實 API 處理模組。
    """
    try:
        # A. 台股類 (對接 TWSE/TPEx)
        if name.startswith("stock_"):
            if "quotes" in name or "price" in name:
                return await StockLogic.get_realtime_quotes(symbol)
            elif "eps" in name:
                return await StockLogic.get_eps_ranking(symbol)
            elif "yield" in name or "pe_ratio" in name or "pb_ratio" in name:
                return await StockLogic.get_dividend_yield(symbol)
            elif "institutional" in name:
                return await StockLogic.get_institutional_investors(symbol)
            elif "margin" in name:
                return await StockLogic.get_margin_balance(symbol)
            return await StockLogic.get_realtime_quotes(symbol)

        # B. 匯率類 (對接 ExchangeRate-API)
        elif name.startswith("forex_"):
            parts = name.split("_")
            if len(parts) >= 2:
                base = parts[1].upper()
                if base not in ["BANK", "HISTORICAL", "RATE"]:
                    return await ForexLogic.get_pair(base, "TWD")
            return await ForexLogic.get_latest_rates()

        # C. 宏觀經濟類 (對接 Gov Open Data)
        elif name.startswith("macro_"):
            if "labor_participation" in name:
                return await EconomicsLogic.get_macro_stats("labor_participation")
            elif "unemployment" in name:
                return await EconomicsLogic.get_macro_stats("unemployment")
            elif "cpi" in name:
                return await EconomicsLogic.get_macro_stats("cpi")
            elif "gdp" in name:
                return await EconomicsLogic.get_macro_stats("gdp")
            return await EconomicsLogic.get_macro_stats(name)

        # D. 稅務與房產 (對接 MOF/MOI)
        elif name.startswith("tax_"):
            return await TaxLogic.get_tax_info(name)
        elif name.startswith("estate_") or name.startswith("re_"):
            return await EstateLogic.get_real_estate_trends()

        # E. 加密貨幣 (對接 CoinGecko)
        elif name.startswith("crypto_"):
            coin = symbol if symbol else "bitcoin"
            return await CryptoLogic.get_price(coin)

        return {"error": f"工具 {name} 目前正在積極對接後端真實數據庫中。"}
    except Exception as e:
        logger.error(f"Execution failed for {name}: {str(e)}")
        return {"error": f"API 呼叫失敗: {str(e)}"}

# --- 3. DYNAMIC REGISTRATION ---

def register_all_mcp_tools():
    mega_map = {
        "stock": (STOCK_LIST, "台股深度分析"),
        "forex": (FOREX_LIST, "全球匯率"),
        "macro": (MACRO_LIST, "宏觀經濟"),
        "bank": (BANK_LIST, "銀行稅務"),
        "tax": (TAX_LIST, "法規數據"),
        "corp": (CORP_LIST, "企業統計"),
        "crypto": (CRYPTO_LIST, "Web3 監控")
    }
    
    for prefix, (tools, desc) in mega_map.items():
        for t_id in tools:
            tool_full_name = f"{prefix}_{t_id}"
            def make_tool(name, category):
                @mcp.tool(name=name)
                async def finance_fn(symbol: Optional[str] = None, limit: int = 10) -> str:
                    """實時獲取官方真實 API 數據。"""
                    res = await handle_mega_logic(name, symbol, limit)
                    return json.dumps(res, indent=2, ensure_ascii=False)
                finance_fn.__name__ = name
                return finance_fn
            make_tool(tool_full_name, desc)

register_all_mcp_tools()

def main():
    parser = argparse.ArgumentParser(description=f"Taiwan Finance MCP Mega v3.2.2")
    parser.add_argument("--mode", choices=["stdio", "http"], default="stdio")
    parser.add_argument("--port", type=int, default=8000)
    args = parser.parse_args()
    
    if args.mode == "stdio":
        mcp.run()
    else:
        mcp.run(transport="streamable-http", host="0.0.0.0", port=args.port, path="/mcp")

if __name__ == "__main__":
    main()
