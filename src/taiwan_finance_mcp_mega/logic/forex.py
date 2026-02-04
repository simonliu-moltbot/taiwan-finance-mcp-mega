from ..config import Config
from ..utils.http_client import AsyncHttpClient

class ForexLogic:
    @staticmethod
    async def get_latest_rates():
        return await AsyncHttpClient.fetch_json(Config.FOREX_API)

    @classmethod
    async def get_pair(cls, base: str, target: str = "TWD"):
        data = await cls.get_latest_rates()
        if "error" in data: return data
        
        rates = data.get("rates", {})
        # Note: API base is JPY
        try:
            jpy_to_target = rates.get(target)
            jpy_to_base = rates.get(base)
            rate = jpy_to_target / jpy_to_base
            return {
                "pair": f"{base}/{target}",
                "rate": round(rate, 4),
                "source": "ExchangeRate-API"
            }
        except:
            return {"error": f"Currency pair {base}/{target} not supported"}
