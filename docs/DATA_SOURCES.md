# Detailed Tool-to-Source Mapping

This registry provides a direct mapping for every tool in the `taiwan-finance-mcp-mega` project to its specific data source and API endpoint. Use this for debugging data integrity or verifying connectivity.

---

## 📈 Stock Market (TWSE / TPEx)
*Data provided by the Taiwan Stock Exchange (TWSE) and Taipei Exchange (TPEx) OpenAPI.*

| Tool Name | Endpoint / Source | Description |
|-----------|-------------------|-------------|
| `get_stock_quotes_realtime_all` | `TWSE:/exchangeReport/STOCK_DAY_ALL` | Real-time quotes for all listed stocks. |
| `get_stock_eps_ranking_summary` | `TWSE:/opendata/t187ap14_L` | EPS ranking for listed companies. |
| `get_stock_dividend_yield_pe_pb` | `TWSE:/exchangeReport/BWIBBU_d` | PE, PB, and Dividend Yield. |
| `get_stock_institutional_investor_flow` | `TWSE:/fund/BFI82U` | Daily institutional buy/sell summary. |
| `get_stock_margin_trading_balance` | `TWSE:/exchangeReport/MI_MARGN` | Margin trading and short selling balance. |
| `get_stock_odd_lot_trading_quotes` | `TWSE:/exchangeReport/TWT53U` | Intraday odd-lot trading prices. |
| `get_stock_mops_significant_announcements` | `TWSE:/opendata/t187ap04_L` | Material information from MOPS. |
| `get_stock_price_limit_up_down_tracker` | `TWSE:/exchangeReport/TWT84U` | Limit up/down stocks list. |
| `get_stock_balance_sheet_general` | `TWSE:/opendata/t187ap07_X_ci` | General balance sheets. |
| `get_stock_monthly_revenue_summary` | `TWSE:/opendata/t187ap05_L` | Monthly revenue aggregation. |
| `get_stock_listed_company_basic_info` | `TWSE:/opendata/t187ap03_L` | Company profile (Tax ID, address, etc.). |
| `get_stock_etf_regular_savings_ranking` | `TWSE:/ETFReport/ETFRank` | ETF recurring investment popularity. |
| `get_stock_block_trade_daily_summary` | `TWSE:/block/BFIAUU_d` | Large block trade summary. |
| `get_stock_after_hours_trading_info` | `TWSE:/exchangeReport/BFT41U` | After-hours fixed-price trading. |
| `get_stock_ipo_new_listing_schedule` | `TWSE:/exchangeReport/TWT82U` | IPO and new listing schedules. |
| `get_stock_buyback_treasury_status` | `TWSE:/opendata/t187ap13_L` | Treasury stock buyback progress. |

## 📉 Derivatives (Taifex)
*Data provided by the Taiwan Futures Exchange (Taifex) OpenAPI.*

| Tool Name | Endpoint / Source | Description |
|-----------|-------------------|-------------|
| `get_futures_quotes_daily` | `Taifex:/v1/DailyQuotes` | Daily settlement and futures prices. |
| `get_futures_institutional_investor_flow` | `Taifex:/v1/InstitutionalInvestorsDaily` | Institutional net positions (Futures). |
| `get_futures_open_interest_ranking` | `Taifex:/v1/LargeTradersPositionsDaily` | Top trader open interest distribution. |

## 🌍 Forex & Commodities
*Real-time market rates and commodity indices.*

| Tool Name | Endpoint / Source | Description |
|-----------|-------------------|-------------|
| `get_forex_[CUR]_twd_realtime` | `ExchangeRate-API:open.er-api.com/v6/latest/` | Real-time FX (USD, JPY, EUR, etc.). |
| `get_commodity_oil_wti_price_usd` | `MOEA (Oil111 CSV)` | WTI crude oil price. |
| `get_commodity_oil_brent_price_usd` | `MOEA (Oil111 CSV)` | Brent crude oil price. |
| `get_commodity_gold_spot_price_twd` | `Yahoo Finance / Market Feed` | Gold spot price in TWD. |
| `get_commodity_silver_spot_price_twd` | `Yahoo Finance / Market Feed` | Silver spot price in TWD. |

## 🏛️ Macroeconomics & Gov Data
*National indicators and official government statistics.*

| Tool Name | Endpoint / Source | Description |
|-----------|-------------------|-------------|
| `get_macro_gdp_growth_rate_quarterly` | `MOL/DGBAS API` | Quarterly GDP growth metrics. |
| `get_macro_cpi_inflation_rate_tw` | `MOL API` | Consumer Price Index (Inflation). |
| `get_macro_unemployment_rate_seasonal_adjusted` | `MOL API` | Seasonally adjusted unemployment. |
| `get_macro_average_monthly_salary_dgbas` | `MOL API` | Average worker monthly salary. |
| `get_macro_fuel_price_cpc_retail` | `CPC:vipmbr.cpc.com.tw/openData/` | Weekly retail fuel prices. |
| `get_macro_housing_price_index_tw` | `MOI:quality.data.gov.tw/dq_download_json.php?nid=11545` | Residential price index. |
| `get_macro_national_debt_clock` | `MOF:Static / Registry Feed` | Current national debt status. |
| `get_macro_central_bank_policy_rate` | `CBC:Official Announcements` | Discount rate and policy interest. |

## 🏦 Banking & Corporate
*Financial institution performance and MOEA registrations.*

| Tool Name | Endpoint / Source | Description |
|-----------|-------------------|-------------|
| `get_bank_list_of_institutions` | `Data.gov.tw:nid=18419` | List of all financial institutions. |
| `get_bank_profit_loss_statements` | `Data.gov.tw:nid=28567` | Bank industry profit/loss reports. |
| `get_bank_sme_loan_balance_stats` | `FSC Open Data` | SME loan balance and counts. |
| `get_corp_moea_business_registration` | `GCIS:data.gcis.nat.gov.tw/od/data/api/` | Business registration search. |
| `get_corp_industry_production_index` | `MOEA Industry Index Feed` | Industrial production index. |
| `get_corp_industry_electricity_consumption_stats` | `MOEA:ECW/opendata/` | Power consumption by sector. |

## 🪙 Cryptocurrency
*Real-time crypto data from CoinGecko.*

| Tool Name | Endpoint / Source | Description |
|-----------|-------------------|-------------|
| `get_crypto_btc_twd_price` | `CoinGecko:/api/v3/simple/price?ids=bitcoin` | BTC price in TWD/USD. |
| `get_crypto_market_fear_greed_index` | `CoinGecko:Alternative.me Proxy` | Crypto market sentiment index. |

## 📰 Official News
*Direct feeds from regulatory bodies.*

| Tool Name | Endpoint / Source | Description |
|-----------|-------------------|-------------|
| `get_gov_financial_news_fsc` | `Data.gov.tw:nid=7334` | FSC official press releases. |
| `get_gov_central_bank_announcements` | `CBC:Official Site Feed` | Central Bank policy announcements. |
| `get_gov_industrial_policy_news_moea` | `MOEA News Feed` | Industrial and energy policy news. |

---
*Last Updated: 2026-02-09*
