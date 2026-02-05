"""
Taiwan Finance MCP Mega v2.7.3
Minimalist Stable Edition for Connection Testing.
"""
import sys
import argparse
import json
import logging
from fastmcp import FastMCP

# Absolute Imports
try:
    from taiwan_finance_mcp_mega.config import Config
except ImportError:
    # Fallback for direct script execution
    class Config:
        APP_NAME = "taiwan-finance-mcp"
        DEFAULT_HTTP_PORT = 8000

# Setup Logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("mcp-finance")

# Initialize FastMCP with name only
mcp = FastMCP(Config.APP_NAME)

@mcp.tool()
async def hello_finance() -> str:
    """測試工具：確認金融 MCP 伺服器已連線。"""
    return "👋 金融 MCP 伺服器已就緒！"

@mcp.tool()
async def get_test_data() -> str:
    """測試工具：回傳範例數據。"""
    return json.dumps({"status": "connected", "data": "Real API connection logic is ready."}, ensure_ascii=False)

def main():
    parser = argparse.ArgumentParser(description="Taiwan Finance MCP Mega Server")
    parser.add_argument("--mode", choices=["stdio", "http"], default="stdio")
    parser.add_argument("--port", type=int, default=8000)
    args = parser.parse_args()
    
    if args.mode == "stdio":
        logger.info("Starting in STDIO mode...")
        mcp.run()
    else:
        logger.info(f"Starting in Streamable HTTP mode on port {args.port}...")
        # Note: 'path' argument might be tricky depending on fastmcp version.
        # We will use the most basic run call.
        mcp.run(
            transport="streamable-http", 
            host="0.0.0.0", 
            port=args.port
        )

if __name__ == "__main__":
    main()
