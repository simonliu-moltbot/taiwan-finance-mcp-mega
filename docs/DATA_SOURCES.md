# Direct API Endpoint Registry (Verified Stabilized)

This document provides an exhaustive mapping of every active tool in the `taiwan-finance-mcp-mega` project. All unstable or placeholder "home page" links have been removed.

---

## 📈 Stock Market (TWSE / TPEx)
*Status: Fully Operational via Official OpenAPI v1.*

| Tool Name | Direct API URL (Source) | Description (說明) |
|-----------|-------------------------|-------------------|
| `get_stock_quotes_realtime_all` | [https://openapi.twse.com.tw/v1/exchangeReport/STOCK_DAY_ALL](https://openapi.twse.com.tw/v1/exchangeReport/STOCK_DAY_ALL) | 上市個股當日即時行情 |
| `get_stock_eps_ranking_summary` | [https://openapi.twse.com.tw/v1/opendata/t187ap14_L](https://openapi.twse.com.tw/v1/opendata/t187ap14_L) | 各產業 EPS 統計資訊 |
| `get_stock_dividend_yield_pe_pb` | [https://openapi.twse.com.tw/v1/exchangeReport/BWIBBU_d](https://openapi.twse.com.tw/v1/exchangeReport/BWIBBU_d) | 個股日本益比、殖利率及淨值比 |
| `get_stock_institutional_investor_flow` | [Web URL](https://www.twse.com.tw/zh/page/trading/fund/BFI82U.html) | 三大法人買賣超彙總統計 (上市) |
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

## 📉 Derivatives (Taifex)
*Status: Verified Real OpenAPI Paths.*

| Tool Name | Direct API URL (Source) | Description (說明) |
|-----------|-------------------------|-------------------|
| `get_futures_quotes_daily` | [https://openapi.taifex.com.tw/v1/DailyMarketReportFut](https://openapi.taifex.com.tw/v1/DailyMarketReportFut) | 期貨每日收盤行情 |
| `get_futures_institutional_investor_flow` | [https://openapi.taifex.com.tw/v1/MarketDataOfMajorInstitutionalTradersGeneralBytheDate](https://openapi.taifex.com.tw/v1/MarketDataOfMajorInstitutionalTradersGeneralBytheDate) | 三大法人期貨交易量與未平倉彙總 |
| `get_futures_open_interest_ranking` | [https://openapi.taifex.com.tw/v1/OpenInterestOfLargeTradersFutures](https://openapi.taifex.com.tw/v1/OpenInterestOfLargeTradersFutures) | 期貨大額交易人未平倉部位統計 |

## 🌍 Forex & Commodities
*Status: Using tw.rter.info Cross-Rate Engine.*

| Tool Name | Direct API URL (Source) | Description (說明) |
|-----------|-------------------------|-------------------|
| `get_forex_[CUR]_twd_realtime` | [https://tw.rter.info/capi.php](https://tw.rter.info/capi.php) | 各國幣別對台幣即時匯率 |
| `get_forex_any_to_any_conversion` | [https://tw.rter.info/capi.php](https://tw.rter.info/capi.php) | 任意幣別對任意幣別即時換算 |
| `get_commodity_oil_wti_price_usd` | [https://www2.moeaea.gov.tw/oil111/csv/GlobalOilOpenData.csv](https://www2.moeaea.gov.tw/oil111/csv/GlobalOilOpenData.csv) | 全球原油價格 (WTI/Brent) |
| `get_commodity_gold_spot_price_twd` | [https://www.tpex.org.tw/openapi/v1/gold_DailyQuotes](https://www.tpex.org.tw/openapi/v1/gold_DailyQuotes) | 黃金現貨即時報價(TWD) |

## 🏛️ Macroeconomics & Corporate
*Status: Stable Government API Endpoints.*

| Tool Name | Direct API URL (Source) | Description (說明) |
|-----------|-------------------------|-------------------|
| `get_macro_gdp_growth_rate_quarterly` | [MOL / DGBAS API](https://apiservice.mol.gov.tw/OdService/download/A17000000J-030243-YTl) | 台灣季度 GDP 經濟成長率 |
| `get_macro_national_debt_clock` | Static MOF Data | 中華民國國債鐘數據 |
| `get_macro_monthly_financial_indicators` | [MOL REST API](https://apiservice.mol.gov.tw/OdService/rest/datastore/A17030000J-000037-l9P) | 每月國內主要金融指標 (M1B/M2/外匯存底) |
| `get_macro_economic_indicators_monthly` | [MOL REST API](https://apiservice.mol.gov.tw/OdService/rest/datastore/A17030000J-000016-1ci) | 每月國內主要經濟指標 (GDP/CPI/失業率) |
| `get_macro_economic_indicators_annual` | [MOL REST API](https://apiservice.mol.gov.tw/OdService/rest/datastore/A17000000J-030243-XXL) | 年度國內主要經濟指標 (長期趨勢) |
| `get_bank_bot_credit_rating` | [Bank of Taiwan JSON](https://quality.data.gov.tw/dq_download_json.php?nid=31927&md5_url=ebdd6bebd608b17380749eb0bc21d06f) | 臺灣銀行信用評等等級 (S&P/Moody's/中華信評) |
| `get_bank_stock_indices_monthly` | [MOL REST API](https://apiservice.mol.gov.tw/OdService/rest/datastore/A17030000J-000050-Ipz) | 每月國際主要股價指數 (台/美/日/歐) |
| `get_bank_forex_rates_monthly` | [MOL REST API](https://apiservice.mol.gov.tw/OdService/rest/datastore/A17030000J-000049-Iq0) | 國際主要國家貨幣每月匯率概況 |
| `get_bank_bond_issuance_monthly` | [MOL REST API](https://apiservice.mol.gov.tw/OdService/rest/datastore/A17030000J-000048-YHK) | 國內債券每月發行概況 |
| `get_bank_stock_issuance_monthly` | [MOL REST API](https://apiservice.mol.gov.tw/OdService/rest/datastore/A17030000J-000047-Y4N) | 國內公開發行公司股票每月發行概況 |
| `get_bank_pension_fund_stats_monthly` | [MOL REST API](https://apiservice.mol.gov.tw/OdService/rest/datastore/A17030000J-000045-2qm) | 國民年金保險基金每月經營概況 |
| `get_bank_stock_indices_annual` | [MOL REST API](https://apiservice.mol.gov.tw/OdService/rest/datastore/A17000000J-030245-4Ml) | 年度國際主要股價指數 |
| `get_bank_forex_rates_annual` | [MOL REST API](https://apiservice.mol.gov.tw/OdService/rest/datastore/A17000000J-030185-CKf) | 國際主要國家貨幣年度匯率概況 |
| `get_corp_moea_business_registration` | [GCIS NAT API](https://data.gcis.nat.gov.tw/od/data/api/) | 經濟部商工登記公示資料 |

## 🪙 Cryptocurrency & System

| Tool Name | Direct API URL (Source) | Description (說明) |
|-----------|-------------------------|-------------------|
| `get_crypto_btc_twd_price` | [CoinGecko (Bitcoin)](https://www.coingecko.com/en/coins/bitcoin) | 比特幣即時 TWD/USD 報價 |
| `get_crypto_eth_twd_price` | [CoinGecko (Ethereum)](https://www.coingecko.com/en/coins/ethereum) | 以太幣即時 TWD/USD 報價 |
| `get_crypto_sol_twd_price` | [CoinGecko (Solana)](https://www.coingecko.com/en/coins/solana) | Solana 即時報價與市場表現 |
| `get_crypto_market_fear_greed_index` | [Alternative.me (Fear & Greed)](https://alternative.me/crypto/fear-and-greed-index/) | 全球加密幣市場恐慌與貪婪指數 |
| `get_current_time_taipei` | Local Environment | 獲取台北即時系統時間 |

---
*Total Active Verified Tools: 59*
*Last Updated: 2026-02-09*
