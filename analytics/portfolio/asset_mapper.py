
def map_assets(investments):
    return {
        "Equity": investments.get("stocks", 0) + investments.get("mutual_funds", 0),
        "Debt": investments.get("fd", 0) + investments.get("bonds", 0),
        "Gold": investments.get("gold", 0),
        "Crypto": investments.get("crypto", 0),
        "Cash": investments.get("cash", investments.get("savings", 0)),  # 🔥 SAFE
        "RealEstate": investments.get("real_estate", 0)
    }