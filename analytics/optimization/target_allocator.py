def get_target_allocation(risk_category):
    if risk_category == "High Risk":
        return {"Equity": 70, "Debt": 20, "Gold": 10}
    elif risk_category == "Moderate Risk":
        return {"Equity": 50, "Debt": 40, "Gold": 10}
    else:
        return {"Equity": 30, "Debt": 60, "Gold": 10}