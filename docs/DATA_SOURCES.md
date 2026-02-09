# Direct API Endpoint Registry

This document provides a comprehensive list of direct API URLs for every tool in the `taiwan-finance-mcp-mega` project. This allows for immediate verification of raw data from the source.

---

## 📈 Stock Market (TWSE / TPEx)
*Data format: JSON*

| Tool Name | Direct API URL (Source) |
|-----------|-------------------------|
| `get_stock_quotes_realtime_all` | [https://openapi.twse.com.tw/v1/exchangeReport/STOCK_DAY_ALL](https://openapi.twse.com.tw/v1/exchangeReport/STOCK_DAY_ALL) |
| `get_stock_eps_ranking_summary` | [https://openapi.twse.com.tw/v1/opendata/t187ap14_L](https://openapi.twse.com.tw/v1/opendata/t187ap14_L) |
| `get_stock_dividend_yield_pe_pb` | [https://openapi.twse.com.tw/v1/exchangeReport/BWIBBU_d](https://openapi.twse.com.tw/v1/exchangeReport/BWIBBU_d) |
| `get_stock_institutional_investor_flow` | [https://openapi.twse.com.tw/v1/fund/BFI82U](https://openapi.twse.com.tw/v1/fund/BFI82U) |
| `get_stock_margin_trading_balance` | [https://openapi.twse.com.tw/v1/exchangeReport/MI_MARGN](https://openapi.twse.com.tw/v1/exchangeReport/MI_MARGN) |
| `get_stock_odd_lot_trading_quotes` | [https://openapi.twse.com.tw/v1/exchangeReport/TWT53U](https://openapi.twse.com.tw/v1/exchangeReport/TWT53U) |
| `get_stock_mops_significant_announcements` | [https://openapi.twse.com.tw/v1/opendata/t187ap04_L](https://openapi.twse.com.tw/v1/opendata/t187ap04_L) |
| `get_stock_price_limit_up_down_tracker` | [https://openapi.twse.com.tw/v1/exchangeReport/TWT84U](https://openapi.twse.com.tw/v1/exchangeReport/TWT84U) |
| `get_stock_balance_sheet_general` | [https://openapi.twse.com.tw/v1/opendata/t187ap07_X_ci](https://openapi.twse.com.tw/v1/opendata/t187ap07_X_ci) |
| `get_stock_monthly_revenue_summary` | [https://openapi.twse.com.tw/v1/opendata/t187ap05_L](https://openapi.twse.com.tw/v1/opendata/t187ap05_L) |
| `get_stock_listed_company_basic_info` | [https://openapi.twse.com.tw/v1/opendata/t187ap03_L](https://openapi.twse.com.tw/v1/opendata/t187ap03_L) |
| `get_stock_etf_regular_savings_ranking` | [https://openapi.twse.com.tw/v1/ETFReport/ETFRank](https://openapi.twse.com.tw/v1/ETFReport/ETFRank) |
| `get_stock_block_trade_daily_summary` | [https://openapi.twse.com.tw/v1/block/BFIAUU_d](https://openapi.twse.com.tw/v1/block/BFIAUU_d) |
| `get_stock_after_hours_trading_info` | [https://openapi.twse.com.tw/v1/exchangeReport/BFT41U](https://openapi.twse.com.tw/v1/exchangeReport/BFT41U) |
| `get_stock_ipo_new_listing_schedule` | [https://openapi.twse.com.tw/v1/exchangeReport/TWT82U](https://openapi.twse.com.tw/v1/exchangeReport/TWT82U) |
| `get_stock_buyback_treasury_status` | [https://openapi.twse.com.tw/v1/opendata/t187ap13_L](https://openapi.twse.com.tw/v1/opendata/t187ap13_L) |
| `get_stock_listed_company_profile_tpex` | [https://www.tpex.org.tw/openapi/v1/t187ap03_O](https://www.tpex.org.tw/openapi/v1/t187ap03_O) |

## 📉 Derivatives (Taifex)

| Tool Name | Direct API URL (Source) |
|-----------|-------------------------|
| `get_futures_quotes_daily` | [https://openapi.taifex.com.tw/v1/DailyQuotes](https://openapi.taifex.com.tw/v1/DailyQuotes) |
| `get_futures_institutional_investor_flow` | [https://openapi.taifex.com.tw/v1/InstitutionalInvestorsDaily](https://openapi.taifex.com.tw/v1/InstitutionalInvestorsDaily) |
| `get_futures_open_interest_ranking` | [https://openapi.taifex.com.tw/v1/LargeTradersPositionsDaily](https://openapi.taifex.com.tw/v1/LargeTradersPositionsDaily) |

## 🌍 Forex & Commodities

| Tool Name | Direct API URL (Source) |
|-----------|-------------------------|
| `get_forex_usd_twd_realtime` | [https://open.er-api.com/v6/latest/USD](https://open.er-api.com/v6/latest/USD) |
| `get_forex_jpy_twd_realtime` | [https://open.er-api.com/v6/latest/JPY](https://open.er-api.com/v6/latest/JPY) |
| `get_commodity_oil_wti_price_usd` | [https://www2.moeaea.gov.tw/oil111/csv/GlobalOilOpenData.csv](https://www2.moeaea.gov.tw/oil111/csv/GlobalOilOpenData.csv) |

## 🏛️ Macroeconomics & Gov Data

| Tool Name | Direct API URL (Source) |
|-----------|-------------------------|
| `get_macro_gdp_growth_rate_quarterly` | [https://apiservice.mol.gov.tw/OdService/download/A17000000J-030243-YTl](https://apiservice.mol.gov.tw/OdService/download/A17000000J-030243-YTl) |
| `get_macro_fuel_price_cpc_retail` | [https://vipmbr.cpc.com.tw/openData/MainProdListPrice](https://vipmbr.cpc.com.tw/openData/MainProdListPrice) |
| `get_macro_housing_price_index_tw` | [https://quality.data.gov.tw/dq_download_json.php?nid=11545&md5_url=59196b0c242337d40236a281691a5f36](https://quality.data.gov.tw/dq_download_json.php?nid=11545&md5_url=59196b0c242337d40236a281691a5f36) |
| `get_bank_list_of_institutions` | [https://quality.data.gov.tw/dq_download_json.php?nid=18419&md5_url=2851676f4e157208d3663a890473919d](https://quality.data.gov.tw/dq_download_json.php?nid=18419&md5_url=2851676f4e157208d3663a890473919d) |
| `get_bank_profit_loss_statements` | [https://quality.data.gov.tw/dq_download_json.php?nid=28567&md5_url=2851676f4e157208d3663a890473919d](https://quality.data.gov.tw/dq_download_json.php?nid=28567&md5_url=2851676f4e157208d3663a890473919d) |
| `get_corp_industry_electricity_consumption_stats` | [https://www.moeaea.gov.tw/ECW/populace/opendata/wHandOpenData_File.ashx?set_id=236](https://www.moeaea.gov.tw/ECW/populace/opendata/wHandOpenData_File.ashx?set_id=236) |
| `get_gov_financial_news_fsc` | [https://quality.data.gov.tw/dq_download_json.php?nid=7334&md5_url=59196b0c242337d40236a281691a5f36](https://quality.data.gov.tw/dq_download_json.php?nid=7334&md5_url=59196b0c242337d40236a281691a5f36) |

## 🪙 Cryptocurrency (CoinGecko Simple API)

| Tool Name | Direct API URL (Source) |
|-----------|-------------------------|
| `get_crypto_btc_twd_price` | [https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=twd,usd&include_24hr_change=true](https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=twd,usd&include_24hr_change=true) |
| `get_crypto_eth_twd_price` | [https://api.coingecko.com/api/v3/simple/price?ids=ethereum&vs_currencies=twd,usd&include_24hr_change=true](https://api.coingecko.com/api/v3/simple/price?ids=ethereum&vs_currencies=twd,usd&include_24hr_change=true) |

---
*Last Updated: 2026-02-09*
