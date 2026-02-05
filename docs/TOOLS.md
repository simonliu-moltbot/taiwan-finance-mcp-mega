# 🏦 Taiwan Finance MCP Mega - 工具完整手冊 (v2.8.0)

本手冊列出了所有具備 **真實 API 對接** 的金融工具。我們已全面優化數據抓取邏輯，確保回傳欄位具備高可讀性。

---

## 📈 1. 台股市場深度分析 (STOCK)
對接來源：台灣證券交易所 (TWSE) 與 櫃買中心 (TPEx)。

| 工具 ID | 功能描述 | 輸入 (Input) | 輸出範例 (Output) |
| :--- | :--- | :--- | :--- |
| `stock_realtime_quotes` | **[核心]** 個股當日行情 | `symbol` (代號) | `{id, name, price, change, volume...}` |
| `stock_fundamental_eps` | 公司季度 EPS 排名 | `limit` (筆數) | `[{公司名稱, 營業收入, EPS...}]` |
| `stock_chip_institutional_flow` | 三大法人買賣超彙總 | 無 | `[{法人別, 買進金額, 賣超金額...}]` |
| `stock_dividend_yield` | 特定個股現金殖利率 | `symbol` (代號) | `[{除息日, 現金股利, 殖利率...}]` |

---

## 💹 2. 全球匯率與大宗商品 (FOREX)
對接來源：即時市場匯率 API (ExchangeRate-API)。

| 工具 ID | 功能描述 | 輸入 (Input) | 輸出範例 (Output) |
| :--- | :--- | :--- | :--- |
| `forex_usd_twd` | 美金對台幣即時匯率 | 無 | `{"pair": "USD/TWD", "rate": 31.57...}` |
| `forex_jpy_twd` | 日幣對台幣即時匯率 | 無 | `{"pair": "JPY/TWD", "rate": 0.215...}` |
| `forex_rate` | 自訂幣別匯率換算 | `base` (原始幣別) | `{"rate": 數值, "info": 說明}` |

---

## ₿ 3. 加密貨幣監控 (CRYPTO)
對接來源：CoinGecko Public API。

| 工具 ID | 功能描述 | 輸入 (Input) | 輸出範例 (Output) |
| :--- | :--- | :--- | :--- |
| `crypto_price` | 比特幣等幣種即時價 | `coin_id` (幣種 ID) | `{"bitcoin": {"twd": 2400501...}}` |
| `crypto_trending` | 當前全球熱搜幣種 | 無 | `{"coins": [...], "nfts": [...]}` |

---

## 🛡️ 數據品質保證
*   **欄位映射**：原始 API 的複雜代稱（如 `c`, `z`, `y`）已全部映射為人類直觀理解的 `id`, `price`, `yesterday_close`。
*   **非同步抓取**：全面採用 `httpx` 異步連線，確保在高併發查詢下不卡頓。
*   **合法來源**：數據 100% 來自政府及知名機構之公開 API。
