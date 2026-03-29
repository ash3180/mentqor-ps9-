def clean_assets(mapped):
    return {k: v for k, v in mapped.items() if v > 0}