
import streamlit as st

st.set_page_config(page_title="AI Financial Advisor", layout="wide")

st.title("📊 Financial Dashboard")

# -------------------------------
# CHECK PROFILE
# -------------------------------
if "profile" not in st.session_state:
    st.warning("⚠️ Please fill input first")
    st.stop()

profile = st.session_state.profile
investments = profile["investments"]

# -------------------------------
# 💰 CALCULATIONS
# -------------------------------
total_investment = sum(investments.values())

total_income = (
    profile["income"]["active_income"] +
    profile["income"]["passive_income"]
)

total_expense = (
    profile["expenses"]["needs"] +
    profile["expenses"]["obligations"]
)

net_savings = total_income - total_expense

# -------------------------------
# 📊 TOP METRICS
# -------------------------------
col1, col2, col3, col4 = st.columns(4)

col1.metric("💰 Total Investment", f"₹{total_investment}")
col2.metric("📈 Total Income", f"₹{total_income}")
col3.metric("💸 Expenses", f"₹{total_expense}")
col4.metric("💡 Net Savings", f"₹{net_savings}")

# -------------------------------
# 📊 INVESTMENT CHART
# -------------------------------
st.subheader("📊 Investment Breakdown")

st.bar_chart(investments)

# -------------------------------
# 📄 PROFILE SUMMARY (CLEAN UI)
# -------------------------------
st.subheader("📄 Profile Summary")

col1, col2, col3 = st.columns(3)

# 👤 BASIC INFO
with col1:
    st.markdown("### 👤 Basic Info")
    st.markdown(f"""
    - **Age:** {profile['basic_info']['age']}
    """)

# 💰 INCOME
with col2:
    st.markdown("### 💰 Income")
    st.markdown(f"""
    - **Active Income:** ₹{profile['income']['active_income']}
    - **Passive Income:** ₹{profile['income']['passive_income']}
    - **Total Income:** ₹{total_income}
    """)

# 💸 EXPENSES
with col3:
    st.markdown("### 💸 Expenses")
    st.markdown(f"""
    - **Needs:** ₹{profile['expenses']['needs']}
    - **Obligations:** ₹{profile['expenses']['obligations']}
    - **Total Expense:** ₹{total_expense}
    """)

# -------------------------------
# 📊 INVESTMENT SUMMARY (CARDS)
# -------------------------------
st.subheader("📊 Investment Summary")

inv = profile["investments"]

col1, col2, col3, col4 = st.columns(4)

col1.metric("Stocks", f"₹{inv['stocks']}")
col2.metric("Mutual Funds", f"₹{inv['mutual_funds']}")
col3.metric("Gold", f"₹{inv['gold']}")
col4.metric("Crypto", f"₹{inv['crypto']}")

col1.metric("FD", f"₹{inv['fd']}")
col2.metric("Bonds", f"₹{inv['bonds']}")
col3.metric("Cash", f"₹{inv['cash']}")
col4.metric("Real Estate", f"₹{inv['real_estate']}")

# -------------------------------
# 🛡️ FINANCIAL HEALTH
# -------------------------------
st.subheader("🛡️ Financial Health")

col1, col2 = st.columns(2)

col1.info(f"Insurance: {profile['financial_health']['insurance']}")
col2.info(f"Tax Efficiency: {profile['financial_health']['tax_efficiency']}")

# -------------------------------
# 🚀 NAVIGATION
# -------------------------------
st.divider()
st.subheader("🚀 Explore")

col1, col2, col3 = st.columns(3)

with col1:
    if st.button("📊 Portfolio"):
        st.switch_page("pages/2_Portfolio.py")

with col2:
    if st.button("💡 Insights"):
        st.switch_page("pages/3_Insights.py")

with col3:
    if st.button("🔄 Rebalance"):
        st.switch_page("pages/4_Rebalance.py")