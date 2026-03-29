def calculate_insurance(profile):
    print("\n=== Insurance Analysis ===")

    income = profile["income"]
    expenses = profile["expenses"]
    financial_health = profile["financial_health"]

    #  Annual income
    annual_income = (income["active_income"] + income["passive_income"]) * 12

    #  Annual expenses (needs + obligations)
    annual_expense = (expenses["needs"] + expenses["obligations"]) * 12

    #  Life Insurance Rule (10–15x income)
    life_insurance_needed = annual_income * 12

    #  Health Insurance basic suggestion
    health_insurance_needed = annual_expense * 2

    #  Insights
    suggestions = []

    if financial_health["insurance"] == "none":
        suggestions.append("⚠️ No insurance detected — high financial risk")

    if financial_health["insurance"] != "none":
        suggestions.append("✅ You have some insurance coverage")

    if life_insurance_needed > 0:
        suggestions.append("💡 Consider term insurance for protection")

    return {
        "life_insurance_needed": life_insurance_needed,
        "health_insurance_needed": health_insurance_needed,
        "suggestions": suggestions
    }