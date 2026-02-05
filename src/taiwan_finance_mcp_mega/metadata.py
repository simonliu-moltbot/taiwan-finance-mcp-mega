# Taiwan Finance MCP Mega - Rich Metadata Mapping (v3.8.1)

TOOL_METADATA = {
    # 📈 STOCK CORE
    "get_stock_quotes_realtime_all": "查詢台股上市個股當日即時行情。包含開盤、最高、最低、收盤價及成交量。數據源：臺灣證券交易所 (TWSE)。",
    "get_stock_eps_ranking_summary": "查詢台股上市公司每股盈餘 (EPS) 排名。適用於分析公司獲利能力與產業排名。數據源：臺灣證券交易所 (TWSE)。",
    "get_stock_dividend_yield_pe_pb": "獲取個股的本益比 (PE)、殖利率 (Yield) 及淨值比 (PB) 指標。評估投資價值的核心工具。數據源：TWSE。",
    "get_stock_institutional_investor_flow": "查詢三大法人（外資、投信、自營商）每日買賣超動向。用於分析主力資金流向。數據源：TWSE。",
    "get_stock_margin_trading_balance": "查詢全市場或特定個股的融資融券餘額與變動。適用於判斷市場籌碼熱度。數據源：TWSE。",
    "get_stock_odd_lot_trading_quotes": "查詢盤中零股交易的即時行情。包含零股成交價與買賣價量。小資存股必備工具。數據源：TWSE。",
    "get_stock_mops_significant_announcements": "查詢公開資訊觀測站 (MOPS) 的即時重大訊息公告。掌握公司經營動態與利多利空訊息。數據源：TWSE。",
    "get_stock_price_limit_up_down_tracker": "查詢集中市場漲跌停價預告與限制。用於監控盤中強勢或弱勢股。數據源：TWSE。",
    "get_stock_balance_sheet_general": "獲取公開發行公司（一般業）的資產負債表。分析總資產、負債與權益結構。數據源：TWSE。",
    "get_stock_monthly_revenue_summary": "查詢上市公司每月營業收入彙總。包含單月營收、去年同期增減%及累計營收。數據源：TWSE。",
    "get_stock_listed_company_basic_info": "獲取上市公司登記基本資料（統一編號、地址、發言人、資本額等）。數據源：TWSE。",
    "get_stock_etf_regular_savings_ranking": "查詢定期定額交易戶數統計排行榜。反映最受投資人歡迎的個股與 ETF 標的。數據源：TWSE。",
    "get_stock_block_trade_daily_summary": "查詢集中市場鉅額交易成交量值統計。追蹤大額資金交易行為。數據源：TWSE。",
    "get_stock_after_hours_trading_info": "查詢台股盤後定價交易行情與資訊。數據源：TWSE。",
    "get_stock_ipo_new_listing_schedule": "查詢台股新股上市 (IPO) 的公告與時程預告。數據源：TWSE。",
    "get_stock_buyback_treasury_status": "查詢上市公司買回庫藏股的執行進度與狀態。數據源：TWSE。",
    "get_stock_broker_regular_savings_data": "查詢目前開辦定期定額業務的證券商名單。數據源：TWSE。",

    # 🌿 STOCK ESG
    "get_stock_esg_greenhouse_gas_emissions": "查詢企業溫室氣體排放量 (範疇一/二/三)。適用於碳盤查分析。數據源：證交所永續揭露平台。",
    "get_stock_esg_energy_management_efficiency": "查詢企業能源管理使用率、再生能源佔比與能效指標。數據源：證交所 ESG 平台。",
    "get_stock_esg_occupational_safety_health": "查詢企業職業災害人數、比率及火災事件統計。數據源：證交所 ESG 平台。",
    "get_stock_esg_board_diversity_structure": "查詢董事會性別比例、席次組成與多元化指標。數據源：證交所 ESG 平台。",
    "get_stock_esg_food_safety_verification": "針對食品業，查詢食安管理制度、認證與檢驗支出統計。數據源：證交所 ESG 平台。",
    "get_stock_esg_information_security_breach": "查詢企業資訊安全外洩事件、影響人數及違規統計。數據源：證交所 ESG 平台。",

    # 🌍 FOREX & GLOBAL
    "get_forex_usd_twd_realtime": "查詢美金兌台幣的即時中間匯率。適用於外匯交易參考。數據源：ExchangeRate-API。",
    "get_forex_jpy_twd_realtime": "查詢日圓兌台幣的即時中間匯率。旅遊與進出口常用指標。數據源：ExchangeRate-API。",
    "get_commodity_oil_wti_price_usd": "查詢美國西德州原油 (WTI) 期貨即時報價 (USD)。全球能源核心指標。數據源：Yahoo Finance。",
    "get_commodity_oil_brent_price_usd": "查詢北海布蘭特原油 (Brent) 期貨即時報價 (USD)。數據源：Yahoo Finance。",
    "get_commodity_gold_spot_price_twd": "查詢黃金現貨即時報價 (TWD)。避險情緒觀察指標。數據源：Yahoo Finance。",
    "get_commodity_baltic_dry_index_bdi": "查詢波羅的海乾散貨指數 (BDI)。全球大宗物資貿易領先指標。數據源：Trading Economics。",

    # 🏛️ MACRO & GOV
    "get_macro_gdp_growth_rate_quarterly": "查詢台灣季度 GDP 經濟成長率。判斷台灣整體景氣循環的核心數據。數據源：行政院主計總處 (DGBAS)。",
    "get_macro_cpi_inflation_rate_tw": "查詢台灣消費者物價指數 (CPI) 年增率。監控通膨狀況的核心指標。數據源：行政院主計總處 (DGBAS)。",
    "get_macro_unemployment_rate_seasonal_adjusted": "查詢台灣經季節調整後的失業率。分析勞動市場供需。數據源：行政院主計總處 (DGBAS)。",
    "get_macro_average_monthly_salary_dgbas": "查詢台灣受僱員工每月平均總薪資。了解薪資水平趨勢。數據源：行政院主計總處 (DGBAS)。",
    "get_macro_fuel_price_cpc_retail": "查詢台灣中油 (CPC) 當週掛牌油價 (92/95/98/柴油)。台灣在地加油價參考。數據源：台灣中油。",
    "get_tax_revenue_collection_monthly": "查詢全國賦稅收入最新實徵淨額統計。數據源：財政部 (MOF)。",
    "get_corp_moea_business_registration": "查詢經濟部商工登記公示資料（統編、資本額、負責人、地址、公司狀態）。數據源：經濟部 (MOEA)。",
    "get_corp_industry_production_index": "查詢台灣工業生產指數與年增率。判斷製造業生產動能。數據源：經濟部 (MOEA)。",

    # 🪙 CRYPTO
    "get_crypto_btc_twd_price": "查詢比特幣 (Bitcoin) 即時報價 (TWD/USD) 與 24 小時漲跌幅。數據源：CoinGecko。",
    "get_crypto_eth_twd_price": "查詢以太幣 (Ethereum) 即時報價 (TWD/USD) 與 24 小時漲跌幅。數據源：CoinGecko。",
    "get_crypto_sol_twd_price": "查詢 Solana 即時報價 (TWD/USD) 與 24 小時漲跌幅。數據源：CoinGecko。",
    "get_crypto_market_fear_greed_index": "查詢加密貨幣市場恐慌與貪婪指數。數據源：CoinGecko。",
    
    # 🕒 COMMON
    "get_current_time_taipei": "獲取台北 (Asia/Taipei) 即時系統時間與星期幾。用於判斷盤中時段。數據源：System Clock。"
}
