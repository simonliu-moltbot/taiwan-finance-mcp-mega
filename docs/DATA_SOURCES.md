# Data Sources Registry

This document lists the official data sources and APIs used by the `taiwan-finance-mcp-mega` project to ensure transparency and facilitate monitoring of data integrity.

## 1. Primary Exchanges & Regulatory Bodies

| Source | Endpoint | Data Provided |
|--------|----------|---------------|
| **TWSE (臺灣證券交易所)** | `https://openapi.twse.com.tw/v1` | Stock quotes, EPS, monthly revenue, dividend yield, institutional investors, ESG metrics. |
| **TPEx (證券櫃檯買賣中心)** | `https://openapi.tpex.org.tw/v1` | OTC stock quotes and company profiles. |
| **Taifex (臺灣期貨交易所)** | `https://openapi.taifex.com.tw/v1` | Futures and options quotes, institutional flow, large trader positions. |
| **MOF (財政部)** | `https://quality.data.gov.tw/` | National debt clock and fiscal statistics. |
| **CBC (中央銀行)** | `https://www.cbc.gov.tw/` | Monetary policy announcements and official rates. |
| **FSC (金管會)** | `https://quality.data.gov.tw/dq_download_json.php?nid=7334` | Financial news and regulatory updates. |

## 2. Economic Indicators & Government Data

| Category | Source | API / Link |
|----------|--------|------------|
| **Macro Indicators** | MOL (勞動部) | `https://apiservice.mol.gov.tw/OdService/download/A17000000J-030243-YTl` |
| **Housing Index** | MOI (內政部) | `https://quality.data.gov.tw/dq_download_json.php?nid=11545` |
| **Electricity Stats** | MOEA (經濟部能源署) | `https://www.moeaea.gov.tw/ECW/populace/opendata/wHandOpenData_File.ashx?set_id=236` |
| **Fuel Prices** | CPC (台灣中油) | `https://vipmbr.cpc.com.tw/openData/MainProdListPrice` |
| **Economic News** | MOEA (經濟部) | `https://www.moea.gov.tw/Mns/populace/news/` |

## 3. Global Finance & Crypto

| Category | Provider | API / Link |
|----------|----------|------------|
| **Forex Rates** | ExchangeRate-API | `https://open.er-api.com/v6/latest/` |
| **Cryptocurrency** | CoinGecko | `https://api.coingecko.com/api/v3` |

## 4. Corporate & Banking

| Data Type | Source | API / Link |
|-----------|--------|------------|
| **Company Registry** | GCIS (經濟部商業發展署) | `https://data.gcis.nat.gov.tw/od/data/api/` |
| **Bank Profit/Loss** | Gov Data Platform | `https://quality.data.gov.tw/dq_download_json.php?nid=28567` |

---
*Last Updated: 2026-02-09*
