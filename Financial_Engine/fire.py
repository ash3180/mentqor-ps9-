from Financial_Engine.sip import calculate_sip


def calculate_fire(profile, xirr):
    print("\n=== FIRE Engine ===")

    #  Extract data
    age = profile["basic_info"]["age"]
    expenses = profile["expenses"]

    monthly_expense = expenses["needs"] + expenses["obligations"]

    print(f"Current Monthly Expense (Needs + Obligations): ₹{monthly_expense}")

    #  User inputs
    retirement_age = int(input("Enter Retirement Age: "))
    life_expectancy = int(input("Enter Life Expectancy (default 75): ") or 75)
    inflation = float(input("Enter Inflation Rate (default 6%): ") or 6) / 100

    #  Time calculations
    years_to_retire = retirement_age - age
    years_post_retirement = life_expectancy - retirement_age

    if years_to_retire <= 0:
        print("Invalid retirement age")
        return None

    #  Inflate expenses
    inflated_expense = monthly_expense * (1 + inflation) ** years_to_retire

    #  Real return
    real_return = ((1 + xirr) / (1 + inflation)) - 1

    #  Corpus required
    temp = 1 + inflation
    corpus_required = inflated_expense * (
        temp * (temp ** years_post_retirement - 1)
    ) / (temp - 1)

    #  CALL SIP MODULE HERE
    sip = calculate_sip(
        corpus_required,
        real_return,
        years_to_retire
    )

    #  Return everything together
    return {
        "inflated_expense": inflated_expense,
        "real_return": real_return,
        "corpus_required": corpus_required,
        "retirement_age": retirement_age,
        "sip": sip
    }