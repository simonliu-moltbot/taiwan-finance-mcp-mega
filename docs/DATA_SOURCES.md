# Direct API Endpoint Registry (Full Coverage)

This document provides a 100% exhaustive mapping of every tool registered in the `taiwan-finance-mcp-mega` project to its specific data source and API endpoint.

---

## 📈 Stock Market (TWSE / TPEx)
*Exhaustive list of all tools in STOCK_LIST.*

| Tool Name | Direct API URL (Source) | Description (說明) |
|-----------|-------------------------|-------------------|
| `get_stock_quotes_realtime_all` | [https://openapi.twse.com.tw/v1/exchangeReport/STOCK_DAY_ALL](https://openapi.twse.com.tw/v1/exchangeReport/STOCK_DAY_ALL) | 上市個股當日即時行情 |
| `get_stock_eps_ranking_summary` | [https://openapi.twse.com.tw/v1/opendata/t187ap14_L](https://openapi.twse.com.tw/v1/opendata/t187ap14_L) | 各產業 EPS 統計資訊 |
| `get_stock_dividend_yield_pe_pb` | [https://openapi.twse.com.tw/v1/exchangeReport/BWIBBU_d](https://openapi.twse.com.tw/v1/exchangeReport/BWIBBU_d) | 個股日本益比、殖利率及淨值比 |
| `get_stock_institutional_investor_flow` | [https://www.twse.com.tw/zh/page/trading/fund/BFI82U.html](https://www.twse.com.tw/zh/page/trading/fund/BFI82U.html) | 三大法人買賣超彙總統計 (上市) |
| `get_stock_institutional_trading_tpex` | [https://www.tpex.org.tw/openapi/v1/tpex_3insti_daily_trading](https://www.tpex.org.tw/openapi/v1/tpex_3insti_daily_trading) | 三大法人買賣超明細 (上櫃個股) |
| `get_stock_institutional_summary_tpex` | [https://www.tpex.org.tw/openapi/v1/tpex_3insti_summary](https://www.tpex.org.tw/openapi/v1/tpex_3insti_summary) | 三大法人買賣超彙總統計 (上櫃) |
| `get_stock_margin_trading_balance` | [https://openapi.twse.com.tw/v1/exchangeReport/MI_MARGN](https://openapi.twse.com.tw/v1/exchangeReport/MI_MARGN) | 融資融券餘額明細 |
| `get_stock_odd_lot_trading_quotes` | [https://openapi.twse.com.tw/v1/exchangeReport/TWT53U](https://openapi.twse.com.tw/v1/exchangeReport/TWT53U) | 盤中零股交易即時行情 |
| `get_stock_mops_significant_announcements` | [https://openapi.twse.com.tw/v1/opendata/t187ap04_L](https://openapi.twse.com.tw/v1/opendata/t187ap04_L) | 每日重大訊息公告 (MOPS) |
| `get_stock_price_limit_up_down_tracker` | [https://openapi.twse.com.tw/v1/exchangeReport/TWT84U](https://openapi.twse.com.tw/v1/exchangeReport/TWT84U) | 股價升降幅度/漲跌停預告 |
| `get_stock_balance_sheet_general` | [https://openapi.twse.com.tw/v1/opendata/t187ap07_X_ci](https://openapi.twse.com.tw/v1/opendata/t187ap07_X_ci) | 資產負債表-一般業 |
| `get_stock_monthly_revenue_summary` | [https://openapi.twse.com.tw/v1/opendata/t187ap05_L](https://openapi.twse.com.tw/v1/opendata/t187ap05_L) | 每月營業收入彙總表 |
| `get_stock_listed_company_basic_info` | [https://openapi.twse.com.tw/v1/opendata/t187ap03_L](https://openapi.twse.com.tw/v1/opendata/t187ap03_L) | 上市公司基本資料 |
| `get_stock_etf_regular_savings_ranking` | [https://openapi.twse.com.tw/v1/ETFReport/ETFRank](https://openapi.twse.com.tw/v1/ETFReport/ETFRank) | ETF 定期定額交易戶數排行 |
| `get_stock_block_trade_daily_summary` | [https://openapi.twse.com.tw/v1/block/BFIAUU_d](https://openapi.twse.com.tw/v1/block/BFIAUU_d) | 鉅額交易日成交量值統計 |
| `get_stock_after_hours_trading_info` | [https://openapi.twse.com.tw/v1/exchangeReport/BFT41U](https://openapi.twse.com.tw/v1/exchangeReport/BFT41U) | 盤後定價交易資訊 |
| `get_stock_listed_stock_price_averages` | [https://openapi.twse.com.tw/v1/exchangeReport/STOCK_DAY_AVG_ALL](https://openapi.twse.com.tw/v1/exchangeReport/STOCK_DAY_AVG_ALL) | 上市公司收盤價及月平均價 |
| `get_stock_daily_closing_quotes_all` | [https://openapi.twse.com.tw/v1/exchangeReport/MI_INDEX](https://openapi.twse.com.tw/v1/exchangeReport/MI_INDEX) | 收盤指數及各類股成交量值 |
| `get_stock_yield_averages_by_industry` | [https://openapi.twse.com.tw/v1/exchangeReport/FMSRFK_ALL](https://openapi.twse.com.tw/v1/exchangeReport/FMSRFK_ALL) | 上市公司各類股殖利率統計 |
| `get_stock_pe_averages_by_industry` | [https://openapi.twse.com.tw/v1/exchangeReport/FMNPTK_ALL](https://openapi.twse.com.tw/v1/exchangeReport/FMNPTK_ALL) | 上市公司各類股本益比統計 |
| `get_stock_broker_list_all` | [https://openapi.twse.com.tw/v1/brokerService/brokerList](https://openapi.twse.com.tw/v1/brokerService/brokerList) | 證券商基本資料一覽表 |
| `get_stock_buyback_treasury_status` | [https://openapi.twse.com.tw/v1/opendata/t187ap13_L](https://openapi.twse.com.tw/v1/opendata/t187ap13_L) | 庫藏股買回進度彙整 |
| `get_stock_broker_regular_savings_data` | [https://openapi.twse.com.tw/v1/brokerService/secRegData](https://openapi.twse.com.tw/v1/brokerService/secRegData) | 開辦定期定額業務證券商名單 |

## 🌍 Forex & Commodities
*Exhaustive list of all tools in FOREX_LIST.*

| Tool Name | Direct API URL (Source) | Description (說明) |
|-----------|-------------------------|-------------------|
| `get_forex_usd_twd_realtime` | [https://tw.rter.info/capi.php](https://tw.rter.info/capi.php) | 美元兌台幣即時匯率 |
| `get_forex_jpy_twd_realtime` | [https://tw.rter.info/capi.php](https://tw.rter.info/capi.php) | 日圓兌台幣即時匯率 |
| `get_forex_eur_twd_realtime` | [https://tw.rter.info/capi.php](https://tw.rter.info/capi.php) | 歐元兌台幣即時匯率 |
| `get_forex_cny_twd_realtime` | [https://tw.rter.info/capi.php](https://tw.rter.info/capi.php) | 人民幣兌台幣即時匯率 |
| `get_forex_hkd_twd_realtime` | [https://tw.rter.info/capi.php](https://tw.rter.info/capi.php) | 港幣兌台幣即時匯率 |
| `get_forex_gbp_twd_realtime` | [https://tw.rter.info/capi.php](https://tw.rter.info/capi.php) | 英鎊兌台幣即時匯率 |
| `get_forex_aud_twd_realtime` | [https://tw.rter.info/capi.php](https://tw.rter.info/capi.php) | 澳幣兌台幣即時匯率 |
| `get_forex_cad_twd_realtime` | [https://tw.rter.info/capi.php](https://tw.rter.info/capi.php) | 加幣兌台幣即時匯率 |
| `get_forex_sgd_twd_realtime` | [https://tw.rter.info/capi.php](https://tw.rter.info/capi.php) | 新幣兌台幣即時匯率 |
| `get_forex_krw_twd_realtime` | [https://tw.rter.info/capi.php](https://tw.rter.info/capi.php) | 韓元兌台幣即時匯率 |
| `get_forex_any_to_any_conversion` | [https://tw.rter.info/capi.php](https://tw.rter.info/capi.php) | 任意幣別對任意幣別即時換算 |
| `get_commodity_oil_wti_price_usd` | [https://www2.moeaea.gov.tw/oil111/csv/GlobalOilOpenData.csv](https://www2.moeaea.gov.tw/oil111/csv/GlobalOilOpenData.csv) | WTI 原油期貨報價(USD) |
| `get_commodity_oil_brent_price_usd` | [https://www2.moeaea.gov.tw/oil111/csv/GlobalOilOpenData.csv](https://www2.moeaea.gov.tw/oil111/csv/GlobalOilOpenData.csv) | Brent 原油期貨報價(USD) |
| `get_commodity_gold_spot_price_twd` | [https://www.tpex.org.tw/openapi/v1/gold_DailyQuotes](https://www.tpex.org.tw/openapi/v1/gold_DailyQuotes) | 黃金現貨即時報價(TWD) |

## 📉 Derivatives (Taifex)
*Exhaustive list of all tools in DERIVATIVES_LIST.*

| Tool Name | Direct API URL (Source) | Description (說明) |
|-----------|-------------------------|-------------------|
| `get_futures_quotes_daily` | [https://openapi.taifex.com.tw/v1/DailyMarketReportFut](https://openapi.taifex.com.tw/v1/DailyMarketReportFut) | 期貨每日收盤行情 |
| `get_futures_institutional_investor_flow` | [https://openapi.taifex.com.tw/v1/MarketDataOfMajorInstitutionalTradersGeneralBytheDate](https://openapi.taifex.com.tw/v1/MarketDataOfMajorInstitutionalTradersGeneralBytheDate) | 三大法人期貨交易量與未平倉彙總 |
| `get_futures_open_interest_ranking` | [https://openapi.taifex.com.tw/v1/OpenInterestOfLargeTradersFutures](https://openapi.taifex.com.tw/v1/OpenInterestOfLargeTradersFutures) | 期貨大額交易人未平倉部位統計 |

## 🏦 Bank Industry
*Exhaustive list of all tools in BANK_LIST.*

| Tool Name | Direct API URL (Source) | Description (說明) |
|-----------|-------------------------|-------------------|
| `get_bank_balance_sheets` | [https://www.cbc.gov.tw/](https://www.cbc.gov.tw/) | 全體本國銀行資產負債表彙總 |
| `get_bank_major_assets_liabilities_stats` | [https://www.cbc.gov.tw/](https://www.cbc.gov.tw/) | 銀行主要資產負債項目統計 |
| `get_bank_sme_loan_balance_stats` | FSC Open Data | 本國銀行對中小企業(SME)放款餘額 |
| `get_bank_monthly_profit_summary` | FSC Open Data | 銀行業每月稅前損益彙總 |
| `get_bank_overdue_loan_stats` | FSC Open Data | 銀行資產品質：逾期放款 (NPL) 比率 |
| `get_bank_foreign_exchange_trading_volume` | [https://www.cbc.gov.tw/](https://www.cbc.gov.tw/) | 台北外匯指定銀行 (DBU) 交易量 |
| `get_bank_deposit_rate_fixed` | Commercial Banks | 本國銀行定期存款固定利率 |
| `get_bank_mortgage_rate_average` | Commercial Banks | 個別商業銀行房貸利率查詢 |
| `get_bank_credit_card_delinquency` | FSC Open Data | 信用卡逾期帳款比率統計 |
| `get_bank_atm_location_map` | Gov Data Platform | 全台 ATM 點位資料 |
| `get_bank_capital_adequacy_ratio` | FSC Open Data | 本國銀行資本適足率 (BIS) 統計 |

## 🏛️ Macroeconomics & Gov News
*Exhaustive list of all remaining tools in MACRO_LIST, TAX_LIST, CORP_LIST, NEWS_LIST.*

| Tool Name | Direct API URL (Source) | Description (說明) |
|-----------|-------------------------|-------------------|
| `get_macro_gdp_growth_rate_quarterly` | [https://apiservice.mol.gov.tw/OdService/download/A17000000J-030243-YTl](https://apiservice.mol.gov.tw/OdService/download/A17000000J-030243-YTl) | 台灣季度 GDP 經濟成長率 |
| `get_macro_national_debt_clock` | [https://www.mof.gov.tw/](https://www.mof.gov.tw/) | 中華民國國債鐘數據 |
| `get_macro_central_bank_policy_rate` | [https://www.cbc.gov.tw/](https://www.cbc.gov.tw/) | 中央銀行重貼現率 (官方基準利率) |
| `get_macro_money_supply_m1b_m2` | [https://www.cbc.gov.tw/](https://www.cbc.gov.tw/) | 台灣貨幣總計數 M1B/M2 年增率 |
| `get_macro_foreign_exchange_reserves` | [https://www.cbc.gov.tw/](https://www.cbc.gov.tw/) | 台灣外匯存底統計 |
| `get_macro_bank_mortgage_loan_rates" | [https://www.cbc.gov.tw/](https://www.cbc.gov.tw/) | 五大銀行新承做購屋貸款平均利率 |
| `get_tax_income_bracket_calculator` | [https://www.mof.gov.tw/](https://www.mof.gov.tw/) | 綜合所得稅級距與試算公式 |
| `get_tax_revenue_collection_monthly` | [https://www.mof.gov.tw/](https://www.mof.gov.tw/) | 全國賦稅實徵淨額統計 |
| `get_tax_electronic_invoice_usage_stats` | [https://www.mof.gov.tw/](https://www.mof.gov.tw/) | 電子發票普及率與張數統計 |
| `get_corp_moea_business_registration` | [https://data.gcis.nat.gov.tw/](https://data.gcis.nat.gov.tw/) | 經濟部商工登記公示資料 |
| `get_corp_industry_electricity_consumption_stats` | [https://www.moeaea.gov.tw/](https://www.moeaea.gov.tw/) | 各產業部門電力消費統計 |
| `get_gov_central_bank_announcements` | [https://www.cbc.gov.tw/](https://www.cbc.gov.tw/) | 中央銀行重要政策公告 |
| `get_gov_industrial_policy_news_moea` | [https://www.moea.gov.tw/](https://www.moea.gov.tw/) | 經濟部經貿與產業政策新聞 |

## 🪙 Cryptocurrency & System
*Exhaustive list of all tools in CRYPTO_LIST, COMMON_LIST.*

| Tool Name | Direct API URL (Source) | Description (說明) |
|-----------|-------------------------|-------------------|
| `get_crypto_btc_twd_price` | [CoinGecko API](https://api.coingecko.com/api/v3/) | 比特幣即時 TWD/USD 報價 |
| `get_crypto_eth_twd_price` | [CoinGecko API](https://api.coingecko.com/api/v3/) | 以太幣即時 TWD/USD 報價 |
| `get_crypto_sol_twd_price` | [CoinGecko API](https://api.coingecko.com/api/v3/) | Solana 即時報價與市場表現 |
| `get_crypto_market_fear_greed_index` | [CoinGecko API](https://api.coingecko.com/api/v3/) | 全球加密幣市場恐慌與貪婪指數 |
| `get_current_time_taipei` | System | 獲取台北即時系統時間 |

---
*Total Tools Documented: 60*
*Last Updated: 2026-02-09*
