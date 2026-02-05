# 🛠️ Taiwan Finance MCP Mega - Verified Tools List (v4.0.0)

本文件僅列出目前**已完成實體邏輯對接 (100% 真實數據)** 並通過語義化優化 (Semantic Optimized) 的工具。
所有工具均對接政府公開 API (TWSE, TPEx, DGBAS, MOF, MOEA, CPC) 或全球市場 Public API (Yahoo Finance, CoinGecko)。

---

## 📈 1. 台灣股市核心 (Taiwan Stocks Core - 17 Tools)
對接：臺灣證券交易所 (TWSE)、證券櫃檯買賣中心 (TPEx)

| 工具 ID | 說明 | 數據源 |
| :--- | :--- | :--- |
| `get_stock_quotes_realtime_all` | 上市個股當日即時行情 (開高低收/量) | TWSE |
| `get_stock_eps_ranking_summary` | 上市公司 每股盈餘 (EPS) 統計排名 | TWSE |
| `get_stock_dividend_yield_pe_pb` | 個股本益比、殖利率、淨值比估值 | TWSE |
| `get_stock_institutional_investor_flow` | 三大法人買賣超彙總統計 | TWSE |
| `get_stock_margin_trading_balance` | 全市場融資融券餘額明細 | TWSE |
| `get_stock_odd_lot_trading_quotes` | 盤中零股交易即時行情 | TWSE |
| `get_stock_mops_significant_announcements` | 公開資訊觀測站 (MOPS) 重大訊息 | TWSE |
| `get_stock_price_limit_up_down_tracker` | 個股漲跌停價預告 | TWSE |
| `get_stock_balance_sheet_general` | 公發公司資產負債表 (一般業) | TWSE |
| `get_stock_monthly_revenue_summary` | 上市公司每月營業收入彙總與增減比 | TWSE |
| `get_stock_listed_company_basic_info` | 上市公司基本登記與掛牌資料 | TWSE |
| `get_stock_etf_regular_savings_ranking` | 定期定額交易戶數排行 (個股/ETF) | TWSE |
| `get_stock_block_trade_daily_summary` | 鉅額交易成交量值統計表 | TWSE |
| `get_stock_after_hours_trading_info` | 盤後定價交易資訊 | TWSE |
| `get_stock_ipo_new_listing_schedule` | 新股上市與 IPO 時程預告 | TWSE |
| `get_stock_buyback_treasury_status` | 庫藏股買回進度與執行狀態 | TWSE |
| `get_stock_broker_regular_savings_data` | 開辦定期定額業務之證券商名單 | TWSE |

---

## 🌍 2. 全球金融、匯率與大宗商品 (Forex & Global - 15 Tools)
對接：ExchangeRate-API, 經濟部能源署 (MOEA), Yahoo Finance

| 工具 ID | 說明 | 數據源 |
| :--- | :--- | :--- |
| `get_forex_usd_twd_realtime` | 美元兌台幣即時匯率 | Market Data |
| `get_forex_jpy_twd_realtime` | 日幣兌台幣即時匯率 | Market Data |
| `get_commodity_oil_wti_price_usd` | WTI 原油價格 (USD/Barrel) | MOEA (政府源) |
| `get_commodity_oil_brent_price_usd` | 布蘭特原油價格 (USD/Barrel) | MOEA (政府源) |
| `get_commodity_baltic_dry_index_bdi` | 波羅的海乾散貨指數 (BDI) | Trading Economics |
| `get_global_market_vix_index` | CBOE 恐慌指數 (VIX) | Yahoo Finance |
| `get_global_fed_funds_rate` | 美國聯準會基準利率代理指標 | Yahoo Finance |

---

## 🏛️ 3. 台灣宏觀經濟與政府數據 (Macro & Gov - 13 Tools)
對接：主計總處 (DGBAS)、財政部 (MOF)、中油 (CPC)、經濟部 (MOEA)

| 工具 ID | 說明 | 數據源 |
| :--- | :--- | :--- |
| `get_macro_gdp_growth_rate_quarterly` | 台灣經濟成長率 (GDP) | DGBAS |
| `get_macro_cpi_inflation_rate_tw` | 消費者物價指數 (CPI) 年增率 | MOL / DGBAS |
| `get_macro_unemployment_rate_seasonal_adjusted`| 經季節調整後失業率 | MOL / DGBAS |
| `get_macro_average_monthly_salary_dgbas` | 每月名目總薪資統計 | MOL / DGBAS |
| `get_macro_fuel_price_cpc_retail` | 中油當週掛牌零售油價 (92/95/98/柴油) | CPC |
| `get_tax_revenue_collection_monthly` | 全國賦稅收入統計月報 | MOF |
| `get_corp_moea_business_registration` | 商工登記公示資料 (統編、負責人、地址) | MOEA |
| `get_corp_industry_production_index` | 工業生產指數與變動率 | MOEA |

---

## 🪙 4. 加密貨幣即時報價 (Crypto - 4 Tools)
對接：CoinGecko Public API (100% 免 Token)

| 工具 ID | 說明 | 數據源 |
| :--- | :--- | :--- |
| `get_crypto_btc_twd_price` | 比特幣即時價格與 24h 漲跌 | CoinGecko |
| `get_crypto_eth_twd_price` | 以太幣即時價格與 24h 漲跌 | CoinGecko |
| `get_crypto_sol_twd_price` | Solana 即時價格與 24h 漲跌 | CoinGecko |
| `get_crypto_market_fear_greed_index` | 加密貨幣市場恐慌與貪婪指數 | CoinGecko |

---

## 🕒 5. 系統通用工具 (Common - 1 Tool)
| 工具 ID | 說明 |
| :--- | :--- |
| `get_current_time_taipei` | 獲取台北 (Asia/Taipei) 現下的精確系統時間與星期幾。 |

---
*最後更新日期：2026-02-05 17:48*
*版本：v4.0.0 Refined Edition*
