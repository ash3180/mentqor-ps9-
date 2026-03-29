def generate_actions(current, target, total_value):
    actions = []

    for asset in target:
        current_pct = current.get(asset, 0)
        target_pct = target[asset]

        diff = current_pct - target_pct

       
        if abs(diff) < 5:
            continue

        amount = (abs(diff) / 100) * total_value

        if diff > 0:
            actions.append(f"Sell ₹{int(amount)} from {asset}")
        else:
            actions.append(f"Invest ₹{int(amount)} into {asset}")

    return actions