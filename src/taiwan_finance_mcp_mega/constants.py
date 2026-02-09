# Taiwan Finance MCP Mega - High-Contrast Tool List Constants (v4.6.0)

# 📈 STOCK: Purely for Securities Exchange (TWSE/TPEx)
STOCK_LIST = [
    "get_stock_quotes_realtime_all", "get_stock_eps_ranking_summary", "get_stock_dividend_yield_pe_pb", 
    "get_stock_institutional_investor_flow", "get_stock_institutional_trading_tpex", "get_stock_institutional_summary_tpex",
    "get_stock_margin_trading_balance", "get_stock_odd_lot_trading_quotes", 
    "get_stock_mops_significant_announcements", "get_stock_price_limit_up_down_tracker", "get_stock_balance_sheet_general", 
    "get_stock_monthly_revenue_summary", "get_stock_listed_company_basic_info", "get_stock_etf_regular_savings_ranking", 
    "get_stock_block_trade_daily_summary", "get_stock_after_hours_trading_info",
    "get_stock_listed_stock_price_averages", "get_stock_daily_closing_quotes_all",
    "get_stock_yield_averages_by_industry", "get_stock_pe_averages_by_industry",
    "get_stock_broker_list_all",
    "get_stock_buyback_treasury_status", "get_stock_broker_regular_savings_data"
]

# 🌍 FOREX & COMMODITY
FOREX_LIST = [
    "get_forex_usd_twd_realtime", "get_forex_jpy_twd_realtime", "get_forex_eur_twd_realtime", 
    "get_forex_cny_twd_realtime", "get_forex_hkd_twd_realtime", "get_forex_gbp_twd_realtime", 
    "get_forex_aud_twd_realtime", "get_forex_cad_twd_realtime", "get_forex_sgd_twd_realtime", 
    "get_forex_krw_twd_realtime", "get_forex_any_to_any_conversion",
    "get_commodity_oil_wti_price_usd", "get_commodity_oil_brent_price_usd", 
    "get_commodity_gold_spot_price_twd"
]

# 📉 DERIVATIVES: Specifically for TAIFEX (Futures/Options)
DERIVATIVES_LIST = [
    "get_futures_quotes_daily", "get_futures_institutional_investor_flow", "get_futures_open_interest_ranking"
]

# 🏦 BANK: Commercial Bank specific metrics
BANK_LIST = []

# 🏛️ MACRO: National Policy & Economy (DGBAS/CBC/MOF)
MACRO_LIST = [
    "get_macro_gdp_growth_rate_quarterly",
    "get_macro_national_debt_clock",
    "get_macro_monthly_financial_indicators"
]

TAX_LIST = []

CORP_LIST = [
    "get_corp_moea_business_registration"
]

NEWS_LIST = []

CRYPTO_LIST = [
    "get_crypto_btc_twd_price", "get_crypto_eth_twd_price", "get_crypto_sol_twd_price",
    "get_crypto_market_fear_greed_index"
]

COMMON_LIST = [
    "get_current_time_taipei"
]
