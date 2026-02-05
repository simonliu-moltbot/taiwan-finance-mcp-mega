from fastmcp import FastMCP
import json
import logging
import sys

# Setup logging to stderr so Docker logs show it
logging.basicConfig(level=logging.DEBUG, stream=sys.stderr)
logger = logging.getLogger("mcp-server")

# Minimal self-contained server
mcp = FastMCP("taiwan-finance-mcp")

@mcp.tool()
async def health_check() -> str:
    """Check if the server is alive."""
    return "OK"

@mcp.tool()
async def echo(text: str) -> str:
    """Echo back the input text."""
    return f"You said: {text}"

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--mode", default="stdio")
    parser.add_argument("--port", type=int, default=8000)
    args = parser.parse_args()

    if args.mode == "stdio":
        mcp.run()
    else:
        logger.info(f"Starting Streamable HTTP server on port {args.port}")
        mcp.run(
            transport="streamable-http",
            host="0.0.0.0",
            port=args.port,
            path="/mcp"
        )
