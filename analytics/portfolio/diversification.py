
def diversification_score(allocation):
    if not allocation:
        return "No Investments"

    active_assets = len(allocation)

    #  Get max concentration
    max_allocation = max(allocation.values())

    #  Calculate balance 
    avg = sum(allocation.values()) / active_assets

    imbalance = sum(abs(v - avg) for v in allocation.values()) / active_assets

    #RULES

    # Case 1: Highly concentrated
    if max_allocation > 70:
        return "Poorly Diversified (Highly Concentrated)"

    # Case 2: Few assets + imbalance
    if active_assets <= 2:
        return "Poorly Diversified"

    # Case 3: Moderate spread but uneven
    if imbalance > 25:
        return "Moderately Diversified (Imbalanced)"

    # Case 4: Good spread + balanced
    if active_assets >= 4 and max_allocation < 50:
        return "Well Diversified"

    return "Moderately Diversified"