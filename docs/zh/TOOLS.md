# 🛠️ Taiwan Finance MCP Mega - 已驗證工具清單 (v4.6.0)

本文件列出了目前**已完成實體邏輯對接 (100% 真實數據)** 並通過語義化與穩定性優化的工具。
所有工具均對接官方公開 API，嚴禁網頁爬蟲 (Anti-Scraping)。

---

## 📈 1. 台灣股市核心 (Taiwan Stocks - 24 工具)
*聚焦於證交所 (TWSE) 與櫃買中心 (TPEx) 數據。*

| 工具 ID | 說明 (方括號為模型辨識標籤) | 數據源 |
| :--- | :--- | :--- |
| `get_stock_quotes_realtime_all` | 上市個股當日即時行情 (開高低收/量) | TWSE |
| `get_stock_eps_ranking_summary` | 上市公司 每股盈餘 (EPS) 統計排名 | TWSE |
| `get_stock_dividend_yield_pe_pb` | 個股日本益比、殖利率、淨值比估值 | TWSE |
| `get_stock_institutional_summary_twse` | **[上市/大盤]** 三大法人買賣超合計 (合計金額) | TWSE |
| `get_stock_institutional_details_tpex` | **[上櫃/櫃買]** 三大法人買賣超明細 (個股進出) | TPEx |
| `get_stock_institutional_summary_tpex` | **[上櫃/櫃買]** 三大法人買賣超合計 (合計金額) | TPEx |
| `get_stock_margin_trading_balance` | 股票現貨融資融券餘額明細 | TWSE |
| `get_stock_odd_lot_trading_quotes` | 盤中零股交易即時行情 | TWSE |
| `get_stock_mops_significant_announcements` | 公開資訊觀測站 (MOPS) 重大訊息公告 | TWSE |
| `get_stock_price_limit_up_down_tracker` | 監控當日漲跌停股票清單 | TWSE |
| `get_stock_monthly_revenue_summary` | **[營收報表]** 上市公司每月營業收入彙總 | TWSE |
| `get_stock_etf_regular_savings_ranking` | **[排行/人氣]** ETF 定期定額交易戶數排行 | TWSE |
| `get_stock_block_trade_daily_summary` | 證券市場鉅額交易成交量值統計 | TWSE |
| `get_stock_after_hours_trading_info` | 股票盤後定價交易資訊 | TWSE |
| `get_stock_individual_average_price` | **[個股/均價]** 單一股票本月收盤均價趨勢 | TWSE |
| `get_stock_yield_averages_by_industry` | 上市公司各類股殖利率統計 | TWSE |
| `get_stock_pe_averages_by_industry` | 上市公司各類股本益比統計 (產業估值) | TWSE |
| `get_stock_broker_list_all` | 全台證券商基本聯絡清單 | TWSE |
| `get_stock_buyback_treasury_status` | 上市公司庫藏股買回進度 | TWSE |
| `get_stock_broker_regular_savings_data` | **[券商/業務]** 開辦定期定額業務之券商名單 | TWSE |
| `get_stock_listed_investor_profile` | **[上市/投資]** 發言人、網址、上市日等深度概況 | TWSE |
| `get_stock_otc_investor_profile` | **[上櫃/投資]** 發言人、網址、上櫃日等深度概況 | TPEx |
| `get_stock_public_investor_profile` | **[公發/投資]** 興櫃及公開發行公司基本投資資料 | TWSE |
| `get_stock_daily_closing_quotes_all` | 每日收盤指數及各類股成交量值總覽 | TWSE |

---

## 📉 2. 衍生性商品 (Derivatives - 3 工具)
*專指期交所 (Taifex) 數據，包含限制 20 筆回傳以確保穩定性。*

| 工具 ID | 說明 | 數據源 |
| :--- | :--- | :--- |
| `get_futures_quotes_daily` | 獲取期貨每日結算價與收盤行情 (限 20 筆) | Taifex |
| `get_futures_institutional_investor_flow` | 三大法人期貨未平倉留倉部位彙總 | Taifex |
| `get_futures_open_interest_ranking` | 期貨市場大額交易人未平倉部位排名 (限 20 筆) | Taifex |

---

## 🌍 3. 匯率與大宗商品 (Forex & Commodity - 14 工具)
| 工具 ID | 說明 | 數據源 |
| :--- | :--- | :--- |
| `get_forex_[CUR]_twd_realtime` | 各國幣別 (如 USD, JPY) 對台幣即時匯率 | rter.info |
| `get_forex_any_to_any_conversion` | 任意兩幣別間之即時匯率換算 | rter.info |
| `get_commodity_oil_wti_price_usd` | WTI 原油即時報價 (美元/桶) | MOEA |
| `get_commodity_oil_brent_price_usd` | Brent 布蘭特原油即時報價 | MOEA |
| `get_commodity_gold_spot_price_twd` | 黃金現貨即時報價 (台幣) | TPEx |

---

## 🏛️ 4. 總體經濟與商工數據 (Macro & Corp - 13 工具)
| 工具 ID | 說明 | 數據源 |
| :--- | :--- | :--- |
| `get_macro_gdp_growth_rate_quarterly` | 台灣季度 GDP 經濟成長率 | DGBAS |
| `get_macro_monthly_financial_indicators` | 每月國內主要金融指標 (M1B/M2/外匯存底) | CBC |
| `get_macro_economic_indicators_monthly` | 每月國內主要經濟指標 (CPI/失業率/薪資) | DGBAS |
| `get_macro_economic_indicators_annual` | 年度國內主要經濟指標 (長期趨勢分析) | DGBAS |
| `get_macro_global_stock_indices` | **[大盤指數]** 每月國際主要股價指數 (台/美/日/歐) | MOL |
| `get_macro_forex_rates_monthly` | **[歷史趨勢]** 國際主要國家貨幣每月匯率趨勢 | MOL |
| `get_macro_global_stock_indices_annual` | **[大盤指數]** 年度國際主要股價指數趨勢 | MOL |
| `get_macro_forex_rates_annual` | **[歷史趨勢]** 國際主要國家貨幣年度匯率歷史 | MOL |
| `get_corp_moea_business_registration` | 經濟部商工登記公示資料 (適用全台公司) | MOEA |

---

## 🏦 5. 銀行與金融發行 (Bank - 3 工具)
| 工具 ID | 說明 | 數據源 |
| :--- | :--- | :--- |
| `get_bank_bond_issuance_monthly` | 國內債券每月發行概況 (公債/公司債) | MOL |
| `get_bank_stock_issuance_monthly` | 國內公開發行公司股票每月發行與增資概況 | MOL |
| `get_bank_pension_fund_stats_monthly` | 國民年金保險基金每月經營規模與收益率 | MOL |

---

## 🪙 6. 加密貨幣 (Crypto - 4 工具)
| 工具 ID | 說明 | 數據源 |
| :--- | :--- | :--- |
| `get_crypto_btc_twd_price` | 比特幣 Bitcoin 即時報價與 24h 漲跌 | CoinGecko |
| `get_crypto_eth_twd_price` | 以太幣 Ethereum 即時報價與 24h 漲跌 | CoinGecko |
| `get_crypto_sol_twd_price` | Solana 即時報價與市場表現 | CoinGecko |
| `get_crypto_market_fear_greed_index` | 全球加密幣市場恐慌與貪婪指數 | Alt.me |

---

## 🕒 7. 系統通用 (Common - 1 工具)
| 工具 ID | 說明 |
| :--- | :--- |
| `get_current_time_taipei` | 獲取台北即時系統時間、日期與星期幾。 |

---
*最後更新日期：2026-02-09*
*版本：v4.6.0 Semantic Optimized*
