def calculate_sip(corpus_required, annual_return, years):
    monthly_rate = annual_return / 12
    months = years * 12

    if monthly_rate == 0:
        return corpus_required / months

    sip = (corpus_required * monthly_rate) / ((1 + monthly_rate) ** months - 1)
    return sip


def get_sip(profile, retirement_data, goals_data):
    print("\n--- SIP Calculation ---")

    # 🔹 Extract values from other modules
    corpus_required = retirement_data["corpus_required"]
    real_return = goals_data["real_return"]

    # 🔹 Time to invest
    age = profile["basic_info"]["age"]
    retirement_age = retirement_data["retirement_age"]

    years_to_invest = retirement_age - age

    if years_to_invest <= 0:
        print("Invalid retirement timeline")
        return None

    # 🔹 Calculate SIP
    sip = calculate_sip(corpus_required, real_return, years_to_invest)

    return sip