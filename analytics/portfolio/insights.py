def generate_insights(allocation, total, risk_category, diversification):
    insights = []

    # EQUITY ANALYSIS
    equity = allocation.get("Equity", 0)

    if equity > 80:
        insights.append(" Very high equity exposure — high volatility risk")
    elif equity < 40:
        insights.append(" Low equity exposure — may limit long-term growth")

    #DEBT ANALYSIS
    debt = allocation.get("Debt", 0)

    if debt < 20:
        insights.append(" Low debt allocation — insufficient stability")
    elif debt > 60:
        insights.append(" High debt allocation — returns may be lower")

    #CRYPTO ANALYSIS
    crypto = allocation.get("Crypto", 0)

    if crypto > 10:
        crypto_amount = (crypto / 100) * total
        insights.append(
            f" High crypto exposure (₹{int(crypto_amount)}) — highly volatile asset"
        )

    #CASH ANALYSIS
    cash = allocation.get("Cash", 0)

    if cash > 30:
        cash_amount = (cash / 100) * total

        if cash > 50:
            insights.append(
                f" ₹{int(cash_amount)} idle cash — major underutilization of funds"
            )
        else:
            insights.append(
                f" ₹{int(cash_amount)} idle cash — consider investing in SIP or debt funds"
            )


    #REAL ESTATE ANALYSIS
    real_estate = allocation.get("RealEstate", 0)

    if real_estate > 50:
        insights.append(" High real estate exposure — low liquidity")

    #GOLD ANALYSIS
    gold = allocation.get("Gold", 0)

    if gold > 20:
        insights.append(" High gold allocation — useful for hedging but limited growth")


    #PORTFOLIO STRUCTURE SUMMARY
    insights.append(f" Risk Level: {risk_category}")
    insights.append(f" Diversification: {diversification}")

    #  OVERALL SUGGESTION
    if risk_category == "High Risk" and debt < 20:
        insights.append(" Consider increasing debt allocation to balance risk")

    if risk_category == "Low Risk" and equity < 40:
        insights.append(" Consider increasing equity for better long-term returns")

    return insights