"""
Taiwan Finance MCP Mega v3.3.3
旗艦級金融數據伺服器 - 邏輯優化版。
移除不穩定的銀行比價功能，專注於精確的市場即時匯率換算。
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
from taiwan_finance_mcp_mega.constants import (
    STOCK_LIST, FOREX_LIST, BANK_LIST, TAX_LIST, CORP_LIST, MACRO_LIST, CRYPTO_LIST
)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("mcp-finance")

mcp = FastMCP(Config.APP_NAME)

# --- 1. API 映射矩陣 ---
STOCK_ENDPOINT_MAP = {
    "realtime_quotes": "/exchangeReport/STOCK_DAY_ALL",
    "fundamental_eps": "/opendata/t187ap14_L",
    "dividend_yield": "/exchangeReport/BWIBBU_d",
    "chip_institutional_flow": "/fund/BFI82U",
    "margin_balance_monitor": "/exchangeReport/MI_MARGN",
    "listed_company_basic_info": "/opendata/t187ap03_L"
}

# --- 2. 核心邏輯分發器 ---

async def handle_mega_logic(name: str, symbol: Optional[str], limit: int) -> Any:
    try:
        # A. 台股類
        if name.startswith("stock_"):
            tool_id = name.replace("stock_", "")
            endpoint = STOCK_ENDPOINT_MAP.get(tool_id)
            if endpoint:
                return await StockLogic.call_generic_api(endpoint, symbol)
            return await StockLogic.get_realtime_quotes(symbol)

        # B. 匯率類 (優化後的市場實時匯率對接)
        elif name.startswith("forex_"):
            # 如果是銀行比價工具，目前先導向至實時市場匯率 (因無穩定官方 API)
            
            # 從 ID 自動提取幣別: forex_jpy_twd -> JPY
            parts = name.split("_")
            if len(parts) >= 2:
                cur_code = parts[1].upper()
                if cur_code not in ["BANK", "HISTORICAL", "ANALYSIS", "RATE", "GLOBAL"]:
                    return await ForexLogic.get_pair(cur_code, "TWD")
            
            # 處理通用換算問題
            if symbol: return await ForexLogic.get_pair(symbol.upper(), "TWD")
            return await ForexLogic.get_latest_rates()

        # C. 宏觀經濟類 (對接主計總處)
        elif name.startswith("macro_") or name.startswith("tax_"):
            indicator = "salary" if "salary" in name else "unemployment"
            if "participation" in name: indicator = "labor_participation"
            if "cpi" in name: indicator = "cpi"
            if "gdp" in name: indicator = "gdp"
            return await EconomicsLogic.get_macro_stats(indicator)

        # D. 加密貨幣 (對接 CoinGecko)
        elif name.startswith("crypto_"):
            coin = symbol if symbol else "bitcoin"
            return await CryptoLogic.get_price(coin)

        return {"error": f"工具 {name} 目前無真實數據對接邏輯。"}
    except Exception as e:
        return {"error": f"系統錯誤: {str(e)}"}

# --- 3. 動態工具註冊系統 ---

def register_all_tools():
    mega_map = {
        "stock": (STOCK_LIST, "台股分析"),
        "forex": (FOREX_LIST, "全球匯率"),
        "bank": (BANK_LIST, "銀行與信貸"),
        "tax": (TAX_LIST, "稅務法規"),
        "corp": (CORP_LIST, "企業統計"),
        "macro": (MACRO_LIST, "宏觀經濟"),
        "crypto": (CRYPTO_LIST, "Web3 監控")
    }
    
    for prefix, (tools, desc) in mega_map.items():
        for t_id in tools:
            tool_full_name = f"{prefix}_{t_id}"
            def make_tool(n, cat):
                @mcp.tool(name=n)
                async def finance_fn(symbol: Optional[str] = None, limit: int = 10) -> str:
                    """獲取官方 API 真實數據。"""
                    res = await handle_mega_logic(n, symbol, limit)
                    return json.dumps(res, indent=2, ensure_ascii=False)
                finance_fn.__name__ = name
                return finance_fn
            make_tool(tool_full_name, desc)

register_all_tools()

def main():
    parser = argparse.ArgumentParser(description="Taiwan Finance MCP Mega v3.3.3")
    parser.add_argument("--mode", choices=["stdio", "http"], default="stdio")
    parser.add_argument("--port", type=int, default=8000)
    args = parser.parse_args()
    
    if args.mode == "stdio":
        mcp.run()
    else:
        mcp.run(transport="streamable-http", host="0.0.0.0", port=args.port, path="/mcp")

if __name__ == "__main__":
    main()
