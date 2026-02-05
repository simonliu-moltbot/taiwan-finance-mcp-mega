# 🛠️ Taiwan Finance MCP Mega - Verified Tools List (v3.4.9)

本文件僅列出目前**已完成實體邏輯對接 (100% 真實數據)** 的工具。
所有工具均對接政府公開 API (TWSE, TPEx, DGBAS, MOF, MOEA, CPC) 或全球市場 Public API (Yahoo Finance, CoinGecko, FRED)。

---

## 📈 1. 台灣股市 (Taiwan Stocks)
對接：臺灣證券交易所 (TWSE)、證券櫃檯買賣中心 (TPEx)

| 工具 ID | 說明 | 數據源 |
| :--- | :--- | :--- |
| `stock_realtime_quotes` | 上市個股當日即時行情 | TWSE |
| `stock_fundamental_eps` | 上市公司 EPS 統計排名 | TWSE |
| `stock_dividend_yield` | 個股本益比、殖利率、淨值比 | TWSE |
| `stock_chip_institutional_flow` | 三大法人買賣超彙總 | TWSE |
| `stock_margin_balance_monitor` | 全市場融資融券餘額明細 | TWSE |
| `stock_odd_lot_quotes` | 盤中零股交易即時行情 | TWSE |
| `stock_announcements` | 上市公司每日重大訊息 | TWSE |
| `stock_price_limit_tracker` | 個股漲跌停價預告 | TWSE |
| `stock_financial_report_general` | 公發公司資產負債表 (一般業) | TWSE |
| `stock_monthly_revenue` | 上市公司每月營業收入彙總 | TWSE |
| `stock_listed_company_basic_info` | 上市公司基本註冊資料 | TWSE |
| `stock_etf_regular_savings_rank` | 定期定額交易戶數統計排行 | TWSE |
| `stock_block_trade_summary` | 鉅額交易成交量值統計 | TWSE |
| `stock_tpex_quotes_realtime` | 上櫃個股即時行情與基本資料 | TPEx |

### 🌿 ESG & 公司治理 (Stocks ESG)
| 工具 ID | 說明 | 數據源 |
| :--- | :--- | :--- |
| `stock_esg_ghg_emissions` | 企業溫室氣體排放量 (範疇一/二/三) | TWSE |
| `stock_esg_occupational_safety` | 企業職業安全衛生統計 | TWSE |
| `stock_esg_waste_management` | 企業廢棄物管理數據 | TWSE |
| `stock_esg_water_resources` | 企業水資源管理與密集度 | TWSE |
| `stock_esg_food_safety` | 食品業安全管理與驗證統計 | TWSE |

---

## 🌍 2. 全球宏觀與加密貨幣 (Global Macro & Crypto)
對接：Yahoo Finance, FRED, CoinGecko (100% 免 Token)

| 工具 ID | 說明 | 數據源 |
| :--- | :--- | :--- |
| `global_fed_rates` | 美國聯準會基準利率代理指標 | Yahoo Finance |
| `global_vix_index` | CBOE 恐慌指數 (VIX) | Yahoo Finance |
| `global_baltic_dry` | 波羅的海乾散貨指數 (BDI) | Trading Economics |
| `crypto_btc_realtime` | 比特幣即時價格與 24h 漲跌 (TWD/USD) | CoinGecko |
| `crypto_eth_realtime` | 以太幣即時價格與 24h 漲跌 (TWD/USD) | CoinGecko |
| `crypto_sol_realtime` | Solana 即時價格與 24h 漲跌 (TWD/USD) | CoinGecko |

---

## 🏛️ 3. 宏觀經濟與政府數據 (Macro & Gov)
對接：主計總處 (DGBAS)、財政部 (MOF)、中油 (CPC)、經濟部 (MOEA)

| 工具 ID | 說明 | 數據源 |
| :--- | :--- | :--- |
| `macro_gdp_growth_quarterly` | 台灣經濟成長率 (GDP) | DGBAS |
| `macro_cpi_inflation_rate` | 消費者物價指數 (CPI) 年增率 | DGBAS |
| `macro_unemployment_rate_tw` | 台灣經季節調整後失業率 | DGBAS |
| `macro_avg_monthly_salary` | 台灣每月名目總薪資統計 | DGBAS |
| `tax_revenue_collection` | 全國賦稅收入統計月報 | MOF |
| `corp_company_registration` | 商工登記公示資料 (統編、地址、資本額) | MOEA |
| `corp_industry_production_index`| 工業生產指數與年增率 | MOEA |
| `macro_fuel_prices` | 台灣中油 (CPC) 當週掛牌油價 (92/95/98) | CPC |

---

## 💱 4. 即時匯率 (Forex)
對接：ExchangeRate-API (Market Mid-Rates)

| 工具 ID | 說明 | 數據源 |
| :--- | :--- | :--- |
| `forex_usd_twd` | 美元兌台幣即時匯率 | Market Data |
| `forex_jpy_twd` | 日幣兌台幣即時匯率 | Market Data |
| `forex_eur_twd` | 歐元兌台幣即時匯率 | Market Data |
| `forex_cny_twd` | 人民幣兌台幣即時匯率 | Market Data |

---

## 🚧 開發中 (Pending)
以下類別目前僅回傳結構化 Placeholder，實體邏輯正在開發中：
- `bank_*` (銀行與信貸類)
- `tax_*` (大部分稅務計算類)

---
*最後更新日期：2026-02-05 13:18*
*所有數據僅供參考，請以各官方網站公告為準。*
