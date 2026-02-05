import pytest
import asyncio
from typing import Dict, Any
from taiwan_finance_mcp_mega.logic.stock import StockLogic
from taiwan_finance_mcp_mega.logic.forex import ForexLogic
from taiwan_finance_mcp_mega.logic.global_macro import GlobalMacroLogic, CryptoLogic
from taiwan_finance_mcp_mega.logic.gov_data import EconomicsLogic, PublicServiceLogic
from taiwan_finance_mcp_mega.server import dispatch_mega_logic

@pytest.mark.asyncio
class TestFinanceMegaLogic:
    """
    [v3.8.0] Finance MCP Mega 核心邏輯自動化測試集。
    旨在驗證真實 API 對接狀況、數據格式與路由正確性。
    """

    # --- 1. 測試台股行情與過濾引擎 ---
    async def test_stock_realtime_quotes(self):
        # 測試台積電 (2330)
        res = await StockLogic.get_realtime_quotes("2330")
        assert isinstance(res, list)
        if res: # 交易日才有資料
            assert any("台積電" in str(v) or "2330" in str(v) for v in res[0].values())

    async def test_stock_etf_ranking(self):
        # 測試 0050 排行 (驗證特殊 Key 匹配)
        res = await StockLogic.call_generic_api("/ETFReport/ETFRank", "0050")
        assert isinstance(res, list)
        if res:
            assert any(str(v) == "0050" for v in res[0].values())

    # --- 2. 測試匯率與大宗商品 ---
    async def test_forex_jpy_twd(self):
        res = await ForexLogic.get_pair("JPY", "TWD")
        assert "rate" in res
        assert res["pair"] == "JPY/TWD"
        assert res["rate"] > 0

    async def test_commodity_oil_wti(self):
        res = await GlobalMacroLogic.get_commodity_price("WTI")
        assert "value" in res
        assert "Yahoo Finance" in res["source"]

    # --- 3. 測試宏觀經濟 (關鍵字匹配) ---
    async def test_macro_gdp_fuzzy_match(self):
        res = await EconomicsLogic.get_macro_stats("gdp")
        assert "indicator" in res
        if "value" in res:
            assert res["value"] != "N/A"

    # --- 4. 測試系統通用工具 ---
    async def test_system_time(self):
        res = await PublicServiceLogic.get_current_time()
        assert res["timezone"] == "Asia/Taipei"
        assert ":" in res["current_time"]

    # --- 5. 測試 Dispatcher (路徑映射驗證) ---
    @pytest.mark.parametrize("tool_name, symbol", [
        ("get_stock_quotes_realtime_all", "2330"),
        ("get_forex_usd_twd_realtime", None),
        ("get_crypto_btc_twd_price", None),
        ("get_macro_fuel_price_cpc_retail", None),
        ("get_corp_moea_business_registration", "台積電")
    ])
    async def test_dispatcher_routing(self, tool_name, symbol):
        """驗證語義化 ID 是否能正確觸發邏輯並回傳非錯誤結果"""
        res = await dispatch_mega_logic(tool_name, symbol, limit=1)
        # 這裡不斷言內容，只斷言不報錯且路徑通暢
        assert "error" not in res if isinstance(res, dict) else True
        assert res is not None

if __name__ == "__main__":
    pytest.main([__file__])
