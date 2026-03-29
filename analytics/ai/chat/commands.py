def execute_command(command, profile, portfolio, rebalance):
    cmd = command.lower().strip()

    
    #ANALYZE
    
    if cmd == "/analyze":
        return format_analyze(portfolio)

    
    #REBALANCE
    
    elif cmd == "/rebalance":
        return format_rebalance(rebalance)

    
    #RISK
    
    elif cmd == "/risk":
        return format_risk(portfolio)

    
    #SUMMARY
    
    elif cmd == "/summary":
        return format_summary(portfolio, rebalance)

    
    #HELP
    
    elif cmd == "/help":
        return show_help()

    else:
        return "Unknown command. Type /help"


#FORMATTERS 

def format_analyze(portfolio):
    return f"""
📊 Portfolio Analysis

Allocation:
{portfolio.allocation}

Risk: {portfolio.risk_category}
Diversification: {portfolio.diversification}

Insights:
{format_list(portfolio.insights)}
"""


def format_rebalance(rebalance):
    return f"""
🔄 Rebalancing Plan

Target Allocation:
{rebalance.target}

Actions:
{format_list(rebalance.actions)}
"""


def format_risk(portfolio):
    return f"""
⚠️ Risk Analysis

Risk Level: {portfolio.risk_category}

Your Allocation:
{portfolio.allocation}
"""


def format_summary(portfolio, rebalance):
    return f"""
📋 Summary

Allocation: {portfolio.allocation}
Risk: {portfolio.risk_category}
Diversification: {portfolio.diversification}

Rebalancing Actions:
{format_list(rebalance.actions)}
"""


def show_help():
    return """
📌 Available Commands:

/analyze   → Portfolio breakdown  
/rebalance → Action plan  
/risk      → Risk details  
/summary   → Full summary  
/help      → Show commands
"""


def format_list(items):
    if not items:
        return "None"
    return "\n".join(f"- {item}" for item in items)