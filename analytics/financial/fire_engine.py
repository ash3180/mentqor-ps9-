from Financial_Engine.sip import calculate_sip


def calculate_fire_streamlit(profile, xirr, retirement_age, life_expectancy=75, inflation=0.06):
    
    age = profile["basic_info"]["age"]
    expenses = profile["expenses"]

    monthly_expense = expenses["needs"] + expenses["obligations"]

    years_to_retire = retirement_age - age
    years_post_retirement = life_expectancy - retirement_age

    inflated_expense = monthly_expense * (1 + inflation) ** years_to_retire

    real_return = ((1 + xirr) / (1 + inflation)) - 1

    temp = 1 + inflation
    corpus_required = inflated_expense * (
        temp * (temp ** years_post_retirement - 1)
    ) / (temp - 1)

    sip = calculate_sip(corpus_required, real_return, years_to_retire)

    return {
        "corpus_required": corpus_required,
        "sip": sip,
        "inflated_expense": inflated_expense
    }