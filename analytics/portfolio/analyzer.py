from .asset_mapper import map_assets
from .allocator import get_allocation
from .risk_analyzer import calculate_portfolio_risk
from .diversification import diversification_score
from .insights import generate_insights
from .schemas import PortfolioResult


def analyze_portfolio(profile):
    investments = profile["investments"]

    # Step 1: Map
    mapped = map_assets(investments)

    # Step 2: Allocation
    allocation, total = get_allocation(mapped)

    # Step 3: Risk
    risk_score, risk_category = calculate_portfolio_risk(allocation)

    # Step 4: Diversification
    diversification = diversification_score(allocation)

    # Step 5: Insights
    insights = generate_insights(allocation,total, risk_category, diversification)

    return PortfolioResult(
        allocation,
        total,
        risk_score,
        risk_category,
        diversification,
        insights
    )