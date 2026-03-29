def generate_recommendations(portfolio):
    """
    Rule-based recommendation engine
    Returns list of recommendations
    """

    allocation = portfolio.allocation
    risk = portfolio.risk_category
    diversification = portfolio.diversification

    recommendations = []

    # RISK BASED
    if "High" in risk:
        recommendations.append({
            "type": "risk",
            "message": "Reduce equity exposure to lower risk"
        })

    # ALLOCATION RULES
    if allocation.get("Equity", 0) > 70:
        recommendations.append({
            "type": "allocation",
            "message": "Equity allocation is too high (>70%)"
        })

    if allocation.get("Debt", 0) < 20:
        recommendations.append({
            "type": "allocation",
            "message": "Increase debt allocation for stability"
        })

    if allocation.get("Cash", 0) > 25:
        recommendations.append({
            "type": "liquidity",
            "message": "High idle cash — consider investing"
        })

    if allocation.get("Crypto", 0) > 10:
        recommendations.append({
            "type": "risk",
            "message": "High crypto exposure — risky asset"
        })

    # DIVERSIFICATION
    if "Poor" in diversification:
        recommendations.append({
            "type": "diversification",
            "message": "Portfolio is poorly diversified"
        })

    return recommendations