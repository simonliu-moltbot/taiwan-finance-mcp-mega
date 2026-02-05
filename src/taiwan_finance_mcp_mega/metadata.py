"""
Taiwan Finance MCP Mega - Exhaustive Metadata Mapping (v4.3.2)
Finalizing Bank and Money Supply indicators.
"""

TOOL_METADATA = {
    # 📈 STOCK CORE (17 Tools)
    "get_stock_quotes_realtime_all": { "summary": "查詢台股上市個股即時行情。", "inputs": "symbol: 代碼。", "outputs": "開高低收、量、漲跌。", "source": "TWSE" },
    "get_stock_eps_ranking_summary": { "summary": "查詢上市公司 EPS 排名。", "inputs": "symbol: 代碼。", "outputs": "EPS、排名。", "source": "TWSE" },
    "get_stock_dividend_yield_pe_pb": { "summary": "獲取個股殖利率、PE、PB。", "inputs": "symbol: 代碼。", "outputs": "Yield, PE, PB。", "source": "TWSE" },
    "get_stock_institutional_investor_flow": { "summary": "查詢三大法人合計買賣超。", "inputs": "limit: 筆數。", "outputs": "買賣超金額。", "source": "TWSE" },
    "get_stock_margin_trading_balance": { "summary": "查詢融資融券餘額。", "inputs": "symbol: 代碼。", "outputs": "餘額、增減。", "source": "TWSE" },
    "get_stock_odd_lot_trading_quotes": { "summary": "獲取盤中零股交易行情。", "inputs": "symbol: 代碼。", "outputs": "成交價量。", "source": "TWSE" },
    "get_stock_mops_significant_announcements": { "summary": "查詢 MOPS 重大訊息公告。", "inputs": "symbol: 代碼。", "outputs": "主旨、內容摘要。", "source": "TWSE" },
    "get_stock_price_limit_up_down_tracker": { "summary": "監控漲跌停股票清單。", "inputs": "None", "outputs": "漲跌停清單。", "source": "TWSE" },
    "get_stock_balance_sheet_general": { "summary": "獲取公司資產負債表。", "inputs": "symbol: 代碼。", "outputs": "資產、負債總額。", "source": "TWSE" },
    "get_stock_monthly_revenue_summary": { "summary": "查詢每月營業收入彙總。", "inputs": "symbol: 代碼。", "outputs": "月增率、年增率。", "source": "TWSE" },
    "get_stock_listed_company_basic_info": { "summary": "獲取上市公司基本資料。", "inputs": "symbol: 代碼。", "outputs": "統編、地址、負責人。", "source": "TWSE" },
    "get_stock_etf_regular_savings_ranking": { "summary": "定期定額交易戶數排行。", "inputs": "None", "outputs": "排名、戶數。", "source": "TWSE" },
    "get_stock_block_trade_daily_summary": { "summary": "查詢鉅額交易成交量值。", "inputs": "None", "outputs": "成交資訊。", "source": "TWSE" },
    "get_stock_after_hours_trading_info": { "summary": "獲取盤後定價交易資訊。", "inputs": "symbol: 代碼。", "outputs": "成交價量。", "source": "TWSE" },
    "get_stock_ipo_new_listing_schedule": { "summary": "查詢新股上市 IPO 時程。", "inputs": "None", "outputs": "日期、公司。", "source": "TWSE" },
    "get_stock_buyback_treasury_status": { "summary": "查詢庫藏股買回進度。", "inputs": "symbol: 代碼。", "outputs": "執行率。", "source": "TWSE" },
    "get_stock_broker_regular_savings_data": { "summary": "查詢開辦定期定額之證券商。", "inputs": "None", "outputs": "券商名單。", "source": "TWSE" },

    # 📉 DERIVATIVES (3 Tools)
    "get_futures_quotes_daily": { "summary": "獲取期交所期貨收盤行情。", "inputs": "None", "outputs": "結算價。", "source": "Taifex" },
    "get_futures_institutional_investor_flow": { "summary": "查詢三大法人期貨未平倉。", "inputs": "None", "outputs": "未平倉量。", "source": "Taifex" },
    "get_futures_open_interest_ranking": { "summary": "查詢期貨大額部位統計。", "inputs": "None", "outputs": "大戶排名。", "source": "Taifex" },

    # 🌍 FOREX & GLOBAL (14 Tools)
    "get_forex_usd_twd_realtime": { "summary": "美元兌台幣即時匯率。", "inputs": "None", "outputs": "Rate", "source": "ExchangeRate-API" },
    "get_forex_jpy_twd_realtime": { "summary": "日圓兌台幣即時匯率。", "inputs": "None", "outputs": "Rate", "source": "ExchangeRate-API" },
    "get_forex_eur_twd_realtime": { "summary": "歐元兌台幣即時匯率。", "inputs": "None", "outputs": "Rate", "source": "ExchangeRate-API" },
    "get_forex_cny_twd_realtime": { "summary": "人民幣兌台幣即時匯率。", "inputs": "None", "outputs": "Rate", "source": "ExchangeRate-API" },
    "get_forex_hkd_twd_realtime": { "summary": "港幣兌台幣即時匯率。", "inputs": "None", "outputs": "Rate", "source": "ExchangeRate-API" },
    "get_forex_gbp_twd_realtime": { "summary": "英鎊兌台幣即時匯率。", "inputs": "None", "outputs": "Rate", "source": "ExchangeRate-API" },
    "get_forex_aud_twd_realtime": { "summary": "澳幣兌台幣即時匯率。", "inputs": "None", "outputs": "Rate", "source": "ExchangeRate-API" },
    "get_forex_cad_twd_realtime": { "summary": "加幣兌台幣即時匯率。", "inputs": "None", "outputs": "Rate", "source": "ExchangeRate-API" },
    "get_forex_sgd_twd_realtime": { "summary": "新幣兌台幣即時匯率。", "inputs": "None", "outputs": "Rate", "source": "ExchangeRate-API" },
    "get_forex_krw_twd_realtime": { "summary": "韓元兌台幣即時匯率。", "inputs": "None", "outputs": "Rate", "source": "ExchangeRate-API" },
    "get_commodity_oil_wti_price_usd": { "summary": "WTI 原油期貨報價。", "inputs": "None", "outputs": "USD/Bbl", "source": "MOEA" },
    "get_commodity_oil_brent_price_usd": { "summary": "Brent 原油期貨報價。", "inputs": "None", "outputs": "USD/Bbl", "source": "MOEA" },
    "get_commodity_gold_spot_price_twd": { "summary": "黃金現貨即時報價。", "inputs": "None", "outputs": "TWD/oz", "source": "Yahoo" },
    "get_commodity_silver_spot_price_twd": { "summary": "白銀現貨即時報價。", "inputs": "None", "outputs": "TWD/oz", "source": "Yahoo" },

    # 🏛️ MACRO & GOV (13 Tools)
    "get_macro_gdp_growth_rate_quarterly": { "summary": "台灣季度 GDP 成長率。", "inputs": "None", "outputs": "%", "source": "DGBAS" },
    "get_macro_cpi_inflation_rate_tw": { "summary": "台灣 CPI 通膨率。", "inputs": "None", "outputs": "%", "source": "MOL" },
    "get_macro_unemployment_rate_seasonal_adjusted": { "summary": "台灣季調後失業率。", "inputs": "None", "outputs": "%", "source": "MOL" },
    "get_macro_average_monthly_salary_dgbas": { "summary": "台灣月平均總薪資。", "inputs": "None", "outputs": "TWD", "source": "MOL" },
    "get_macro_fuel_price_cpc_retail": { "summary": "中油當週零售掛牌油價。", "inputs": "None", "outputs": "Price", "source": "CPC" },
    "get_macro_housing_price_index_tw": { "summary": "台灣全國住宅價格指數。", "inputs": "None", "outputs": "Index", "source": "Interior Ministry" },
    "get_tax_revenue_collection_monthly": { "summary": "全國賦稅收入月報。", "inputs": "None", "outputs": "Revenue", "source": "MOF" },
    "get_tax_income_bracket_calculator": { "summary": "綜所稅級距與試算公式。", "inputs": "None", "outputs": "Brackets", "source": "MOF" },
    "get_tax_electronic_invoice_usage_stats": { "summary": "電子發票普及率統計。", "inputs": "None", "outputs": "Stats", "source": "MOF" },
    "get_corp_moea_business_registration": { "summary": "經濟部商工登記公示資料。", "inputs": "symbol: 名稱。", "outputs": "登記資料。", "source": "MOEA" },
    "get_corp_industry_production_index": { "summary": "台灣工業生產指數。", "inputs": "None", "outputs": "Index", "source": "MOEA" },
    "get_corp_factory_count_statistics": { "summary": "全台工廠登記數統計。", "inputs": "None", "outputs": "Count", "source": "MOEA" },
    "get_corp_export_value_by_industry": { "summary": "各行業出口貿易總值。", "inputs": "None", "outputs": "Value", "source": "MOEA" },

    # 🪙 CRYPTO (4 Tools)
    "get_crypto_btc_twd_price": { "summary": "比特幣 TWD/USD 報價。", "inputs": "None", "outputs": "Price", "source": "CoinGecko" },
    "get_crypto_eth_twd_price": { "summary": "以太幣 TWD/USD 報價。", "inputs": "None", "outputs": "Price", "source": "CoinGecko" },
    "get_crypto_sol_twd_price": { "summary": "Solana 即時價格。", "inputs": "None", "outputs": "Price", "source": "CoinGecko" },
    "get_crypto_market_fear_greed_index": { "summary": "加密幣市場恐慌貪婪指數。", "inputs": "None", "outputs": "Index", "source": "CoinGecko" },
    
    # 🏦 BANK (13 Tools)
    "get_bank_list_of_institutions": { "summary": "獲取台灣金融機構一覽表。", "inputs": "None", "outputs": "機構名稱、代號。", "source": "CBC" },
    "get_bank_profit_loss_statements": { "summary": "獲取本國銀行損益表彙總。", "inputs": "None", "outputs": "損益數據。", "source": "CBC" },
    "get_bank_balance_sheets": { "summary": "獲取本國銀行資產負債表。", "inputs": "None", "outputs": "規模結構。", "source": "CBC" },
    "get_bank_major_assets_liabilities_stats": { "summary": "獲取本國銀行主要資產負債項目。", "inputs": "None", "outputs": "存貸款統計。", "source": "CBC" },
    "get_bank_m1b_m2_money_supply": { "summary": "查詢貨幣總計數 M1B/M2 年增率。", "inputs": "None", "outputs": "%。", "source": "CBC" },
    "get_bank_foreign_exchange_reserves": { "summary": "查詢台灣外匯存底統計。", "inputs": "None", "outputs": "USD 億元。", "source": "CBC" },
    "get_bank_central_bank_base_rate": { "summary": "中央銀行基準利率(重貼現率)。", "inputs": "None", "outputs": "%", "source": "CBC" },
    "get_bank_five_major_banks_loan_rates": { "summary": "五大銀行新承做放款利率(含房貸)。", "inputs": "None", "outputs": "Rate (%)", "source": "CBC" },
    "get_bank_sme_loan_balance_stats": { "summary": "獲取本國銀行對中小企業放款餘額。", "inputs": "None", "outputs": "Balance (TWD)", "source": "FSC" },
    "get_bank_monthly_profit_summary": { "summary": "獲取銀行業每月獲利損益摘要。", "inputs": "None", "outputs": "Profit", "source": "FSC" },
    "get_bank_foreign_exchange_trading_volume": { "summary": "查詢外匯指定銀行交易量統計。", "inputs": "None", "outputs": "Volume", "source": "CBC" },
    "get_bank_overdue_loan_stats": { "summary": "查詢銀行逾期放款與資產品質。", "inputs": "None", "outputs": "Ratio", "source": "FSC" },
    "get_bank_capital_adequacy_ratio": { "summary": "本國銀行資本適足率。", "inputs": "None", "outputs": "Ratio", "source": "FSC" },

    # 🕒 COMMON (1 Tool)
    "get_current_time_taipei": { "summary": "獲取台北即時系統時間與星期幾。", "inputs": "None", "outputs": "Timestamp", "source": "System" }
}
