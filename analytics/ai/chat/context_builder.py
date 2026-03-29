def build_full_context(profile, portfolio, rebalance,
                       fire_data=None, goal_data=None,
                       tax_data=None, insurance_data=None):

    context = f"""
USER PROFILE:
Age: {profile['basic_info']['age']}
Income: {profile['income']['active_income']}

PORTFOLIO:
Allocation: {portfolio.allocation}
Risk: {portfolio.risk_category}
Diversification: {portfolio.diversification}

INSIGHTS:
{portfolio.insights}

REBALANCING:
{rebalance.actions}
"""

    if fire_data:
        context += f"\nFIRE:\nCorpus: {fire_data['corpus_required']}, SIP: {fire_data['sip']}"

    if goal_data:
        context += f"\nGOALS:\n{goal_data}"

    if tax_data:
        context += f"\nTAX:\nTax: {tax_data['tax']}"

    if insurance_data:
        context += f"\nINSURANCE:\n{insurance_data['suggestions']}"

    return context