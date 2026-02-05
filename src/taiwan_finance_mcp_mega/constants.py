# Taiwan Finance MCP Mega - Semantic Tool List Constants (v4.1.0)

STOCK_LIST = [
    "get_stock_quotes_realtime_all", "get_stock_eps_ranking_summary", "get_stock_dividend_yield_pe_pb", 
    "get_stock_institutional_investor_flow", "get_stock_margin_trading_balance", "get_stock_odd_lot_trading_quotes", 
    "get_stock_mops_significant_announcements", "get_stock_price_limit_up_down_tracker", "get_stock_balance_sheet_general", 
    "get_stock_monthly_revenue_summary", "get_stock_listed_company_basic_info", "get_stock_etf_regular_savings_ranking", 
    "get_stock_block_trade_daily_summary", "get_stock_after_hours_trading_info", "get_stock_ipo_new_listing_schedule",
    "get_stock_buyback_treasury_status", "get_stock_broker_regular_savings_data"
]

FOREX_LIST = [
    "get_forex_usd_twd_realtime", "get_forex_jpy_twd_realtime", "get_forex_eur_twd_realtime", 
    "get_forex_cny_twd_realtime", "get_forex_hkd_twd_realtime", "get_forex_gbp_twd_realtime", 
    "get_forex_aud_twd_realtime", "get_forex_cad_twd_realtime", "get_forex_sgd_twd_realtime", 
    "get_forex_krw_twd_realtime",
    
    # Commodities (Government Source for Oil)
    "get_commodity_oil_wti_price_usd", "get_commodity_oil_brent_price_usd", 
    "get_commodity_gold_spot_price_twd", "get_commodity_silver_spot_price_twd"
]

BANK_LIST = [
    "get_bank_deposit_rate_fixed", "get_bank_mortgage_rate_average", "get_bank_credit_card_delinquency",
    "get_bank_atm_location_map", "get_bank_capital_adequacy_ratio"
]

TAX_LIST = [
    "get_tax_income_bracket_calculator", "get_tax_revenue_collection_monthly", 
    "get_tax_electronic_invoice_usage_stats"
]

CORP_LIST = [
    "get_corp_moea_business_registration", "get_corp_industry_production_index", 
    "get_corp_factory_count_statistics", "get_corp_export_value_by_industry"
]

MACRO_LIST = [
    "get_macro_gdp_growth_rate_quarterly", "get_macro_cpi_inflation_rate_tw", 
    "get_macro_unemployment_rate_seasonal_adjusted", "get_macro_average_monthly_salary_dgbas",
    "get_macro_fuel_price_cpc_retail"
]

CRYPTO_LIST = [
    "get_crypto_btc_twd_price", "get_crypto_eth_twd_price", "get_crypto_sol_twd_price",
    "get_crypto_market_fear_greed_index"
]

COMMON_LIST = [
    "get_current_time_taipei"
]
