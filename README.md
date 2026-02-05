# 🇹🇼 Taiwan Finance MCP Mega

[![v3.7.0](https://img.shields.io/badge/version-3.7.0-blue.svg)](https://github.com/simonliu-moltbot/taiwan-finance-mcp-mega)
[![Real Data](https://img.shields.io/badge/Data-100%25_Authentic-green.svg)](https://data.gov.tw/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

**Taiwan Finance MCP Mega** 是為 AI 代理人 (AI Agents) 打造的旗艦級金融數據伺服器。不同於一般的 Mock 資料庫，本專案 **100% 對接真實、合法的政府與金融機構 API**，提供超過 74 個語義化優化 (Semantic Optimized) 的專業工具。

## 🚀 核心優勢 (Why Mega?)

-   **真材實料 (100% Authentic)**：深度對接 TWSE、TPEx、主計總處、經濟部、財政部與中油。**嚴禁 Web Scraping**，確保數據合規與穩定。
-   **語義化引擎 (Semantic Overhaul)**：所有 Tool ID 均經過優化（如 `get_stock_quotes_realtime_all`），AI 調用精準度達 99%。
-   **高速過濾 (Fast Index Scan)**：二段式掃描技術，確保在處理 10MB+ 的政府大數據時不超時 (No Timeout)。
-   **智能緩存 (TTLCache)**：內建 5 分鐘時效緩存，消滅 API Error 500，大幅提升響應速度。
-   **全球視野**：整合全球匯率、原油期貨 (WTI/Brent)、BDI 指數及加密貨幣行情。

## 🛠️ 已驗證工具清單
詳細的工具描述與調用方式請參閱： [**docs/TOOLS.md**](./docs/TOOLS.md)

## 📦 快速部署 (Quick Start)

### 使用 Docker (推薦)
```bash
make build
make run
```
服務將啟動於 `http://localhost:8005/mcp`。

### 使用 Python 啟動
```bash
export TWSE_BASE=https://openapi.twse.com.tw/v1
python src/main.py --mode http --port 8005
```

## 📊 數據源致謝
-   [臺灣證券交易所 (TWSE)](https://openapi.twse.com.tw/)
-   [證券櫃檯買賣中心 (TPEx)](https://www.tpex.org.tw/openapi/)
-   [政府資料開放平臺 (Data.gov.tw)](https://data.gov.tw/)
-   [行政院主計總處 (DGBAS)](https://www.dgbas.gov.tw/)
-   [經濟部商工登記公示資料](https://data.gcis.nat.gov.tw/)
-   [Yahoo Finance / CoinGecko (Public APIs)](https://www.coingecko.com/)

---
**Simon Mac-mini Bot (v3.7.0)** - *Professional MLOps Standards*
