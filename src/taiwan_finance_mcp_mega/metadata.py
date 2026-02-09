"""
Taiwan Finance MCP Mega - High-Contrast Metadata (v4.6.0)
Strict separation between Stock, Futures, and Macro tools.
"""

TOOL_METADATA = {
    # 📈 STOCK CORE: Purely for Securities Exchange (TWSE/TPEx)
    # MANDATORY: Only for stocks/ETFs listed on TWSE. Do NOT use for Futures.
    "get_stock_quotes_realtime_all": { "summary": "查詢台股上市個股即時行情。僅限現貨股票，不包含期貨。", "inputs": "ticker: 股票代碼 (例: 2330)。", "outputs": "開高低收、量、漲跌。", "source": "TWSE" },
    "get_stock_eps_ranking_summary": { "summary": "查詢上市公司 EPS 排名。僅針對已上市企業。", "inputs": "ticker: 股票代碼。", "outputs": "EPS、排名。", "source": "TWSE" },
    "get_stock_dividend_yield_pe_pb": { "summary": "獲取個股殖利率、PE、PB。僅限上市個股。", "inputs": "ticker: 股票代碼。", "outputs": "Yield, PE, PB。", "source": "TWSE" },
    "get_stock_institutional_investor_flow": { "summary": "查詢三大法人於股票現貨市場之買賣超 (上市)。", "inputs": "None", "outputs": "買賣超金額。", "source": "TWSE" },
    "get_stock_institutional_trading_tpex": { "summary": "查詢三大法人於櫃買市場 (上櫃) 之個股買賣超明細。", "inputs": "ticker: 股票代碼。", "outputs": "買賣超金額。", "source": "TPEx" },
    "get_stock_institutional_summary_tpex": { "summary": "查詢三大法人於櫃買市場 (上櫃) 之買賣超彙總統計。", "inputs": "None", "outputs": "合計買賣超。", "source": "TPEx" },
    "get_stock_margin_trading_balance": { "summary": "查詢股票現貨融資融券餘額。", "inputs": "ticker: 股票代碼。", "outputs": "餘額、增減。", "source": "TWSE" },
    "get_stock_odd_lot_trading_quotes": { "summary": "獲取股票盤中零股交易行情。非期貨。", "inputs": "ticker: 股票代碼。", "outputs": "成交價量。", "source": "TWSE" },
    "get_stock_mops_significant_announcements": { "summary": "查詢 MOPS 公開資訊觀測站重大訊息。僅限上市公司公告。", "inputs": "ticker: 股票代碼。", "outputs": "主旨、內容摘要。", "source": "TWSE" },
    "get_stock_price_limit_up_down_tracker": { "summary": "監控當日漲跌停股票清單。僅限現貨市場。", "inputs": "None", "outputs": "漲跌停清單。", "source": "TWSE" },
    "get_stock_balance_sheet_general": { "summary": "獲取上市公司資產負債表。", "inputs": "ticker: 股票代碼。", "outputs": "資產、負債總額。", "source": "TWSE" },
    "get_stock_monthly_revenue_summary": { "summary": "查詢上市公司每月營業收入彙總。", "inputs": "ticker: 股票代碼。", "outputs": "月增率、年增率。", "source": "TWSE" },
    "get_stock_listed_company_basic_info": { "summary": "獲取上市公司商工登記基本資料。", "inputs": "ticker: 股票代碼。", "outputs": "統編、地址、負責人。", "source": "TWSE" },
    "get_stock_etf_regular_savings_ranking": { "summary": "ETF 定期定額交易戶數排行。僅限 ETF 現貨。", "inputs": "None", "outputs": "排名、戶數。", "source": "TWSE" },
    "get_stock_block_trade_daily_summary": { "summary": "查詢股票集中市場鉅額交易。不包含期貨大額部位。", "inputs": "None", "outputs": "成交資訊。", "source": "TWSE" },
    "get_stock_after_hours_trading_info": { "summary": "獲取股票盤後定價交易資訊。", "inputs": "ticker: 股票代碼。", "outputs": "成交價量。", "source": "TWSE" },
    "get_stock_listed_stock_price_averages": { "summary": "上市公司本月股票收盤價與月平均價。包含個股本月平均價格。", "inputs": "None", "outputs": "收盤價、月平均價。", "source": "TWSE" },
    "get_stock_daily_closing_quotes_all": { "summary": "收盤指數及各類股成交量值。每日市場收盤總覽資訊。", "inputs": "None", "outputs": "指數、成交量值。", "source": "TWSE" },
    "get_stock_yield_averages_by_industry": { "summary": "上市公司各類股殖利率與現金殖利率統計。", "inputs": "None", "outputs": "類股殖利率。", "source": "TWSE" },
    "get_stock_pe_averages_by_industry": { "summary": "上市公司各類股本益比與殖利率統計。用於比較產業估值。", "inputs": "None", "outputs": "類股本益比。", "source": "TWSE" },
    "get_stock_broker_list_all": { "summary": "獲取全台證券商基本資料一覽表。包含券商名稱、地址與聯絡電話。", "inputs": "None", "outputs": "券商清單。", "source": "TWSE" },
    "get_stock_buyback_treasury_status": { "summary": "查詢上市公司庫藏股買回進度。", "inputs": "ticker: 股票代碼。", "outputs": "執行率。", "source": "TWSE" },
    "get_stock_broker_regular_savings_data": { "summary": "查詢開辦股票定期定額之證券商名單。", "inputs": "None", "outputs": "券商名單。", "source": "TWSE" },

    # 📉 DERIVATIVES: Specifically for TAIFEX (Futures/Options)
    # MANDATORY: Use ONLY for questions about 'Futures', 'Options', 'Open Interest', or 'Daily Settlement'.
    "get_futures_quotes_daily": { "summary": "獲取期交所期貨每日結算價與行情。包含台指期、金融期、電子期。非股票現貨。", "inputs": "None", "outputs": "結算價、未平倉。", "source": "Taifex" },
    "get_futures_institutional_investor_flow": { "summary": "查詢三大法人期貨未平倉留倉部位彙總。與股票買賣超不同，專指期貨合約。", "inputs": "None", "outputs": "多空淨額、未平倉量。", "source": "Taifex" },
    "get_futures_open_interest_ranking": { "summary": "查詢期貨市場大額交易人未平倉部位排名。用於追蹤期貨大戶動向。", "inputs": "None", "outputs": "大戶持倉比例、排名。", "source": "Taifex" },

    # 🌍 FOREX & COMMODITY
    "get_forex_usd_twd_realtime": { "summary": "美元兌台幣即時匯率。", "inputs": "None", "outputs": "Rate", "source": "tw.rter.info" },
    "get_forex_jpy_twd_realtime": { "summary": "日圓兌台幣即時匯率。", "inputs": "None", "outputs": "Rate", "source": "tw.rter.info" },
    "get_forex_eur_twd_realtime": { "summary": "歐元兌台幣即時匯率。", "inputs": "None", "outputs": "Rate", "source": "tw.rter.info" },
    "get_forex_cny_twd_realtime": { "summary": "人民幣兌台幣即時匯率。", "inputs": "None", "outputs": "Rate", "source": "tw.rter.info" },
    "get_forex_hkd_twd_realtime": { "summary": "港幣兌台幣即時匯率。", "inputs": "None", "outputs": "Rate", "source": "tw.rter.info" },
    "get_forex_gbp_twd_realtime": { "summary": "英鎊兌台幣即時匯率。", "inputs": "None", "outputs": "Rate", "source": "tw.rter.info" },
    "get_forex_aud_twd_realtime": { "summary": "澳幣兌台幣即時匯率。", "inputs": "None", "outputs": "Rate", "source": "tw.rter.info" },
    "get_forex_cad_twd_realtime": { "summary": "加幣兌台幣即時匯率。", "inputs": "None", "outputs": "Rate", "source": "tw.rter.info" },
    "get_forex_sgd_twd_realtime": { "summary": "新幣兌台幣即時匯率。", "inputs": "None", "outputs": "Rate", "source": "tw.rter.info" },
    "get_forex_krw_twd_realtime": { "summary": "韓元兌台幣即時匯率。", "inputs": "None", "outputs": "Rate", "source": "tw.rter.info" },
    "get_forex_any_to_any_conversion": { "summary": "任意幣別對任意幣別之即時匯率換算 (OOO to OOO)。", "inputs": "base: 原始幣別 (例: JPY), target: 目標幣別 (例: USD)。", "outputs": "計算後匯率。", "source": "tw.rter.info" },
    "get_commodity_oil_wti_price_usd": { "summary": "WTI 原油期貨報價(USD)。", "inputs": "None", "outputs": "USD/Bbl", "source": "MOEA" },
    "get_commodity_oil_brent_price_usd": { "summary": "Brent 原油期貨報價(USD)。", "inputs": "None", "outputs": "USD/Bbl", "source": "MOEA" },
    "get_commodity_gold_spot_price_twd": { "summary": "黃金現貨即時報價(TWD)。", "inputs": "None", "outputs": "TWD/oz", "source": "Yahoo" },
    "get_commodity_silver_spot_price_twd": { "summary": "白銀現貨即時報價(TWD)。", "inputs": "None", "outputs": "TWD/oz", "source": "Yahoo" },

    # 🏛️ MACRO: National Policy & Economy (DGBAS/CBC/MOF)
    "get_macro_gdp_growth_rate_quarterly": { "summary": "台灣季度 GDP 經濟成長率。國家級宏觀指標。", "inputs": "None", "outputs": "%", "source": "DGBAS" },
    "get_macro_cpi_inflation_rate_tw": { "summary": "台灣 CPI 消費者物價指數(通膨率)。國家級宏觀指標。", "inputs": "None", "outputs": "%", "source": "MOL" },
    "get_macro_unemployment_rate_seasonal_adjusted": { "summary": "台灣最新經季節調整後之失業率。國家級宏觀指標。", "inputs": "None", "outputs": "%", "source": "MOL" },
    "get_macro_average_monthly_salary_dgbas": { "summary": "台灣勞工月平均總薪資(含獎金)。國家級指標。", "inputs": "None", "outputs": "TWD", "source": "MOL" },
    "get_macro_central_bank_policy_rate": { "summary": "中央銀行重貼現率 (官方基準利率)。影響市場資金成本。非一般銀行存款利率。", "inputs": "None", "outputs": "%", "source": "CBC" },
    "get_macro_national_debt_clock": { "summary": "中華民國國債鐘：中央政府長短期債務與人均負擔額。", "inputs": "None", "outputs": "Debt Amount", "source": "MOF" },

    # 🏦 BANK: Commercial Bank specific metrics
    "get_bank_balance_sheets": { "summary": "獲取全體本國銀行資產負債表彙總。", "inputs": "None", "outputs": "規模結構。", "source": "CBC" },
    "get_bank_major_assets_liabilities_stats": { "summary": "獲取銀行主要資產負債項目 (存款、貸款、有價證券) 統計。", "inputs": "None", "outputs": "統計金額。", "source": "CBC" },
    "get_bank_sme_loan_balance_stats": { "summary": "獲取本國銀行對中小企業(SME)放款餘額與家數。", "inputs": "None", "outputs": "Balance (TWD)", "source": "FSC" },
    "get_bank_monthly_profit_summary": { "summary": "獲取銀行業每月稅前損益彙總。不包含稅務收入。", "inputs": "None", "outputs": "Profit", "source": "FSC" },
    "get_bank_overdue_loan_stats": { "summary": "查詢銀行資產品質：逾期放款 (NPL) 比率與備抵呆帳覆蓋率。", "inputs": "None", "outputs": "Ratio (%)", "source": "FSC" },
    "get_bank_foreign_exchange_trading_volume": { "summary": "查詢台北外匯指定銀行 (DBU) 交易量統計。", "inputs": "None", "outputs": "Volume", "source": "CBC" },
    "get_bank_deposit_rate_fixed": { "summary": "查詢本國銀行定期存款(一年期)之平均固定利率。非央行政策利率。", "inputs": "bank_query: 名稱。", "outputs": "Rate (%)", "source": "Banks" },
    "get_bank_mortgage_rate_average": { "summary": "個別商業銀行房貸利率查詢。非國家平均。", "inputs": "bank_query: 銀行名稱。", "outputs": "Rate (%)", "source": "Banks" },
    "get_bank_credit_card_delinquency": { "summary": "信用卡逾期帳款比率統計。", "inputs": "None", "outputs": "Ratio", "source": "FSC" },
    "get_bank_capital_adequacy_ratio": { "summary": "本國銀行資本適足率 (BIS) 統計。", "inputs": "None", "outputs": "Ratio", "source": "FSC" },

    # 🏢 CORP & INDUSTRY
    "get_corp_moea_business_registration": { "summary": "經濟部商工登記公示資料。查詢公司基本信息。", "inputs": "company_query: 公司名稱或統編。", "outputs": "登記資料。", "source": "MOEA" },
    "get_corp_industry_electricity_consumption_stats": { "summary": "各產業部門電力消費統計。判斷產業景氣。", "inputs": "None", "outputs": "GWh", "source": "MOEA" },

    # 📰 NEWS & GOV (Official Announcements)
    "get_gov_central_bank_announcements": { "summary": "獲取中央銀行(CBC)重要政策公告、理監事會議決議、外匯政策。", "inputs": "None", "outputs": "主旨、日期。", "source": "CBC" },
    "get_gov_industrial_policy_news_moea": { "summary": "獲取經濟部(MOEA)經貿、產業與能源政策動態新聞。", "inputs": "None", "outputs": "日期、主旨。", "source": "MOEA" },

    # 🪙 CRYPTO
    "get_crypto_btc_twd_price": { "summary": "比特幣 Bitcoin 即時 TWD/USD 報價與 24h 漲跌。", "inputs": "None", "outputs": "Price", "source": "CoinGecko" },
    "get_crypto_eth_twd_price": { "summary": "以太幣 Ethereum 即時 TWD/USD 報價與 24h 漲跌。", "inputs": "None", "outputs": "Rate", "source": "CoinGecko" },
    "get_crypto_sol_twd_price": { "summary": "Solana 即時報價與市場表現。", "inputs": "None", "outputs": "Price", "source": "CoinGecko" },
    "get_crypto_market_fear_greed_index": { "summary": "全球加密幣市場恐慌與貪婪指數。情緒判斷指標。", "inputs": "None", "outputs": "Index", "source": "CoinGecko" },
    
    # ⚖️ TAX
    "get_tax_revenue_collection_monthly": { "summary": "全國賦稅實徵淨額統計。國家稅收月報。", "inputs": "None", "outputs": "Revenue", "source": "MOF" },
    "get_tax_income_bracket_calculator": { "summary": "綜合所得稅級距、免稅額與試算公式。", "inputs": "None", "outputs": "Brackets", "source": "MOF" },
    "get_tax_electronic_invoice_usage_stats": { "summary": "電子發票普及率與張數統計。", "inputs": "None", "outputs": "Stats", "source": "MOF" },

    # 🕒 COMMON
    "get_current_time_taipei": { "summary": "獲取台北即時系統時間、日期與星期幾。", "inputs": "None", "outputs": "Timestamp", "source": "System" }
}
