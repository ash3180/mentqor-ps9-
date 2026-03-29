from .target_allocator import get_target_allocation
from .action_generator import generate_actions
from .schemas import RebalanceResult


def rebalance_portfolio(portfolio_result):
    current = portfolio_result.allocation
    total = portfolio_result.total
    risk = portfolio_result.risk_category

    #  target allocation
    target = get_target_allocation(risk)

    #  actions
    actions = generate_actions(current, target, total)

    return RebalanceResult(target, actions)