from Financial_Engine.sip import calculate_sip


def calculate_goal_streamlit(current_cost, years, inflation, expected_return):

    inflated_cost = current_cost * (1 + inflation) ** years

    real_return = ((1 + expected_return) / (1 + inflation)) - 1

    sip = calculate_sip(inflated_cost, real_return, years)

    return {
        "inflated_cost": inflated_cost,
        "sip": sip
    }