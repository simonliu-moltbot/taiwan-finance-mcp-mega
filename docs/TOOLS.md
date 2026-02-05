# 🛠️ Taiwan Finance MCP Mega - Verified Tools List (v3.7.0)

本文件僅列出目前**已完成實體邏輯對接 (100% 真實數據)** 並通過語義化優化 (Semantic Optimized) 的工具。
所有工具均對接政府公開 API (TWSE, TPEx, DGBAS, MOF, MOEA, CPC) 或全球市場 Public API (Yahoo Finance, CoinGecko)。

---

## 📈 1. 台灣股市核心 (Taiwan Stocks Core)
對接：臺灣證券交易所 (TWSE)、證券櫃檯買賣中心 (TPEx)

| 工具 ID | 說明 | 數據源 |
| :--- | :--- | :--- |
| `get_stock_quotes_realtime_all` | 上市個股當日即時行情 (開高低收/量) | TWSE |
| `get_stock_eps_ranking_summary` | 上市公司每股盈餘 (EPS) 統計排名 | TWSE |
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

---

## 🌿 2. 企業 ESG 指標 (Stock ESG Indicators)
對接：證交所企業永續發展揭露平台 (21 項關鍵指標)

| 工具 ID | 說明 |
| :--- | :--- |
| `get_stock_esg_greenhouse_gas_emissions` | 溫室氣體排放量 (範疇一/二/三) |
| `get_stock_esg_energy_management_efficiency` | 能源管理使用率與效率 |
| `get_stock_esg_water_resource_usage` | 水資源管理與密集度數據 |
| `get_stock_esg_waste_management_data` | 廢棄物處理重量與驗證統計 |
| `get_stock_esg_occupational_safety_health` | 職業災害人數與安全衛生比率 |
| `get_stock_esg_food_safety_verification` | 食品業專用安全管理統計 |
| `get_stock_esg_information_security_breach` | 資訊安全外洩事件統計揭露 |
| `get_stock_esg_board_diversity_structure` | 董事會組成、性別比例與席次 |

---

## 🌍 3. 全球金融與加密貨幣 (Global & Crypto)
對接：Yahoo Finance, FRED, CoinGecko (100% 免 Token)

| 工具 ID | 說明 | 數據源 |
| :--- | :--- | :--- |
| `get_forex_usd_twd_realtime` | 美元兌台幣即時匯率 | Market Data |
| `get_forex_jpy_twd_realtime` | 日幣兌台幣即時匯率 | Market Data |
| `get_commodity_oil_wti_price_usd` | WTI 原油期貨即時報價 (USD) | Yahoo Finance |
| `get_commodity_oil_brent_price_usd` | 布蘭特原油期貨即時報價 (USD) | Yahoo Finance |
| `get_commodity_baltic_dry_index_bdi` | 波羅的海乾散貨指數 (BDI) | Trading Economics |
| `get_crypto_btc_twd_price` | 比特幣即時價格與 24h 漲跌 | CoinGecko |
| `get_crypto_eth_twd_price` | 以太幣即時價格與 24h 漲跌 | CoinGecko |

---

## 🏛️ 4. 台灣宏觀經濟 (Taiwan Macro)
對接：主計總處 (DGBAS)、財政部 (MOF)、中油 (CPC)、經濟部 (MOEA)

| 工具 ID | 說明 | 數據源 |
| :--- | :--- | :--- |
| `get_macro_gdp_growth_rate_quarterly` | 台灣經濟成長率 (GDP) | DGBAS |
| `get_macro_cpi_inflation_rate_tw` | 消費者物價指數 (CPI) 年增率 | DGBAS |
| `get_macro_unemployment_rate_seasonal_adjusted`| 經季節調整後失業率 | DGBAS |
| `get_macro_average_monthly_salary_dgbas` | 每月名目總薪資統計 | DGBAS |
| `get_macro_fuel_price_cpc_retail` | 中油當週掛牌油價 (92/95/98/柴油) | CPC |
| `get_tax_revenue_collection_monthly` | 全國賦稅收入統計月報 | MOF |
| `get_corp_moea_business_registration` | 商工登記公示資料 (統編、地址、負責人) | MOEA |
| `get_corp_industry_production_index` | 工業生產指數與變動率 | MOEA |

---
*最後更新日期：2026-02-05*
*版本：v3.7.0 Semantic Overhaul*
