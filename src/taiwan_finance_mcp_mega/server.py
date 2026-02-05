"""
Taiwan Finance MCP Mega v2.7.4
Extreme Stability Edition.
Ensures correct path and dependencies for Dive/Cherry Studio.
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
    class Config:
        APP_NAME = "taiwan-finance-mcp"
        DEFAULT_HTTP_PORT = 8000

# Setup Logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger("mcp-finance")

# Initialize FastMCP
mcp = FastMCP(Config.APP_NAME)

@mcp.tool()
async def hello_finance() -> str:
    """測試工具：確認金融 MCP 伺服器已連線。"""
    return "👋 金融 MCP 伺服器已就緒！"

def main():
    parser = argparse.ArgumentParser(description="Taiwan Finance MCP Mega Server")
    parser.add_argument("--mode", choices=["stdio", "http"], default="stdio")
    parser.add_argument("--port", type=int, default=8000)
    args = parser.parse_args()
    
    if args.mode == "stdio":
        logger.info("Starting in STDIO mode...")
        mcp.run()
    else:
        logger.info(f"Starting in Streamable HTTP mode on 0.0.0.0:{args.port}/mcp")
        # Explicitly set path to /mcp to match common client expectations
        mcp.run(
            transport="streamable-http", 
            host="0.0.0.0", 
            port=args.port,
            path="/mcp"
        )

if __name__ == "__main__":
    main()
