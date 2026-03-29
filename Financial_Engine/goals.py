from Financial_Engine.sip import calculate_sip


def calculate_goal(xirr):
    print("\n=== Goal Planning ===")

    #  Goal Info
    goal_name = input("Enter Goal Name (House, Education, etc): ")
    current_cost = float(input("Enter Current Cost of Goal (₹): "))
    years = int(input("Enter Time to Achieve Goal (years): "))

    #  Inflation
    inflation = float(input("Enter Inflation Rate (default 6%): ") or 6) / 100

    #  Return Handling
    has_return = input("Do you know expected return? (yes/no): ").lower()

    if has_return == "yes":
        expected_return = float(input("Enter Expected Return (%): ")) / 100
    else:
        use_xirr = input("Use your portfolio return (XIRR)? (yes/no): ").lower()

        if use_xirr == "yes":
            expected_return = xirr
        else:
            expected_return = 0  # conservative fallback

    #  Inflate goal cost
    inflated_cost = current_cost * (1 + inflation) ** years

    #  Real return
    real_return = ((1 + expected_return) / (1 + inflation)) - 1

    #  Existing investment
    has_existing = input("Any existing investment for this goal? (yes/no): ").lower()

    if has_existing == "yes":
        current_investment = float(input("Enter current invested amount (₹): "))
    else:
        current_investment = 0

    #  Future value of current investment
    future_value_existing = current_investment * (1 + expected_return) ** years

    #  Final corpus required
    corpus_required = inflated_cost - future_value_existing

    if corpus_required < 0:
        corpus_required = 0

    #  SIP Calculation (handles zero return safely)
    sip = calculate_sip(corpus_required, real_return, years)

    #  Return structured output
    return {
        "goal_name": goal_name,
        "inflated_cost": inflated_cost,
        "real_return": real_return,
        "corpus_required": corpus_required,
        "sip": sip
    }