def calculate_tax(profile):
    print("\n=== Tax Analysis ===")

    income = profile["income"]
    investments = profile["investments"]
    financial_health = profile["financial_health"]

    #  Total Income
    total_income = income["active_income"] + income["passive_income"]

    #  Basic deduction assumption (simplified)
    deduction = min(sum(investments.values()), 150000)  # 80C limit approx

    taxable_income = total_income - deduction

    #  Simple tax slab (very simplified)
    if taxable_income <= 250000:
        tax = 0
    elif taxable_income <= 500000:
        tax = (taxable_income - 250000) * 0.05
    elif taxable_income <= 1000000:
        tax = 12500 + (taxable_income - 500000) * 0.20
    else:
        tax = 112500 + (taxable_income - 1000000) * 0.30

    #  Insights
    suggestions = []

    if financial_health["tax_efficiency"] == "no":
        suggestions.append("⚠️ You are not using tax-saving strategies")

    if deduction < 150000:
        suggestions.append("💡 You can invest more under 80C to save tax")

    return {
        "total_income": total_income,
        "taxable_income": taxable_income,
        "tax": tax,
        "suggestions": suggestions
    }