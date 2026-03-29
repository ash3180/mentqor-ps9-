def get_allocation(assets):
    total = sum(assets.values())

    if total == 0:
        return {}

    return {
        k: round((v / total) * 100, 2)
        for k, v in assets.items()
    }, total