# Taiwan Finance MCP Mega - Semantic Tool List Constants (v3.7.0)
# Naming Pattern: [action]_[category]_[specific_data]_[frequency/source]

STOCK_LIST = [
    "get_stock_quotes_realtime_all", "get_stock_eps_ranking_summary", "get_stock_dividend_yield_pe_pb", 
    "get_stock_institutional_investor_flow", "get_stock_margin_trading_balance", "get_stock_odd_lot_trading_quotes", 
    "get_stock_mops_significant_announcements", "get_stock_price_limit_up_down_tracker", "get_stock_balance_sheet_general", 
    "get_stock_monthly_revenue_summary", "get_stock_listed_company_basic_info", "get_stock_etf_regular_savings_ranking", 
    "get_stock_block_trade_daily_summary", "get_stock_after_hours_trading_info", "get_stock_ipo_new_listing_schedule",
    "get_stock_buyback_treasury_status", "get_stock_broker_regular_savings_data",
    
    # ESG (21 Semantic IDs)
    "get_stock_esg_greenhouse_gas_emissions", "get_stock_esg_energy_management_efficiency", 
    "get_stock_esg_water_resource_usage", "get_stock_esg_waste_management_data", 
    "get_stock_esg_human_capital_development", "get_stock_esg_board_diversity_structure", 
    "get_stock_esg_investor_communication_index", "get_stock_esg_climate_change_governance", 
    "get_stock_esg_functional_committee_status", "get_stock_esg_fuel_management_stats", 
    "get_stock_esg_product_life_cycle_management", "get_stock_esg_food_safety_verification", 
    "get_stock_esg_supply_chain_management_audit", "get_stock_esg_product_quality_safety", 
    "get_stock_esg_local_community_relations", "get_stock_esg_information_security_breach", 
    "get_stock_esg_inclusive_finance_promotion", "get_stock_esg_shareholding_control_power", 
    "get_stock_esg_risk_management_policy", "get_stock_esg_anti_competitive_litigation", 
    "get_stock_esg_occupational_safety_health"
]

FOREX_LIST = [
    "get_forex_usd_twd_realtime", "get_forex_jpy_twd_realtime", "get_forex_eur_twd_realtime", 
    "get_forex_cny_twd_realtime", "get_forex_hkd_twd_realtime", "get_forex_gbp_twd_realtime", 
    "get_forex_aud_twd_realtime", "get_forex_cad_twd_realtime", "get_forex_sgd_twd_realtime", 
    "get_forex_krw_twd_realtime",
    
    # Commodities (Semantic IDs)
    "get_commodity_oil_wti_price_usd", "get_commodity_oil_brent_price_usd", 
    "get_commodity_gold_spot_price_twd", "get_commodity_silver_spot_price_twd",
    "get_commodity_baltic_dry_index_bdi"
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
