def calculate_portfolio_risk(allocation):
    risk_score = 0

    # Risk weights
    weights = {
        "Equity": 0.8,
        "Crypto": 1.0,
        "RealEstate": 0.6,
        "Gold": 0.4,
        "Debt": 0.2,
        "Cash": 0.1
    }

    for asset, percent in allocation.items():
        risk_score += weights.get(asset, 0) * (percent / 100)

    if risk_score > 0.7:
        category = "High Risk"
    elif risk_score > 0.4:
        category = "Moderate Risk"
    else:
        category = "Low Risk"

    return round(risk_score, 2), category