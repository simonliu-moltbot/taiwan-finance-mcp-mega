import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    # API Bases
    TWSE_BASE = "https://openapi.twse.com.tw/v1"
    TPEX_BASE = "https://openapi.tpex.org.tw/v1"
    FOREX_API = "https://open.er-api.com/v6/latest/JPY"
    COINGECKO_BASE = "https://api.coingecko.com/api/v3"
    
    # Server Settings
    APP_NAME = "taiwan-finance-mcp-mega"
    VERSION = "2.0.0"
    DEFAULT_HTTP_PORT = 8000
    
    # Logging
    LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
