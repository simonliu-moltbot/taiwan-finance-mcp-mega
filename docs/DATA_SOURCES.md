# Direct API Endpoint Registry

This document provides a comprehensive list of direct API URLs for every tool in the `taiwan-finance-mcp-mega` project. This allows for immediate verification of raw data from the source.

---

## 📈 Stock Market (TWSE / TPEx)
*Data format: JSON. Focuses on spot market quotes and corporate financial data.*

| Tool Name | Direct API URL (Source) | Description (說明) |
|-----------|-------------------------|-------------------|
| `get_stock_block_trade_daily_summary` | [https://openapi.twse.com.tw/v1/block/BFIAUU_d](https://openapi.twse.com.tw/v1/block/BFIAUU_d) | 鉅額交易日成交量值統計 |
| `get_stock_broker_list_all` | [https://openapi.twse.com.tw/v1/brokerService/brokerList](https://openapi.twse.com.tw/v1/brokerService/brokerList) | 證券商基本資料一覽表 |
| `get_stock_etf_regular_savings_ranking` | [https://openapi.twse.com.tw/v1/ETFReport/ETFRank](https://openapi.twse.com.tw/v1/ETFReport/ETFRank) | ETF 定期定額交易戶數排行 |
| `get_stock_after_hours_trading_info` | [https://openapi.twse.com.tw/v1/exchangeReport/BFT41U](https://openapi.twse.com.tw/v1/exchangeReport/BFT41U) | 盤後定價交易資訊 |
| `get_stock_institutional_investor_flow` | [https://www.twse.com.tw/zh/page/trading/fund/BFI82U.html](https://www.twse.com.tw/zh/page/trading/fund/BFI82U.html) | 三大法人買賣超彙總統計 (上市) |
| `get_stock_dividend_yield_pe_pb` | [https://openapi.twse.com.tw/v1/exchangeReport/BWIBBU_d](https://openapi.twse.com.tw/v1/exchangeReport/BWIBBU_d) | 個股日本益比、殖利率及淨值比 |
| `get_stock_pe_averages_by_industry` | [https://openapi.twse.com.tw/v1/exchangeReport/FMNPTK_ALL](https://openapi.twse.com.tw/v1/exchangeReport/FMNPTK_ALL) | 上市公司各類股本益比統計 |
| `get_stock_yield_averages_by_industry` | [https://openapi.twse.com.tw/v1/exchangeReport/FMSRFK_ALL](https://openapi.twse.com.tw/v1/exchangeReport/FMSRFK_ALL) | 上市公司各類股殖利率統計 |
| `get_stock_daily_closing_quotes_all` | [https://openapi.twse.com.tw/v1/exchangeReport/MI_INDEX](https://openapi.twse.com.tw/v1/exchangeReport/MI_INDEX) | 收盤指數及各類股成交量值 |
| `get_stock_margin_trading_balance` | [https://openapi.twse.com.tw/v1/exchangeReport/MI_MARGN](https://openapi.twse.com.tw/v1/exchangeReport/MI_MARGN) | 融資融券餘額明細 |
| `get_stock_listed_stock_price_averages` | [https://openapi.twse.com.tw/v1/exchangeReport/STOCK_DAY_AVG_ALL](https://openapi.twse.com.tw/v1/exchangeReport/STOCK_DAY_AVG_ALL) | 上市公司收盤價及月平均價 |
| `get_stock_quotes_realtime_all` | [https://openapi.twse.com.tw/v1/exchangeReport/STOCK_DAY_ALL](https://openapi.twse.com.tw/v1/exchangeReport/STOCK_DAY_ALL) | 上市個股當日即時行情 |
| `get_stock_odd_lot_trading_quotes` | [https://openapi.twse.com.tw/v1/exchangeReport/TWT53U](https://openapi.twse.com.tw/v1/exchangeReport/TWT53U) | 盤中零股交易即時行情 |
| `get_stock_price_limit_up_down_tracker` | [https://openapi.twse.com.tw/v1/exchangeReport/TWT84U](https://openapi.twse.com.tw/v1/exchangeReport/TWT84U) | 股價升降幅度/漲跌停預告 |
| `get_stock_listed_company_basic_info` | [https://openapi.twse.com.tw/v1/opendata/t187ap03_L](https://openapi.twse.com.tw/v1/opendata/t187ap03_L) | 上市公司基本資料 |
| `get_stock_mops_significant_announcements` | [https://openapi.twse.com.tw/v1/opendata/t187ap04_L](https://openapi.twse.com.tw/v1/opendata/t187ap04_L) | 每日重大訊息公告 (MOPS) |
| `get_stock_monthly_revenue_summary` | [https://openapi.twse.com.tw/v1/opendata/t187ap05_L](https://openapi.twse.com.tw/v1/opendata/t187ap05_L) | 每月營業收入彙總表 |
| `get_stock_balance_sheet_general` | [https://openapi.twse.com.tw/v1/opendata/t187ap07_X_ci](https://openapi.twse.com.tw/v1/opendata/t187ap07_X_ci) | 資產負債表-一般業 |
| `get_stock_buyback_treasury_status` | [https://openapi.twse.com.tw/v1/opendata/t187ap13_L](https://openapi.twse.com.tw/v1/opendata/t187ap13_L) | 庫藏股買回進度彙整 |
| `get_stock_eps_ranking_summary` | [https://openapi.twse.com.tw/v1/opendata/t187ap14_L](https://openapi.twse.com.tw/v1/opendata/t187ap14_L) | 各產業 EPS 統計資訊 |
| `get_stock_listed_company_profile_tpex` | [https://www.tpex.org.tw/openapi/v1/t187ap03_O](https://www.tpex.org.tw/openapi/v1/t187ap03_O) | 上櫃公司基本資料 |
| `get_stock_institutional_trading_tpex` | [https://www.tpex.org.tw/openapi/v1/tpex_3insti_daily_trading](https://www.tpex.org.tw/openapi/v1/tpex_3insti_daily_trading) | 三大法人買賣超明細 (上櫃個股) |
| `get_stock_institutional_summary_tpex` | [https://www.tpex.org.tw/openapi/v1/tpex_3insti_summary](https://www.tpex.org.tw/openapi/v1/tpex_3insti_summary) | 三大法人買賣超彙總統計 (上櫃) |

## 📉 Derivatives (Taifex)
*Futures and options contracts data from the Taiwan Futures Exchange.*

| Tool Name | Direct API URL (Source) | Description (說明) |
|-----------|-------------------------|-------------------|
| `get_futures_quotes_daily` | [https://openapi.taifex.com.tw/v1/DailyMarketReportFut](https://openapi.taifex.com.tw/v1/DailyMarketReportFut) | 期貨每日收盤行情 |
| `get_futures_institutional_investor_flow` | [https://openapi.taifex.com.tw/v1/MarketDataOfMajorInstitutionalTradersGeneralBytheDate](https://openapi.taifex.com.tw/v1/MarketDataOfMajorInstitutionalTradersGeneralBytheDate) | 三大法人期貨交易量與未平倉彙總 |
| `get_futures_open_interest_ranking` | [https://openapi.taifex.com.tw/v1/OpenInterestOfLargeTradersFutures](https://openapi.taifex.com.tw/v1/OpenInterestOfLargeTradersFutures) | 期貨大額交易人未平倉部位統計 |

## 🌍 Forex & Commodities

| Tool Name | Direct API URL (Source) | Description (說明) |
|-----------|-------------------------|-------------------|
| `get_forex_[CUR]_twd_realtime` | [https://tw.rter.info/capi.php](https://tw.rter.info/capi.php) | 全球即時匯率換算 (源自即匯站) |
| `get_commodity_oil_wti_price_usd` | [https://www2.moeaea.gov.tw/oil111/csv/GlobalOilOpenData.csv](https://www2.moeaea.gov.tw/oil111/csv/GlobalOilOpenData.csv) | 全球原油價格 (WTI/Brent) |

## 🏛️ Macroeconomics & Gov Data

| Tool Name | Direct API URL (Source) | Description (說明) |
|-----------|-------------------------|-------------------|
| `get_macro_gdp_growth_rate_quarterly` | [https://apiservice.mol.gov.tw/OdService/download/A17000000J-030243-YTl](https://apiservice.mol.gov.tw/OdService/download/A17000000J-030243-YTl) | 經濟成長率、CPI、失業率統計 |
| `get_macro_fuel_price_cpc_retail` | [https://vipmbr.cpc.com.tw/openData/MainProdListPrice](https://vipmbr.cpc.com.tw/openData/MainProdListPrice) | 中油即時牌價 |
| `get_macro_housing_price_index_tw` | [https://quality.data.gov.tw/dq_download_json.php?nid=11545&md5_url=59196b0c242337d40236a281691a5f36](https://quality.data.gov.tw/dq_download_json.php?nid=11545&md5_url=59196b0c242337d40236a281691a5f36) | 全國住宅價格指數 |
| `get_bank_list_of_institutions` | [https://quality.data.gov.tw/dq_download_json.php?nid=18419&md5_url=2851676f4e157208d3663a890473919d](https://quality.data.gov.tw/dq_download_json.php?nid=18419&md5_url=2851676f4e157208d3663a890473919d) | 金融機構基本資料 |
| `get_bank_profit_loss_statements` | [https://quality.data.gov.tw/dq_download_json.php?nid=28567&md5_url=2851676f4e157208d3663a890473919d](https://quality.data.gov.tw/dq_download_json.php?nid=28567&md5_url=2851676f4e157208d3663a890473919d) | 銀行業損益統計 |
| `get_corp_industry_electricity_consumption_stats` | [https://www.moeaea.gov.tw/ECW/populace/opendata/wHandOpenData_File.ashx?set_id=236](https://www.moeaea.gov.tw/ECW/populace/opendata/wHandOpenData_File.ashx?set_id=236) | 產業電力消費統計 |
| `get_gov_financial_news_fsc` | [https://quality.data.gov.tw/dq_download_json.php?nid=7334&md5_url=59196b0c242337d40236a281691a5f36](https://quality.data.gov.tw/dq_download_json.php?nid=7334&md5_url=59196b0c242337d40236a281691a5f36) | 金管會新聞稿公告 |

## 🪙 Cryptocurrency

| Tool Name | Direct API URL (Source) | Description (說明) |
|-----------|-------------------------|-------------------|
| `get_crypto_btc_twd_price` | [https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=twd,usd&include_24hr_change=true](https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=twd,usd&include_24hr_change=true) | 比特幣即時報價 |
| `get_crypto_eth_twd_price` | [https://api.coingecko.com/api/v3/simple/price?ids=ethereum&vs_currencies=twd,usd&include_24hr_change=true](https://api.coingecko.com/api/v3/simple/price?ids=ethereum&vs_currencies=twd,usd&include_24hr_change=true) | 以太幣即時報價 |

---
*Last Updated: 2026-02-09*
