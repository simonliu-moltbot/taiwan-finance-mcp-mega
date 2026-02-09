# 直連 API 介面註冊表 (已驗證與穩定)

本文件提供了 `taiwan-finance-mcp-mega` 專案中每個活躍工具的詳盡對應關係。所有不穩定或僅為「首頁」的連結均已移除。

---

## 📈 股票市場 (證交所 TWSE / 櫃買中心 TPEx)
*狀態：透過官方 OpenAPI v1 與 RWD JSON 介面全面運作。*

| 工具名稱 | 直連 API URL (來源) | 說明 (Description) |
|-----------|-------------------------|-------------------|
| `get_stock_quotes_realtime_all` | [TWSE OpenAPI](https://openapi.twse.com.tw/v1/exchangeReport/STOCK_DAY_ALL) | 上市個股當日即時行情 |
| `get_stock_eps_ranking_summary` | [TWSE OpenAPI](https://openapi.twse.com.tw/v1/opendata/t187ap14_L) | 各產業 EPS 統計資訊 |
| `get_stock_dividend_yield_pe_pb` | [TWSE OpenAPI](https://openapi.twse.com.tw/v1/exchangeReport/BWIBBU_d) | 個股日本益比、殖利率及淨值比 |
| `get_stock_institutional_summary_twse` | [TWSE RWD API](https://www.twse.com.tw/rwd/zh/fund/BFI82U?response=json) | [上市/大盤] 三大法人買賣超彙總統計 (合計) |
| `get_stock_institutional_details_tpex` | [TPEx OpenAPI](https://www.tpex.org.tw/openapi/v1/tpex_3insti_daily_trading) | [上櫃/櫃買] 三大法人買賣超明細 (個股) |
| `get_stock_institutional_summary_tpex` | [TPEx OpenAPI](https://www.tpex.org.tw/openapi/v1/tpex_3insti_summary) | [上櫃/櫃買] 三大法人買賣超彙總統計 (合計) |
| `get_stock_margin_trading_balance` | [TWSE OpenAPI](https://openapi.twse.com.tw/v1/exchangeReport/MI_MARGN) | 融資融券餘額明細 |
| `get_stock_odd_lot_trading_quotes` | [TWSE OpenAPI](https://openapi.twse.com.tw/v1/exchangeReport/TWT53U) | 盤中零股交易即時行情 |
| `get_stock_mops_significant_announcements` | [TWSE OpenAPI](https://openapi.twse.com.tw/v1/opendata/t187ap04_L) | 每日重大訊息公告 (MOPS) |
| `get_stock_price_limit_up_down_tracker` | [TWSE OpenAPI](https://openapi.twse.com.tw/v1/exchangeReport/TWT84U) | 股價升降幅度/漲跌停預告 |
| `get_stock_monthly_revenue_summary` | [TWSE OpenAPI](https://openapi.twse.com.tw/v1/opendata/t187ap05_L) | 每月營業收入彙總表 |
| `get_stock_etf_regular_savings_ranking` | [TWSE OpenAPI](https://openapi.twse.com.tw/v1/ETFReport/ETFRank) | ETF 定期定額交易戶數排行 |
| `get_stock_block_trade_daily_summary` | [TWSE OpenAPI](https://openapi.twse.com.tw/v1/block/BFIAUU_d) | 鉅額交易日成交量值統計 |
| `get_stock_after_hours_trading_info` | [TWSE OpenAPI](https://openapi.twse.com.tw/v1/exchangeReport/BFT41U) | 盤後定價交易資訊 |
| `get_stock_individual_average_price` | [TWSE OpenAPI](https://openapi.twse.com.tw/v1/exchangeReport/STOCK_DAY_AVG_ALL) | 上市公司收盤價及月平均價 |
| `get_stock_listed_investor_profile` | [TWSE OpenAPI](https://openapi.twse.com.tw/v1/opendata/t187ap03_L) | 上市公司投資人概況 (發言人/網址/上市日) |
| `get_stock_otc_investor_profile` | [TPEx OpenAPI](https://www.tpex.org.tw/openapi/v1/t187ap03_O) | 上櫃公司投資人概況 (發言人/網址/上櫃日) |
| `get_stock_public_investor_profile` | [TWSE OpenAPI](https://openapi.twse.com.tw/v1/opendata/t187ap03_P) | 興櫃/公發公司基本投資資料 |
| `get_stock_daily_closing_quotes_all` | [TWSE OpenAPI](https://openapi.twse.com.tw/v1/exchangeReport/MI_INDEX) | 收盤指數及各類股成交量值 |
| `get_stock_yield_averages_by_industry` | [TWSE OpenAPI](https://openapi.twse.com.tw/v1/exchangeReport/FMSRFK_ALL) | 上市公司各類股殖利率統計 |
| `get_stock_pe_averages_by_industry` | [TWSE OpenAPI](https://openapi.twse.com.tw/v1/exchangeReport/FMNPTK_ALL) | 上市公司各類股本益比統計 |
| `get_stock_broker_list_all` | [TWSE OpenAPI](https://openapi.twse.com.tw/v1/brokerService/brokerList) | 證券商基本資料一覽表 |
| `get_stock_buyback_treasury_status` | [TWSE OpenAPI](https://openapi.twse.com.tw/v1/opendata/t187ap13_L) | 庫藏股買回進度彙整 |
| `get_stock_broker_regular_savings_data` | [TWSE OpenAPI](https://openapi.twse.com.tw/v1/brokerService/secRegData) | 開辦定期定額業務證券商名單 |

## 📉 衍生性商品 (期交所 Taifex)
*狀態：已驗證真實在線路徑。*

| 工具名稱 | 直連 API URL (來源) | 說明 (Description) |
|-----------|-------------------------|-------------------|
| `get_futures_quotes_daily` | [Taifex OpenAPI](https://openapi.taifex.com.tw/v1/DailyMarketReportFut) | 期貨每日收盤行情 |
| `get_futures_institutional_investor_flow` | [Taifex OpenAPI](https://openapi.taifex.com.tw/v1/MarketDataOfMajorInstitutionalTradersGeneralBytheDate) | 三大法人期貨交易量與未平倉彙總 |
| `get_futures_open_interest_ranking` | [Taifex OpenAPI](https://openapi.taifex.com.tw/v1/OpenInterestOfLargeTradersFutures) | 期貨大額交易人未平倉部位統計 |

## 🌍 匯率與大宗商品
*狀態：使用 tw.rter.info 交叉匯率引擎與政府公開資料。*

| 工具名稱 | 直連 API URL (來源) | 說明 (Description) |
|-----------|-------------------------|-------------------|
| `get_forex_[CUR]_twd_realtime` | [tw.rter.info API](https://tw.rter.info/capi.php) | 各國幣別對台幣即時匯率 |
| `get_forex_any_to_any_conversion` | [tw.rter.info API](https://tw.rter.info/capi.php) | 任意幣別對任意幣別即時換算 |
| `get_commodity_oil_wti_price_usd` | [MOEA CSV](https://www2.moeaea.gov.tw/oil111/csv/GlobalOilOpenData.csv) | 全球原油價格 (WTI/Brent) |
| `get_commodity_gold_spot_price_twd` | [TPEx OpenAPI](https://www.tpex.org.tw/openapi/v1/tpex_gold_latest) | 黃金現貨即時報價(TWD) |

## 🏛️ 宏觀經濟與商工數據
*Status: 穩定政府 API 端點。*

| 工具名稱 | 直連 API URL (來源) | 說明 (Description) |
|-----------|-------------------------|-------------------|
| `get_macro_gdp_growth_rate_quarterly` | [MOL REST API](https://apiservice.mol.gov.tw/OdService/rest/datastore/A17030000J-000016-1ci) | 台灣季度 GDP 經濟成長率 |
| `get_macro_monthly_financial_indicators` | [MOL REST API](https://apiservice.mol.gov.tw/OdService/rest/datastore/A17030000J-000037-l9P) | 每月國內主要金融指標 (M1B/M2/外匯存底) |
| `get_macro_economic_indicators_monthly` | [MOL REST API](https://apiservice.mol.gov.tw/OdService/rest/datastore/A17030000J-000016-1ci) | 每月國內主要經濟指標 (GDP/CPI/失業率) |
| `get_macro_economic_indicators_annual` | [MOL REST API](https://apiservice.mol.gov.tw/OdService/rest/datastore/A17000000J-030243-XXL) | 年度國內主要經濟指標 (長期趨勢) |
| `get_macro_global_stock_indices` | [MOL REST API](https://apiservice.mol.gov.tw/OdService/rest/datastore/A17030000J-000050-Ipz) | 每月國際主要股價指數 (台/美/日/歐) |
| `get_macro_forex_rates_monthly` | [MOL REST API](https://apiservice.mol.gov.tw/OdService/rest/datastore/A17030000J-000049-Iq0) | 國際主要國家貨幣每月匯率概況 |
| `get_macro_global_stock_indices_annual` | [MOL REST API](https://apiservice.mol.gov.tw/OdService/rest/datastore/A17000000J-030245-4Ml) | 年度國際主要股價指數 |
| `get_macro_forex_rates_annual` | [MOL REST API](https://apiservice.mol.gov.tw/OdService/rest/datastore/A17000000J-030185-CKf) | 國際主要國家貨幣年度匯率概況 |
| `get_bank_bond_issuance_monthly` | [MOL REST API](https://apiservice.mol.gov.tw/OdService/rest/datastore/A17030000J-000048-YHK) | 國內債券每月發行概況 |
| `get_bank_stock_issuance_monthly` | [MOL REST API](https://apiservice.mol.gov.tw/OdService/rest/datastore/A17030000J-000047-Y4N) | 國內公開發行公司股票每月發行概況 |
| `get_bank_pension_fund_stats_monthly` | [MOL REST API](https://apiservice.mol.gov.tw/OdService/rest/datastore/A17030000J-000045-2qm) | 國民年金保險基金每月經營概況 |
| `get_corp_moea_business_registration` | [GCIS NAT API](https://data.gcis.nat.gov.tw/od/data/api/) | 經濟部商工登記公示資料 |

## 🪙 加密貨幣與系統

| 工具名稱 | 直連 API URL (來源) | 說明 (Description) |
|-----------|-------------------------|-------------------|
| `get_crypto_btc_twd_price` | [CoinGecko](https://www.coingecko.com/en/coins/bitcoin) | 比特幣即時 TWD/USD 報價 |
| `get_crypto_eth_twd_price` | [CoinGecko](https://www.coingecko.com/en/coins/ethereum) | 以太幣即時 TWD/USD 報價 |
| `get_crypto_sol_twd_price` | [CoinGecko](https://www.coingecko.com/en/coins/solana) | Solana 即時報價與市場表現 |
| `get_crypto_market_fear_greed_index` | [Alternative.me](https://alternative.me/crypto/fear-and-greed-index/) | 全球加密幣市場恐慌與貪婪指數 |
| `get_current_time_taipei` | 本端環境 | 獲取台北即時系統時間 |

---
*活躍已驗證工具總數：58*
*最後更新日期：2026-02-09*
