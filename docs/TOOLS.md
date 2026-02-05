# 🛠️ Taiwan Finance MCP Mega - Full Semantic Tools List (v3.7.1)

本文件列出 **74 個已實體化語義優化 (Semantic Optimized)** 的專業工具。
所有工具均對接政府公開 API (TWSE, TPEx, DGBAS, MOF, MOEA, CPC) 或全球市場 Public API (Yahoo Finance, CoinGecko)。

---

## 📈 1. 台灣股市核心 (Taiwan Stocks Core - 17 Tools)
對接：臺灣證券交易所 (TWSE)、證券櫃檯買賣中心 (TPEx)

| 工具 ID | 說明 | 數據源 |
| :--- | :--- | :--- |
| `get_stock_quotes_realtime_all` | 上市個股當日即時行情 | TWSE |
| `get_stock_eps_ranking_summary` | 上市公司 EPS 統計排名 | TWSE |
| `get_stock_dividend_yield_pe_pb` | 個股本益比、殖利率、淨值比估值 | TWSE |
| `get_stock_institutional_investor_flow` | 三大法人買賣超彙總統計 | TWSE |
| `get_stock_margin_trading_balance` | 全市場融資融券餘額明細 | TWSE |
| `get_stock_odd_lot_trading_quotes` | 盤中零股交易即時行情 | TWSE |
| `get_stock_mops_significant_announcements` | 公開資訊觀測站 (MOPS) 重大訊息 | TWSE |
| `get_stock_price_limit_up_down_tracker` | 個股漲跌停價預告 | TWSE |
| `get_stock_balance_sheet_general` | 公發公司資產負債表 (一般業) | TWSE |
| `get_stock_monthly_revenue_summary` | 上市公司每月營業收入彙總 | TWSE |
| `get_stock_listed_company_basic_info` | 上市公司基本登記與掛牌資料 | TWSE |
| `get_stock_etf_regular_savings_ranking` | 定期定額交易戶數排行 | TWSE |
| `get_stock_block_trade_daily_summary` | 鉅額交易成交量值統計表 | TWSE |
| `get_stock_after_hours_trading_info` | 盤後定價交易資訊 | TWSE |
| `get_stock_ipo_new_listing_schedule` | 新股上市與 IPO 時程預告 | TWSE |
| `get_stock_buyback_treasury_status` | 庫藏股買回進度統計 | TWSE |
| `get_stock_broker_regular_savings_data` | 開辦定期定額業務之證券商名單 | TWSE |

---

## 🌿 2. 企業 ESG 資訊 (Stock ESG Indicators - 21 Tools)
對接：證交所企業永續發展揭露平台

| 工具 ID | 說明 |
| :--- | :--- |
| `get_stock_esg_greenhouse_gas_emissions` | 溫室氣體排放量 (範疇一/二/三) |
| `get_stock_esg_energy_management_efficiency` | 能源管理使用率與效率 |
| `get_stock_esg_water_resource_usage` | 水資源管理與密集度數據 |
| `get_stock_esg_waste_management_data` | 廢棄物處理重量與驗證統計 |
| `get_stock_esg_human_capital_development` | 員工薪資與人力發展統計 |
| `get_stock_esg_board_diversity_structure` | 董事會組成、性別比例與席次 |
| `get_stock_esg_investor_communication_index` | 投資人溝通與法說會次數 |
| `get_stock_esg_climate_change_governance` | 氣候相關議題管理與監督 |
| `get_stock_esg_functional_committee_status` | 薪酬與審計委員會出席率 |
| `get_stock_esg_fuel_management_stats` | 企業消耗燃料總量與類型百分比 |
| `get_stock_esg_product_life_cycle_management` | 產品生命週期與回收管理 |
| `get_stock_esg_food_safety_verification` | 食品安全管理、認證與支出統計 |
| `get_stock_esg_supply_chain_management_audit` | 供應商稽核與符合認證百分比 |
| `get_stock_esg_product_quality_safety` | 產品品質、重量與生產設施數 |
| `get_stock_esg_local_community_relations` | 企業與人口密集區社區關係 |
| `get_stock_esg_information_security_breach` | 資訊安全外洩事件統計揭露 |
| `get_stock_esg_inclusive_finance_promotion` | 普惠金融與弱勢族群金融教育 |
| `get_stock_esg_shareholding_control_power` | 前 10 大股東持股與控制力 |
| `get_stock_esg_risk_management_policy` | 重大事件風險管理政策描述 |
| `get_stock_esg_anti_competitive_litigation` | 反競爭行為法律訴訟損失統計 |
| `get_stock_esg_occupational_safety_health` | 職業災害人數與安全衛生比率 |

---

## 🌍 3. 全球金融與加密貨幣 (Global & Crypto - 15 Tools)
對接：Yahoo Finance, Trading Economics, CoinGecko (100% 免 Token)

| 工具 ID | 說明 | 數據源 |
| :--- | :--- | :--- |
| `get_forex_usd_twd_realtime` | 美元兌台幣即時匯率 | Market Data |
| `get_forex_jpy_twd_realtime` | 日幣兌台幣即時匯率 | Market Data |
| `get_forex_eur_twd_realtime` | 歐元兌台幣即時匯率 | Market Data |
| `get_forex_cny_twd_realtime` | 人民幣兌台幣即時匯率 | Market Data |
| `get_forex_hkd_twd_realtime` | 港幣兌台幣即時匯率 | Market Data |
| `get_forex_gbp_twd_realtime` | 英鎊兌台幣即時匯率 | Market Data |
| `get_forex_aud_twd_realtime` | 澳幣兌台幣即時匯率 | Market Data |
| `get_forex_cad_twd_realtime` | 加幣兌台幣即時匯率 | Market Data |
| `get_forex_sgd_twd_realtime` | 新幣兌台幣即時匯率 | Market Data |
| `get_forex_krw_twd_realtime` | 韓元兌台幣即時匯率 | Market Data |
| `get_commodity_oil_wti_price_usd` | WTI 原油期貨即時報價 (USD) | Yahoo Finance |
| `get_commodity_oil_brent_price_usd` | 布蘭特原油期貨即時報價 (USD) | Yahoo Finance |
| `get_commodity_gold_spot_price_twd` | 黃金現貨即時價格 (TWD) | Yahoo Finance |
| `get_commodity_silver_spot_price_twd` | 白銀現貨即時價格 (TWD) | Yahoo Finance |
| `get_commodity_baltic_dry_index_bdi` | 波羅的海乾散貨指數 (BDI) | Trading Economics |

---

## 🏛️ 4. 台灣宏觀與政府數據 (Macro & Gov - 13 Tools)
對接：主計總處 (DGBAS)、財政部 (MOF)、中油 (CPC)、經濟部 (MOEA)

| 工具 ID | 說明 | 數據源 |
| :--- | :--- | :--- |
| `get_macro_gdp_growth_rate_quarterly` | 台灣經濟成長率 (GDP) | DGBAS |
| `get_macro_cpi_inflation_rate_tw` | 消費者物價指數 (CPI) 年增率 | DGBAS |
| `get_macro_unemployment_rate_seasonal_adjusted`| 經季節調整後失業率 | DGBAS |
| `get_macro_average_monthly_salary_dgbas` | 每月名目總薪資統計 | DGBAS |
| `get_macro_fuel_price_cpc_retail` | 中油當週掛牌油價 (92/95/98/柴油) | CPC |
| `get_tax_revenue_collection_monthly` | 全國賦稅收入統計月報 | MOF |
| `get_tax_income_bracket_calculator` | 台灣綜合所得稅級距與試算 | MOF |
| `get_tax_electronic_invoice_usage_stats` | 電子發票推廣與使用率統計 | MOF |
| `get_corp_moea_business_registration` | 商工登記公示資料 (統編、負責人、地址) | MOEA |
| `get_corp_industry_production_index` | 工業生產指數與變動率 | MOEA |
| `get_corp_factory_count_statistics` | 全台工廠登記數量統計 | MOEA |
| `get_corp_export_value_by_industry` | 按行業別劃分之出口貿易總值 | MOEA |
| `get_crypto_market_fear_greed_index` | 加密貨幣市場恐慌貪婪指數 | CoinGecko |

---

## 🪙 5. 加密貨幣即時報價 (Crypto - 8 Tools)
對接：CoinGecko Public API (100% 免 Token)

| 工具 ID | 說明 | 幣種 |
| :--- | :--- | :--- |
| `get_crypto_btc_twd_price` | 比特幣即時價格與 24h 漲跌 | BTC |
| `get_crypto_eth_twd_price` | 以太幣即時價格與 24h 漲跌 | ETH |
| `get_crypto_sol_twd_price` | Solana 即時價格與 24h 漲跌 | SOL |
| `get_bank_deposit_rate_fixed` | 台灣主要銀行定期存款利率 | Bank Data |
| `get_bank_mortgage_rate_average` | 台灣平均購屋貸款利率趨勢 | Bank Data |
| `get_bank_credit_card_delinquency` | 信用卡逾期帳款與簽帳總額統計 | Bank Data |
| `get_bank_atm_location_map` | 全台 ATM 網點與設置位置分布 | Bank Data |
| `get_bank_capital_adequacy_ratio` | 本國銀行資本適足率指標 | Bank Data |

---
*最後更新日期：2026-02-05 15:35*
*版本：v3.7.1 Complete Semantic Mapping*
