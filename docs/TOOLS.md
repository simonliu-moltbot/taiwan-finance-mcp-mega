# 🏦 Taiwan Finance MCP Mega - 220+ 完整工具字典 (v2.7.0)

本手冊列出了所有正式註冊於 **Taiwan Finance MCP Mega** 的工具。為了確保 MLOps 等級的精確度，我們已棄用所有索引名稱，改用具備語義的明確功能 ID。

---

## 📈 1. 台股市場深度分析 (60 Tools)
*   `stock_realtime_quotes`: 個股即時報價
*   `stock_fundamental_eps`: 季度 EPS 分析
*   `stock_dividend_yield`: 現金殖利率計算
*   `stock_chip_institutional_flow`: 三大法人買賣超
*   `stock_technical_ma_signals`: 移動平均線多空
*   `stock_margin_balance_monitor`: 融資融券餘額
*   `stock_pe_ratio_ranking`: 全市場本益比排名
*   `stock_pb_ratio_analysis`: 股價淨值比解析
*   `stock_etf_dividend_calendar`: ETF 除息日曆
*   `stock_announcements`: 上市公司重大訊息
*   `stock_price_limit_tracker`: 今日漲跌停追蹤
*   `stock_revenue_growth_yoy`: 營收年增率分析
*   `stock_roe_dupoint_analysis`: 杜邦分析(ROE)
*   *(更多 47 項台股專業分析工具已全部部署於 stock_* 前綴下)*

---

## 💹 2. 全球匯率與大宗商品 (40 Tools)
*   `forex_usd_twd`: 美金/台幣即時匯率
*   `forex_jpy_twd`: 日幣/台幣即時匯率
*   `forex_bank_buying_max`: 全台銀行最高買入價比價
*   `forex_volatility_index_fx`: 匯率波動率指數
*   `forex_interbank_swap_rates`: 銀行同業拆解利率
*   `forex_fx_correlation_matrix`: 幣別相關性矩陣
*   `forex_gold_spot_twd`: 國際金價(台幣計價)
*   `forex_oil_wti_price`: WTI 原油即時行情
*   `forex_bdi_shipping_index`: 波羅的海乾散貨指數
*   *(更多 31 項匯率與商品工具已部署於 forex_* 前綴下)*

---

## 🏦 3. 銀行、稅務與信貸 (30 Tools)
*   `bank_mortgage_rate_avg`: 五大銀行平均房貸利率
*   `bank_personal_loan_index`: 個人信貸市場行情
*   `bank_credit_card_delinquency`: 信用卡逾期違約率
*   `bank_digital_bank_bonus`: 數位銀行優惠方案監控
*   `tax_income_brackets`: 個人所得稅課稅級距
*   `tax_house_tax_rates`: 各縣市囤房稅率分布
*   `tax_land_value_increment`: 土地增值稅計算基礎
*   `tax_gift_estate_limits`: 遺贈稅免稅額度查詢
*   *(更多 22 項銀行稅務工具已部署於 bank_* / tax_* 前綴下)*

---

## 🏛️ 4. 企業登記、ESG 與產業 (30 Tools)
*   `corp_company_registration`: 全國公司商工登記查詢
*   `corp_factory_count_stats`: 全台工廠登記地理統計
*   `corp_esg_carbon_emission`: 企業碳排放揭露概況
*   `corp_legal_suit_count`: 企業法律訴訟揭露次數
*   `corp_procurement_winner_rank`: 政府標案得標商排名
*   `corp_trade_balance_monitor`: 進出口貿易差額監控
*   `corp_patent_registration_stats`: 專利權登記趨勢
*   *(更多 22 項企業數據工具已部署於 corp_* 前綴下)*

---

## 📊 5. 宏觀經濟與政府支出 (30 Tools)
*   `macro_cpi_inflation_rate`: 台灣 CPI 通膨監控
*   `macro_gdp_growth_quarterly`: 季度 GDP 成長率
*   `macro_government_debt_clock`: 國債鐘即時數據
*   `macro_unemployment_rate_tw`: 台灣最新失業率
*   `macro_central_bank_interest_rate`: 央行基準利率
*   `macro_electricity_reserve_margin`: 台電備轉容量率
*   `macro_water_reservoir_levels`: 全台水庫即時蓄水量
*   *(更多 23 項宏觀工具已部署於 macro_* 前綴下)*

---

## ₿ 6. Web3 與加密貨幣監控 (20 Tools)
*   `crypto_btc_realtime`: 比特幣即時報價
*   `crypto_fear_greed`: 市場恐懼與貪婪指數
*   `crypto_stablecoin_market_cap`: 穩定幣發行量監控
*   `crypto_eth_gas_tracker`: 以太坊即時 Gas 費
*   `crypto_defi_total_value_locked`: DeFi 協議鎖倉量
*   `crypto_whale_transaction_tracker`: 鯨魚大額交易監控
*   *(更多 14 項 Web3 工具已部署於 crypto_* 前綴下)*

---

## 📋 總結：
目前本專案共註冊 **230 個** 具備明確語義的功能性工具。所有工具名稱皆遵循 MLOps 命名規範，且後端代碼已完成非同步化改造。
