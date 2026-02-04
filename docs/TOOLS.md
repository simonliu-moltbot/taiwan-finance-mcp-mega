# 🏦 Taiwan Finance MCP Mega - 工具完整手冊 (v2.5.0)

本文件詳列了 **Taiwan Finance MCP Mega** 所提供的所有 220+ 個金融工具及其詳細資訊。所有數據均來自政府官方與合法公開 API。

## 📂 工具類別概覽

| 類別 | 工具數量 | 數據來源 |
| :--- | :--- | :--- |
| **台股市場深度分析** | 50+ | 台灣證券交易所 (TWSE), 櫃買中心 (TPEx) |
| **全球匯率與跨境支付** | 30+ | 中華民國中央銀行 (CBC), ExchangeRate-API |
| **銀行、信貸與稅務** | 30+ | 金管會, 財政部 (MOF) |
| **企業與產業數據** | 30+ | 經濟部 (MOEA), 公開資訊觀測站 (MOPS) |
| **宏觀經濟與預算** | 30+ | 行政院主計總處 (DGBAS), 審計部 |
| **不動產與物流** | 30+ | 內政部 (MOI), 交通部 (MOTC) |
| **Web3 與加密貨幣** | 20+ | CoinGecko, Blockchain Nodes |

---

## 🛠 詳細工具清單 (精選範例)

### 📈 台股工具 (`stock_tool_*`)
*   **stock_day_all**: 獲取全市場即時行情。
    *   **Input**: `limit` (int, 筆數)
    *   **Output**: JSON 數組，包含代號、名稱、開盤、最高、最低、收盤、成交量。
*   **stock_fin_eps**: 查詢公司 EPS 獲利排名。
    *   **Input**: `symbol` (str, 代號)
    *   **Output**: 獲利數據與 YOY 成長。

### 💹 匯率工具 (`forex_tool_*`)
*   **forex_rate**: 查詢台幣即時匯率。
    *   **Input**: `base` (str, 原始幣別，如 USD)
    *   **Output**: 兌換台幣之匯率數值。

### 🏛️ 企業工具 (`corp_tool_*`)
*   **corp_reg_info**: 查詢公司登記資料。
    *   **Input**: `company_id` (str, 統一編號)
    *   **Output**: 負責人、資本額、登記地址、營業項目。

*(更多 200+ 項工具請參閱原始碼與 API 定義)*

---

## 🛡️ 數據合規性
所有工具僅串接公開資料 (Open Data)，無須特殊授權即可進行學術或一般查詢用途。
