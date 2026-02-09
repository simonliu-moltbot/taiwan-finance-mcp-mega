# Direct API Endpoint Registry (Verified & Stabilized)

This document provides an exhaustive mapping of every active tool in the `taiwan-finance-mcp-mega` project. All unstable or placeholder "home page" links have been removed.

---

## 📈 Stock Market (TWSE / TPEx)
*Status: Fully Operational via Official OpenAPI v1 and RWD JSON interfaces.*

| Tool Name | Direct API URL (Source) | Description |
|-----------|-------------------------|-------------------|
| `get_stock_quotes_realtime_all` | [TWSE OpenAPI](https://openapi.twse.com.tw/v1/exchangeReport/STOCK_DAY_ALL) | Real-time stock quotes for listed companies |
| `get_stock_eps_ranking_summary` | [TWSE OpenAPI](https://openapi.twse.com.tw/v1/opendata/t187ap14_L) | EPS statistics and ranking by industry |
| `get_stock_dividend_yield_pe_pb` | [TWSE OpenAPI](https://openapi.twse.com.tw/v1/exchangeReport/BWIBBU_d) | PE ratio, dividend yield, and PB ratio |
| `get_stock_institutional_summary_twse` | [TWSE RWD API](https://www.twse.com.tw/rwd/zh/fund/BFI82U?response=json) | [Listed/Main] Institutional investor net flow summary |
| `get_stock_institutional_details_tpex` | [TPEx OpenAPI](https://www.tpex.org.tw/openapi/v1/tpex_3insti_daily_trading) | [OTC] Institutional investor net flow details per stock |
| `get_stock_institutional_summary_tpex` | [TPEx OpenAPI](https://www.tpex.org.tw/openapi/v1/tpex_3insti_summary) | [OTC] Institutional investor net flow summary |
| `get_stock_margin_trading_balance` | [TWSE OpenAPI](https://openapi.twse.com.tw/v1/exchangeReport/MI_MARGN) | Margin trading and short selling balance details |
| `get_stock_odd_lot_trading_quotes` | [TWSE OpenAPI](https://openapi.twse.com.tw/v1/exchangeReport/TWT53U) | Real-time odd-lot trading quotes |
| `get_stock_mops_significant_announcements` | [TWSE OpenAPI](https://openapi.twse.com.tw/v1/opendata/t187ap04_L) | Daily significant announcements (MOPS) |
| `get_stock_price_limit_up_down_tracker` | [TWSE OpenAPI](https://openapi.twse.com.tw/v1/exchangeReport/TWT84U) | Price limit up/down alerts |
| `get_stock_monthly_revenue_summary` | [TWSE OpenAPI](https://openapi.twse.com.tw/v1/opendata/t187ap05_L) | Monthly revenue summary and growth rates |
| `get_stock_etf_regular_savings_ranking` | [TWSE OpenAPI](https://openapi.twse.com.tw/v1/ETFReport/ETFRank) | ETF regular savings account count ranking |
| `get_stock_block_trade_daily_summary` | [TWSE OpenAPI](https://openapi.twse.com.tw/v1/block/BFIAUU_d) | Block trade daily volume and value statistics |
| `get_stock_after_hours_trading_info` | [TWSE OpenAPI](https://openapi.twse.com.tw/v1/exchangeReport/BFT41U) | After-hours fixed-price trading info |
| `get_stock_individual_average_price` | [TWSE OpenAPI](https://openapi.twse.com.tw/v1/exchangeReport/STOCK_DAY_AVG_ALL) | Individual stock monthly closing average price |
| `get_stock_listed_investor_profile` | [TWSE OpenAPI](https://openapi.twse.com.tw/v1/opendata/t187ap03_L) | Listed company investor profile (Spokesperson/URL/Listing Date) |
| `get_stock_otc_investor_profile` | [TPEx OpenAPI](https://www.tpex.org.tw/openapi/v1/t187ap03_O) | OTC company investor profile (Spokesperson/URL/Listing Date) |
| `get_stock_public_investor_profile` | [TWSE OpenAPI](https://openapi.twse.com.tw/v1/opendata/t187ap03_P) | Publicly issued company basic investment data |
| `get_stock_daily_closing_quotes_all` | [TWSE OpenAPI](https://openapi.twse.com.tw/v1/exchangeReport/MI_INDEX) | Closing index and trading volume by category |
| `get_stock_yield_averages_by_industry` | [TWSE OpenAPI](https://openapi.twse.com.tw/v1/exchangeReport/FMSRFK_ALL) | Listed company dividend yield stats by industry |
| `get_stock_pe_averages_by_industry` | [TWSE OpenAPI](https://openapi.twse.com.tw/v1/exchangeReport/FMNPTK_ALL) | Listed company PE ratio stats by industry |
| `get_stock_broker_list_all` | [TWSE OpenAPI](https://openapi.twse.com.tw/v1/brokerService/brokerList) | Comprehensive list of stock brokers in Taiwan |
| `get_stock_buyback_treasury_status` | [TWSE OpenAPI](https://openapi.twse.com.tw/v1/opendata/t187ap13_L) | Treasury stock buyback progress summary |
| `get_stock_broker_regular_savings_data` | [TWSE OpenAPI](https://openapi.twse.com.tw/v1/brokerService/secRegData) | List of brokers providing regular savings plans |

## 📉 Derivatives (Taifex)
*Status: Verified Real OpenAPI Paths.*

| Tool Name | Direct API URL (Source) | Description |
|-----------|-------------------------|-------------------|
| `get_futures_quotes_daily` | [Taifex OpenAPI](https://openapi.taifex.com.tw/v1/DailyMarketReportFut) | Daily futures market closing report |
| `get_futures_institutional_investor_flow` | [Taifex OpenAPI](https://openapi.taifex.com.tw/v1/MarketDataOfMajorInstitutionalTradersGeneralBytheDate) | Institutional net flow and open interest summary |
| `get_futures_open_interest_ranking` | [Taifex OpenAPI](https://openapi.taifex.com.tw/v1/OpenInterestOfLargeTradersFutures) | Open interest ranking of large futures traders |

## 🌍 Forex & Commodities
*Status: Using tw.rter.info cross-rate engine and public gov data.*

| Tool Name | Direct API URL (Source) | Description |
|-----------|-------------------------|-------------------|
| `get_forex_[CUR]_twd_realtime` | [tw.rter.info API](https://tw.rter.info/capi.php) | Real-time exchange rate vs TWD |
| `get_forex_any_to_any_conversion` | [tw.rter.info API](https://tw.rter.info/capi.php) | Real-time currency conversion (Any to Any) |
| `get_commodity_oil_wti_price_usd` | [MOEA CSV](https://www2.moeaea.gov.tw/oil111/csv/GlobalOilOpenData.csv) | Global crude oil prices (WTI/Brent) |
| `get_commodity_gold_spot_price_twd` | [TPEx OpenAPI](https://www.tpex.org.tw/openapi/v1/tpex_gold_latest) | Real-time gold spot price (TWD) |

## 🏛️ Macroeconomics & Corporate
*Status: Stable Government API Endpoints.*

| Tool Name | Direct API URL (Source) | Description |
|-----------|-------------------------|-------------------|
| `get_macro_gdp_growth_rate_quarterly` | [MOL REST API](https://apiservice.mol.gov.tw/OdService/rest/datastore/A17030000J-000016-1ci) | Taiwan Quarterly GDP growth rate |
| `get_macro_monthly_financial_indicators` | [MOL REST API](https://apiservice.mol.gov.tw/OdService/rest/datastore/A17030000J-000037-l9P) | Monthly financial indicators (M1B/M2/Reserves) |
| `get_macro_economic_indicators_monthly` | [MOL REST API](https://apiservice.mol.gov.tw/OdService/rest/datastore/A17030000J-000016-1ci) | Monthly economic indicators (GDP/CPI/Unemployment) |
| `get_macro_economic_indicators_annual` | [MOL REST API](https://apiservice.mol.gov.tw/OdService/rest/datastore/A17000000J-030243-XXL) | Annual economic indicators (Long-term trends) |
| `get_macro_global_stock_indices` | [MOL REST API](https://apiservice.mol.gov.tw/OdService/rest/datastore/A17030000J-000050-Ipz) | Monthly global stock indices (TW/US/JP/EU) |
| `get_macro_forex_rates_monthly` | [MOL REST API](https://apiservice.mol.gov.tw/OdService/rest/datastore/A17030000J-000049-Iq0) | Monthly forex rate summary for major countries |
| `get_macro_global_stock_indices_annual` | [MOL REST API](https://apiservice.mol.gov.tw/OdService/rest/datastore/A17000000J-030245-4Ml) | Annual global stock index trends |
| `get_macro_forex_rates_annual` | [MOL REST API](https://apiservice.mol.gov.tw/OdService/rest/datastore/A17000000J-030185-CKf) | Annual forex rate summary for major countries |
| `get_bank_bond_issuance_monthly` | [MOL REST API](https://apiservice.mol.gov.tw/OdService/rest/datastore/A17030000J-000048-YHK) | Monthly domestic bond issuance overview |
| `get_bank_stock_issuance_monthly` | [MOL REST API](https://apiservice.mol.gov.tw/OdService/rest/datastore/A17030000J-000047-Y4N) | Monthly domestic stock issuance overview |
| `get_bank_pension_fund_stats_monthly` | [MOL REST API](https://apiservice.mol.gov.tw/OdService/rest/datastore/A17030000J-000045-2qm) | National Pension Fund monthly operation stats |
| `get_corp_moea_business_registration` | [GCIS NAT API](https://data.gcis.nat.gov.tw/od/data/api/) | MOEA corporate business registration data |

## 🪙 Cryptocurrency & System

| Tool Name | Direct API URL (Source) | Description |
|-----------|-------------------------|-------------------|
| `get_crypto_btc_twd_price` | [CoinGecko](https://www.coingecko.com/en/coins/bitcoin) | Real-time BTC TWD/USD price |
| `get_crypto_eth_twd_price` | [CoinGecko](https://www.coingecko.com/en/coins/ethereum) | Real-time ETH TWD/USD price |
| `get_crypto_sol_twd_price` | [CoinGecko](https://www.coingecko.com/en/coins/solana) | Real-time SOL quotes and performance |
| `get_crypto_market_fear_greed_index` | [Alternative.me](https://alternative.me/crypto/fear-and-greed-index/) | Global crypto Fear & Greed index |
| `get_current_time_taipei` | Local Environment | Get Taipei real-time system time |

---
*Total Active Verified Tools: 58*
*Last Updated: 2026-02-09*
