# 🏦 Taiwan Finance MCP Mega - 工具完整手冊 (v3.1.0)

本手冊列出了 **v3.1.0** 版本中所有具備 **真實數據對接與符號過濾功能** 的核心工具。

## 📈 1. 台股核心工具 (STOCK)
| 工具 ID | 功能描述 | 輸入 (Input) | 輸出 (Output) |
| :--- | :--- | :--- | :--- |
| `stock_realtime_quotes` | **[修復]** 獲取個股即時行情。支援 2330 等代號過濾。 | `symbol` (代號) | id, name, price, change, volume... |
| `stock_fundamental_eps` | **[修復]** 查詢每股盈餘 (EPS)。支援單一公司過濾。 | `symbol` (代號) | year, quarter, name, eps... |
| `stock_dividend_yield` | **[修復]** 查詢殖利率、本益比、淨值比。 | `symbol` (代號) | yield, pe, pb, name... |
| `stock_chip_institutional_flow` | **[修正]** 查詢全市場三大法人買賣超彙總。 | 無 | 法人別, 買進金額, 買賣超金額... |
| `stock_margin_balance_monitor` | **[修正]** 監控市場融資融券水位。 | `symbol` (選填) | 股票代號, 融資餘額, 融券餘額... |
| `stock_pe_ratio_ranking` | 全市場本益比排行分析。 | `limit` (筆數) | 排行榜清單 |

---

## 💹 2. 匯率與加密貨幣 (FOREX & CRYPTO)
| 工具 ID | 功能描述 | 輸入 (Input) | 輸出 (Output) |
| :--- | :--- | :--- | :--- |
| `forex_usd_twd` | 美金對台幣即時匯率 (真實對接)。 | 無 | pair, rate, source... |
| `crypto_price` | 加密貨幣即時價 (CoinGecko)。 | `coin_id` (幣種) | twd, usd, 24h_change... |

---

## 🛡️ v3.1.0 重大修復說明：
1. **正確標的導向**：所有查詢台積電 (2330) 的問題，現在都會正確觸發 `symbol='2330'` 的過濾邏輯，不再回傳其他不相干的公司（如創意電子）。
2. **解決 API 逾時**：優化了非同步請求機制，減少 API 回傳過大導致的連線中斷。
3. **欄位標準化**：回傳 JSON 鍵值已從 API 原始代碼（如 `z`, `y`）全面轉換為易讀英文（如 `price`, `yesterday_close`）。
