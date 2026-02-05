"""
Taiwan Finance MCP Mega - Exhaustive Metadata Mapping (v4.0.0)
Removed ESG category as requested by the user due to data source limitations.
"""

TOOL_METADATA = {
    # 📈 STOCK CORE (17 Tools)
    "get_stock_quotes_realtime_all": "獲取台股集中市場所有個股當日即時行情。包含開盤、最高、最低、收盤價、漲跌幅及成交量。數據源：臺灣證券交易所 (TWSE)。",
    "get_stock_eps_ranking_summary": "查詢台股上市公司每股盈餘 (EPS) 排名彙總。用於分析企業獲利能力與同產業競爭力排名。數據源：TWSE。",
    "get_stock_dividend_yield_pe_pb": "查詢上市個股的殖利率、本益比 (PE) 與股價淨值比 (PB) 估值數據。長期存股與估值核心指標。數據源：TWSE。",
    "get_stock_institutional_investor_flow": "獲取三大法人（外資、投信、自營商）合計買賣超彙總。判斷市場主力資金流向與籌碼面變化。數據源：TWSE。",
    "get_stock_margin_trading_balance": "查詢全市場融資融券餘額明細與變動。用於分析散戶熱度與空方籌碼動向。數據源：TWSE。",
    "get_stock_odd_lot_trading_quotes": "查詢盤中零股交易即時行情（1-999股）。包含成交價、買賣委託價量。小資存股族專用工具。數據源：TWSE。",
    "get_stock_mops_significant_announcements": "查詢公開資訊觀測站 (MOPS) 即時重大訊息。包含經營權變動、財務預警、利多利空公告等。數據源：TWSE。",
    "get_stock_price_limit_up_down_tracker": "監控當日觸及或預告漲跌停價的股票清單。用於捕捉市場極端行情與強勢股。數據源：TWSE。",
    "get_stock_balance_sheet_general": "獲取公開發行公司資產負債表彙總（一般業）。分析公司流動性、負債比與資產結構。數據源：TWSE。",
    "get_stock_monthly_revenue_summary": "查詢上市公司每月營業收入彙總。包含單月營收、去年同期增減、MoM 與 YoY。分析成長動能核心數據。數據源：TWSE。",
    "get_stock_listed_company_basic_info": "獲取上市公司登記基本資料（統一編號、負責人、地址、資本額、發言人、官網）。數據源：TWSE。",
    "get_stock_etf_regular_savings_ranking": "查詢定期定額交易戶數統計排行榜（個股與 ETF 分別排行）。反映長期投資人的標的偏好。數據源：TWSE。",
    "get_stock_block_trade_daily_summary": "查詢集中市場鉅額交易成交量值統計表。追蹤大額資金法人交易動向。數據源：TWSE。",
    "get_stock_after_hours_trading_info": "獲取集中市場盤後定價交易資訊。查詢收盤後的穩定成交價格與量。數據源：TWSE。",
    "get_stock_ipo_new_listing_schedule": "查詢台股新股上市 (IPO) 公告、申購時程與新掛牌進度。數據源：TWSE。",
    "get_stock_buyback_treasury_status": "查詢上市公司執行買回庫藏股的進度、金額與股數統計。數據源：TWSE。",
    "get_stock_broker_regular_savings_data": "查詢目前開辦定期定額業務的證券商名單與承作規定。數據源：TWSE。",

    # 🌍 FOREX & GLOBAL (15 Tools)
    "get_forex_usd_twd_realtime": "查詢美金 (USD) 兌換新台幣 (TWD) 的即時市場中間匯率。數據源：Real-time ExchangeRate-API。",
    "get_forex_jpy_twd_realtime": "查詢日圓 (JPY) 兌換新台幣 (TWD) 的即時市場中間匯率。適用於旅遊與進出口。數據源：ExchangeRate-API。",
    "get_forex_eur_twd_realtime": "查詢歐元 (EUR) 兌換新台幣 (TWD) 的即時市場中間匯率。數據源：ExchangeRate-API。",
    "get_forex_cny_twd_realtime": "查詢人民幣 (CNY) 兌換新台幣 (TWD) 的即時市場中間匯率。數據源：ExchangeRate-API。",
    "get_forex_hkd_twd_realtime": "查詢港幣 (HKD) 兌換新台幣 (TWD) 的即時市場中間匯率。數據源：ExchangeRate-API。",
    "get_forex_gbp_twd_realtime": "查詢英鎊 (GBP) 兌換新台幣 (TWD) 的即時市場中間匯率。數據源：ExchangeRate-API。",
    "get_forex_aud_twd_realtime": "查詢澳幣 (AUD) 兌換新台幣 (TWD) 的即時市場中間匯率。數據源：ExchangeRate-API。",
    "get_forex_cad_twd_realtime": "查詢加幣 (CAD) 兌換新台幣 (TWD) 的即時市場中間匯率。數據源：ExchangeRate-API。",
    "get_forex_sgd_twd_realtime": "查詢新幣 (SGD) 兌換新台幣 (TWD) 的即時市場中間匯率。數據源：ExchangeRate-API。",
    "get_forex_krw_twd_realtime": "查詢韓元 (KRW) 兌換新台幣 (TWD) 的即時市場中間匯率。數據源：ExchangeRate-API。",
    "get_commodity_oil_wti_price_usd": "查詢美國西德州原油 (WTI) 報價 (USD/Barrel)。數據源：經濟部能源署 (MOEA)。",
    "get_commodity_oil_brent_price_usd": "查詢北海布蘭特原油 (Brent) 報價 (USD/Barrel)。數據源：經濟部能源署 (MOEA)。",
    "get_commodity_gold_spot_price_twd": "查詢國際黃金現貨即時行情（對台幣報價）。避險資產核心參考。數據源：Yahoo Finance。",
    "get_commodity_silver_spot_price_twd": "查詢國際白銀現貨即時行情（對台幣報價）。工業與投資性貴金屬參考。數據源：Yahoo Finance。",
    "get_commodity_baltic_dry_index_bdi": "查詢波羅的海乾散貨指數 (BDI)。全球大宗原物料航運運費的重要指標。",

    # 🏛️ MACRO & GOV (13 Tools)
    "get_macro_gdp_growth_rate_quarterly": "查詢台灣季度 GDP 經濟成長率 (%)。衡量台灣整體經濟擴張或衰退的最權威指標。數據源：行政院主計總處 (DGBAS)。",
    "get_macro_cpi_inflation_rate_tw": "查詢台灣消費者物價指數 (CPI) 年增率。判斷通膨狀況的重要依據。數據源：勞動部年度主要指標 (MOL)。",
    "get_macro_unemployment_rate_seasonal_adjusted": "查詢台灣最新失業率百分比。分析台灣就業市場供需。數據源：勞動部年度主要指標 (MOL)。",
    "get_macro_average_monthly_salary_dgbas": "查詢台灣受僱員工每月平均名目總薪資。數據源：勞動部年度主要指標 (MOL)。",
    "get_macro_fuel_price_cpc_retail": "查詢台灣中油 (CPC) 當週掛牌零售油價（92/95/98無鉛、超級柴油）。台灣在地生活成本參考。數據源：台灣中油。",
    "get_tax_revenue_collection_monthly": "查詢全國各項賦稅收入最新月份的實徵淨額與年度累計統計。數據源：財政部 (MOF)。",
    "get_tax_income_bracket_calculator": "獲取台灣綜合所得稅級距與免稅額試算資料。數據源：財政部。",
    "get_tax_electronic_invoice_usage_stats": "查詢台灣電子發票普及統計。數據源：財政部。",
    "get_corp_moea_business_registration": "獲取經濟部商工登記公示資料（統一編號、代表人、地址、資本額、經營狀態）。數據源：經濟部 (MOEA)。",
    "get_corp_industry_production_index": "查詢台灣工業生產指數與年增率。判斷製造業生產動能。數據源：經濟部 (MOEA)。",
    "get_corp_factory_count_statistics": "查詢台灣各縣市工廠登記數量統計。數據源：經濟部 (MOEA)。",
    "get_corp_export_value_by_industry": "查詢按行業別劃分之出口貿易總值統計（美元）。數據源：經濟部 (MOEA)。",
    "get_crypto_market_fear_greed_index": "查詢全球加密貨幣市場恐慌與貪婪指數。數據源：CoinGecko。",

    # 🪙 CRYPTO (3 Core Tools)
    "get_crypto_btc_twd_price": "查詢比特幣 (Bitcoin) 的台幣與美金即時報價、24小時漲跌幅。數據源：CoinGecko。",
    "get_crypto_eth_twd_price": "查詢以太幣 (Ethereum) 的台幣與美金即時報價、24小時漲跌幅。數據源：CoinGecko。",
    "get_crypto_sol_twd_price": "查詢 Solana 的即時報價與 24 小時漲跌變動。數據源：CoinGecko。",
    
    # 🏦 BANK
    "get_bank_deposit_rate_fixed": "查詢台灣主要銀行定期存款利率。數據源：中央銀行。",
    "get_bank_mortgage_rate_average": "查詢台灣平均購屋貸款利率趨勢。數據源：中央銀行。",
    "get_bank_credit_card_delinquency": "信用卡逾期帳款統計。數據源：金管會。",
    "get_bank_atm_location_map": "全台 ATM 網點設置位置分布統計。數據源：金管會。",
    "get_bank_capital_adequacy_ratio": "本國銀行資本適足率指標。數據源：金管會。",

    # 🕒 COMMON (1 Tool)
    "get_current_time_taipei": "獲取台北 (Asia/Taipei) 現下的精確系統時間。用於確認盤中、盤後或例假日狀態。"
}
