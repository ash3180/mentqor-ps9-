def get_basic_info():
    print("\n--- Basic Information ---")
    return {
        "name": input("Enter Name: "),
        "age": int(input("Enter Age: ")),
        "sector": input("Enter Sector (Govt/Corporate/Business/etc): ")
    }


def get_income():
    print("\n--- Income ---")
    return {
        "active_income": float(input("Active Income: ")),
        "passive_income": float(input("Passive Income: "))
    }


def get_expenses():
    print("\n--- Expenditure ---")
    return {
        "needs": float(input("Needs (rent, food, etc): ")),
        "obligations": float(input("Financial Obligations (EMI, etc): ")),
        # "investments": float(input("Current Investments: ")),
        "lifestyle": float(input("Lifestyle Expenses: ")),
        "luxury": float(input("Luxury Expenses: "))
    }


def get_goals():
    print("\n--- Goals ---")
    return {
        "short_term": input("Short-term goals: "),
        "medium_term": input("Medium-term goals: "),
        "long_term": input("Long-term goals: "),
        "retirement": input("Retirement goal (age): ")
    }


def get_investments():
    print("\n--- Investments ---")
    return {
        "savings": float(input("Savings (cash/liquid): ")),
        "stocks": float(input("Stocks: ")),
        "mutual_funds": float(input("Mutual Funds: ")),
        "crypto": float(input("Crypto: ")),
        "fd": float(input("FDs: ")),
        "bonds": float(input("Government Bonds: ")),
        "gold": float(input("Gold: ")),
        "real_estate": float(input("Real Estate: "))
    }


def get_financial_health():
    print("\n--- Financial Health ---")
    return {
        "emergency_fund": input("Emergency fund available? (yes/no): "),
        "insurance": input("Insurance (life/health/general/none): "),
        "debt_health": input("Debt level (low/medium/high): "),
        "tax_efficiency": input("Tax planning done? (yes/no): ")
    }


# Master Function 
def get_full_user_profile():
    profile = {}

    profile["basic_info"] = get_basic_info()
    profile["income"] = get_income()
    profile["expenses"] = get_expenses()
    profile["goals"] = get_goals()
    profile["investments"] = get_investments()
    profile["financial_health"] = get_financial_health()

    return profile