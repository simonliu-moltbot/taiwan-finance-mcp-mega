# 🛠️ Taiwan Finance MCP Mega - Verified Tools List (v4.6.0)

This document lists all tools that have **completed logic implementation (100% authentic data)** and have been optimized for semantic clarity and stability.
All tools interface with official public APIs; Web Scraping is strictly prohibited.

---

## 📈 1. Taiwan Stocks Core (24 Tools)
*Focusing on Taiwan Stock Exchange (TWSE) and TPEx data.*

| Tool ID | Description (Brackets indicate semantic labels) | Source |
| :--- | :--- | :--- |
| `get_stock_quotes_realtime_all` | Real-time quotes for listed companies (Open/High/Low/Close/Vol) | TWSE |
| `get_stock_eps_ranking_summary` | EPS statistics and ranking for listed companies | TWSE |
| `get_stock_dividend_yield_pe_pb` | PE ratio, dividend yield, and PB ratio valuation | TWSE |
| `get_stock_institutional_summary_twse` | **[Listed/Main]** Institutional investor net flow summary (Totals) | TWSE |
| `get_stock_institutional_details_tpex` | **[OTC]** Institutional investor net flow details per stock | TPEx |
| `get_stock_institutional_summary_tpex` | **[OTC]** Institutional investor net flow summary (Totals) | TPEx |
| `get_stock_margin_trading_balance` | Detailed margin trading and short selling balances | TWSE |
| `get_stock_odd_lot_trading_quotes` | Real-time odd-lot trading quotes | TWSE |
| `get_stock_mops_significant_announcements` | Significant daily announcements (MOPS) | TWSE |
| `get_stock_price_limit_up_down_tracker` | Monitor daily price limits (Limit Up/Down) | TWSE |
| `get_stock_monthly_revenue_summary` | **[Revenue Report]** Monthly revenue summary and growth rates | TWSE |
| `get_stock_etf_regular_savings_ranking` | **[Popularity]** Ranking of ETF regular savings account counts | TWSE |
| `get_stock_block_trade_daily_summary` | Block trade daily volume and value statistics | TWSE |
| `get_stock_after_hours_trading_info` | After-hours fixed-price trading information | TWSE |
| `get_stock_individual_average_price` | **[Individual/Avg]** Monthly closing average price trend for a stock | TWSE |
| `get_stock_yield_averages_by_industry` | Dividend yield statistics by industry | TWSE |
| `get_stock_pe_averages_by_industry` | PE ratio statistics by industry (valuation comparison) | TWSE |
| `get_stock_broker_list_all` | Comprehensive contact list of stock brokers in Taiwan | TWSE |
| `get_stock_buyback_treasury_status` | Treasury stock buyback progress and status | TWSE |
| `get_stock_broker_regular_savings_data` | **[Broker/Services]** List of brokers offering regular savings plans | TWSE |
| `get_stock_listed_investor_profile` | **[Listed/Invest]** Profile: Spokesperson, listing date, URL, etc. | TWSE |
| `get_stock_otc_investor_profile` | **[OTC/Invest]** Profile: Spokesperson, listing date, URL, etc. | TPEx |
| `get_stock_public_investor_profile` | **[Public/Invest]** Profile: Investment data for publicly issued companies | TWSE |
| `get_stock_daily_closing_quotes_all` | Daily closing index and volume overview by category | TWSE |

---

## 📉 2. Derivatives (3 Tools)
*Targeting Taiwan Futures Exchange (Taifex) data. Limits output to 20 records for stability.*

| Tool ID | Description | Source |
| :--- | :--- | :--- |
| `get_futures_quotes_daily` | Daily settlement prices and closing market data (Max 20) | Taifex |
| `get_futures_institutional_investor_flow` | Summary of institutional net flow and open interest | Taifex |
| `get_futures_open_interest_ranking` | Open interest ranking of large futures traders (Max 20) | Taifex |

---

## 🌍 3. Forex & Commodities (14 Tools)
| Tool ID | Description | Source |
| :--- | :--- | :--- |
| `get_forex_[CUR]_twd_realtime` | Real-time exchange rates vs TWD (e.g., USD, JPY) | rter.info |
| `get_forex_any_to_any_conversion` | Real-time currency conversion between any two currencies | rter.info |
| `get_commodity_oil_wti_price_usd` | Real-time WTI crude oil price (USD/Barrel) | MOEA |
| `get_commodity_oil_brent_price_usd` | Real-time Brent crude oil price | MOEA |
| `get_commodity_gold_spot_price_twd` | Real-time gold spot price (TWD) | TPEx |

---

## 🏛️ 4. Macroeconomics & Corporate (13 Tools)
| Tool ID | Description | Source |
| :--- | :--- | :--- |
| `get_macro_gdp_growth_rate_quarterly` | Taiwan quarterly GDP growth rate | DGBAS |
| `get_macro_monthly_financial_indicators` | Monthly indicators (M1B/M2/Reserves) | CBC |
| `get_macro_economic_indicators_monthly` | Monthly indicators (CPI/Unemployment/Wages) | DGBAS |
| `get_macro_economic_indicators_annual` | Annual economic indicators (Long-term trends) | DGBAS |
| `get_macro_global_stock_indices` | **[Indices]** Monthly global indices (TW/US/JP/EU) | MOL |
| `get_macro_forex_rates_monthly` | **[Historical]** Monthly forex rate trends for major currencies | MOL |
| `get_macro_global_stock_indices_annual` | **[Indices]** Annual global stock index trends | MOL |
| `get_macro_forex_rates_annual` | **[Historical]** Annual historical forex rate summary | MOL |
| `get_corp_moea_business_registration` | Corporate business registration data (All TW companies) | MOEA |

---

## 🏦 5. Bank & Financial Issuance (3 Tools)
| Tool ID | Description | Source |
| :--- | :--- | :--- |
| `get_bank_bond_issuance_monthly` | Monthly domestic bond issuance (Gov/Corp bonds) | MOL |
| `get_bank_stock_issuance_monthly` | Monthly stock issuance and capital increase statistics | MOL |
| `get_bank_pension_fund_stats_monthly` | National Pension Fund monthly operation and yield stats | MOL |

---

## 🪙 6. Cryptocurrency (4 Tools)
| Tool ID | Description | Source |
| :--- | :--- | :--- |
| `get_crypto_btc_twd_price` | Real-time BTC price and 24h change | CoinGecko |
| `get_crypto_eth_twd_price` | Real-time ETH price and 24h change | CoinGecko |
| `get_crypto_sol_twd_price` | Real-time SOL quotes and market performance | CoinGecko |
| `get_crypto_market_fear_greed_index` | Global crypto Fear & Greed index | Alt.me |

---

## 🕒 7. Common Tools (1 Tool)
| Tool ID | Description |
| :--- | :--- |
| `get_current_time_taipei` | Get Taipei real-time system time, date, and day of the week. |

---
*Last Updated: 2026-02-09*
*Version: v4.6.0 Semantic Optimized*
