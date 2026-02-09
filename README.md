# 🇹🇼 Taiwan Finance MCP Mega

[![v4.6.0](https://img.shields.io/badge/version-4.6.0-blue.svg)](https://github.com/simonliu-moltbot/taiwan-finance-mcp-mega)
[![Real Data](https://img.shields.io/badge/Data-100%25_Authentic-green.svg)](https://data.gov.tw/)
[![Anti-Scraping](https://img.shields.io/badge/Anti--Scraping-Compliance-orange.svg)](https://data.gov.tw/)

**Taiwan Finance MCP Mega** 是為 AI 代理人 (AI Agents) 打造的旗艦級金融數據伺服器。本專案 **100% 對接真實、合法的政府與金融機構 API**，提供 58 個語義化優化 (Semantic Optimized) 的專業工具。

## 🚀 核心優勢 (Why Mega?)

-   **真材實料 (100% Authentic)**：深度對接 TWSE、TPEx、主計總處、經濟部、財政部與勞動部。**嚴禁 Web Scraping**，確保數據合規與穩定。
-   **語義化引擎 (Semantic Overhaul)**：所有 Tool ID 與描述均經過「高對比度」優化，明確區分上市/上櫃與大盤/個股，AI 調用精準度大幅提升。
-   **Anti-Cache 技術**：自動注入緩存控制標頭，確保法人買賣超、黃金與即時行情數據永遠對接官方最新狀態。
-   **分頁與截斷 (Stability)**：針對大流量 API 自動實作 20 筆截斷機制，徹底解決 500 Error 與超時問題。
-   **智能緩存 (TTLCache)**：內建 5 分鐘時效緩存，兼顧即時性與後端保護。

## 🛠️ 核心功能模組
-   **股市 (Stock)**：即時行情、三大法人買賣超 (上市/上櫃分流)、定期定額排行、營收報表、投資人關係概況。
-   **總體經濟 (Macro)**：GDP 成長率、CPI、失業率、國內外主要金融指標 (M1B/M2)、國際股價指數趨勢。
-   **匯率與大宗 (Forex & Commodity)**：即時匯率、WTI/Brent 原油、黃金現貨價格。
-   **銀行與金融 (Bank)**：債券/股票發行概況、國保基金經營統計。
-   **加密貨幣 (Crypto)**：BTC/ETH/SOL 即時報價與恐慌與貪婪指數。

## 📦 快速部署 (Quick Start)

### 使用 Python 啟動 (stdio 模式)
```bash
pip install -r requirements.txt
python src/taiwan_finance_mcp_mega/server.py --mode stdio
```

### 使用 Docker
```bash
make build
make run
```

## 📊 數據源與 API 詳細說明
詳細的資料來源連結、授權與 API 端點清單請參閱： [**docs/DATA_SOURCES.md**](./docs/DATA_SOURCES.md)

---
**Simon Mac-mini Bot (v4.6.0)** - *Professional MLOps Standards*
