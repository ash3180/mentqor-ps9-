from datetime import datetime
from scipy.optimize import newton


def calculate_xirr(cash_flows, dates):
    def npv(rate):
        return sum(
            cf / (1 + rate) ** ((d - dates[0]).days / 365)
            for cf, d in zip(cash_flows, dates)
        )

    try:
        return newton(npv, 0.1)
    except:
        return None


# 🔹 Option 1 (AUTO investment from profile)
def xirr_from_profile(profile):
    print("\n--- Option 1: Using Your Investment Data ---")

    total_investment = sum(profile["investments"].values())

    print(f"Total Investment detected: ₹{total_investment}")

    final_value = float(input("Enter current/final portfolio value (₹): "))

    start_date = datetime.strptime(
        input("Start date (YYYY-MM-DD): "), "%Y-%m-%d"
    )
    end_date = datetime.strptime(
        input("End date (YYYY-MM-DD): "), "%Y-%m-%d"
    )

    cash_flows = [-total_investment, final_value]
    dates = [start_date, end_date]

    return calculate_xirr(cash_flows, dates)


# 🔹 Option 2
def xirr_direct():
    print("\n--- Option 2: Direct XIRR ---")
    xirr = float(input("Enter XIRR (%): "))
    return xirr / 100


# 🔹 Option 3
def xirr_from_transactions():
    print("\n--- Option 3: Transaction-based XIRR ---")

    cash_flows = []
    dates = []

    n = int(input("Enter number of transactions: "))

    for i in range(n):
        print(f"\nTransaction {i+1}")
        amount = float(input("Amount (negative = invest, positive = return): "))
        date = datetime.strptime(
            input("Date (YYYY-MM-DD): "), "%Y-%m-%d"
        )

        cash_flows.append(amount)
        dates.append(date)

    return calculate_xirr(cash_flows, dates)


#MASTER FUNCTION 
def get_xirr(profile):
    print("\n=== XIRR Options ===")
    print("1. Use my investment data (auto)")
    print("2. Enter XIRR directly")
    print("3. Enter all transactions")

    choice = int(input("Choose option (1/2/3): "))

    if choice == 1:
        return xirr_from_profile(profile)

    elif choice == 2:
        return xirr_direct()

    elif choice == 3:
        return xirr_from_transactions()

    else:
        print("Invalid choice")
        return None