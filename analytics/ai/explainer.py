from analytics.ai.core.llm_client import call_llm


def explain_recommendations(recommendations, portfolio):
    """
    Converts recommendations into human-friendly explanation using LLM
    """

    if not recommendations:
        return "Your portfolio looks well balanced. No major improvements needed."

    # Extract only messages
    rec_text = [rec["message"] for rec in recommendations]

    prompt = f"""
You are a financial advisor.

User Portfolio:
Allocation: {portfolio.allocation}
Risk: {portfolio.risk_category}
Diversification: {portfolio.diversification}

Recommendations:
{rec_text}

Explain each recommendation clearly:
- Why it is needed
- What the user should do
- Keep it simple and actionable
- Avoid technical jargon
"""

    try:
        return call_llm(prompt)
    except Exception:
        return "AI explanation unavailable"