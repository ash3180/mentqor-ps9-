
import streamlit as st

st.set_page_config(layout="wide")
st.title(" Financial Profile Input")

# BASIC INFO
with st.expander("Basic Information", expanded=True):
    age = st.number_input("Age", min_value=18, max_value=100, value=25)

# INCOME
with st.expander("Income"):
    active_income = st.number_input("Active Income (Monthly)", min_value=0, value=50000)
    passive_income = st.number_input("Passive Income (Monthly)", min_value=0, value=0)


# EXPENSES
with st.expander("Expenses"):
    needs = st.number_input("Needs (Rent, Food, etc.)", min_value=0, value=20000)
    obligations = st.number_input("Obligations (EMI, Loans)", min_value=0, value=5000)

# INVESTMENTS
with st.expander("Investments"):
    col1, col2 = st.columns(2)

    with col1:
        stocks = st.number_input("Stocks", min_value=0, value=100000)
        mutual_funds = st.number_input("Mutual Funds", min_value=0, value=200000)
        fd = st.number_input("Fixed Deposits", min_value=0, value=50000)
        bonds = st.number_input("Bonds", min_value=0, value=20000)

    with col2:
        gold = st.number_input("Gold", min_value=0, value=30000)
        crypto = st.number_input("Crypto", min_value=0, value=10000)
        cash = st.number_input("Cash / Savings", min_value=0, value=20000)
        real_estate = st.number_input("Real Estate", min_value=0, value=0)

# FINANCIAL HEALTH
with st.expander("Financial Health"):
    insurance = st.selectbox(
        "Do you have insurance?",
        ["none", "basic", "adequate"]
    )

    tax_efficiency = st.selectbox(
        "Using tax-saving strategies?",
        ["no", "yes"]
    )

# SUBMIT BUTTON
st.divider()

if st.button("Save Profile & Continue"):

    profile = {
        "basic_info": {
            "age": age
        },
        "income": {
            "active_income": active_income,
            "passive_income": passive_income
        },
        "expenses": {
            "needs": needs,
            "obligations": obligations
        },
        "investments": {
            "stocks": stocks,
            "mutual_funds": mutual_funds,
            "fd": fd,
            "bonds": bonds,
            "gold": gold,
            "crypto": crypto,
            "cash": cash,
            "real_estate": real_estate
        },
        "financial_health": {
            "insurance": insurance,
            "tax_efficiency": tax_efficiency
        }
    }

    # Save to session
    st.session_state.profile = profile

    st.success("Profile Saved Successfully!")

    st.info("Go to Dashboard from sidebar")