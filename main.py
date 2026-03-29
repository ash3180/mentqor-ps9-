from Input_layer.input import get_full_user_profile
from analytics.portfolio.analyzer import analyze_portfolio
from analytics.optimization.rebalancer import rebalance_portfolio
from analytics.ai.advisor import generate_advice
from analytics.ai.chat.chat_engine import chat_with_ai

def main():
    user_profile = get_full_user_profile()

    print("\n--- User Profile Summary ---")
    for section, details in user_profile.items():
        print(f"\n{section.upper()}:")
        for key, value in details.items():
            print(f"  {key}: {value}")
    
    portfolio = analyze_portfolio(user_profile)
    print("\n Portfolio Allocation:", portfolio.allocation)
    print(" Total:", portfolio.total)
    print(" Risk:", portfolio.risk_category)
    print(" Diversification:", portfolio.diversification)

    print("\n Insights:")
    for i in portfolio.insights:
        print("-", i)
    
    rebalance = rebalance_portfolio(portfolio)

    print("\n Rebalancing Plan:")
    print("Target Allocation:", rebalance.target)

    for action in rebalance.actions:
        print("-", action)


    print("\n Financial AI Assistant\n")
    print("Type /help to see commands\n")

    while True:
        user_input = input("You: ")

        if user_input.lower() == "exit":
            break

        response = chat_with_ai(
            user_input,
            user_profile,
            portfolio,
            rebalance
    )
        print("\nAI:", response)
        print()



if __name__ == "__main__":
    main()