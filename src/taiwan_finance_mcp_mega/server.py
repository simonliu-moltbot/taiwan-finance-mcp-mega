"""
Taiwan Finance MCP Mega v2.0.0
Refactored for maintainability with DevOps concepts.
Supports Streamable HTTP and STDIO.
"""
import sys
import argparse
import json
from fastmcp import FastMCP

# Core Logic Imports
from .config import Config
from .logic.stock import StockLogic
from .logic.forex import ForexLogic
from .logic.crypto import CryptoLogic
from .utils.http_client import AsyncHttpClient

# Initialize FastMCP
mcp = FastMCP(Config.APP_NAME)

# --- Stock Tools ---
@mcp.tool()
async def stock_day_all() -> str:
    """獲取台灣上市個股當日即時行情彙總。"""
    data = await StockLogic.get_day_all()
    return json.dumps(data[:10], indent=2, ensure_ascii=False) + f"\n... (Total {len(data)} items)"

@mcp.tool()
async def stock_monthly_revenue() -> str:
    """查詢公開發行公司最近一月營業收入。"""
    data = await StockLogic.get_monthly_revenue()
    return json.dumps(data[:5], indent=2, ensure_ascii=False)

# --- Forex Tools ---
@mcp.tool()
async def forex_rate(base: str = "USD") -> str:
    """查詢指定幣別對台幣 (TWD) 的即時匯率。預設為 USD。"""
    data = await ForexLogic.get_pair(base.upper(), "TWD")
    return json.dumps(data, indent=2)

# --- Crypto Tools ---
@mcp.tool()
async def crypto_price(coin_id: str = "bitcoin") -> str:
    """查詢加密貨幣即時報價。範例 ID: bitcoin, ethereum, solana。"""
    data = await CryptoLogic.get_price(coin_id)
    return json.dumps(data, indent=2)

@mcp.tool()
async def crypto_trending() -> str:
    """查詢 CoinGecko 當前熱搜加密貨幣排行。"""
    data = await CryptoLogic.get_trending()
    return json.dumps(data, indent=2, ensure_ascii=False)

def main():
    parser = argparse.ArgumentParser(description="Taiwan Finance MCP Mega Server")
    parser.add_argument("--mode", choices=["stdio", "http"], default="stdio", help="Transport mode")
    parser.add_argument("--port", type=int, default=Config.DEFAULT_HTTP_PORT, help="HTTP port")
    args = parser.parse_args()

    try:
        if args.mode == "stdio":
            mcp.run()
        else:
            print(f"Starting {Config.APP_NAME} v{Config.VERSION} in HTTP mode on port {args.port}...", file=sys.stderr)
            mcp.run(
                transport="streamable-http",
                host="0.0.0.0",
                port=args.port,
                path="/mcp"
            )
    finally:
        # Cleanup
        import asyncio
        asyncio.run(AsyncHttpClient.close())

if __name__ == "__main__":
    main()
