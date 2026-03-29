
import streamlit as st
import matplotlib.pyplot as plt
from analytics.portfolio.analyzer import analyze_portfolio
from analytics.portfolio.recommendation_engine import generate_recommendations
from analytics.ai.explainer import explain_recommendations


# PAGE CONFIG
st.title("Portfolio Analysis")

if "profile" not in st.session_state:
    st.warning("Please fill input first")
    st.stop()

portfolio = analyze_portfolio(st.session_state.profile)
st.session_state.portfolio = portfolio

allocation = portfolio.allocation

#  TOP METRICS (IMPORTANT)

col1, col2 = st.columns(2)

with col1:
    if "High" in portfolio.risk_category:
        st.error(f"Risk: {portfolio.risk_category}")
    elif "Moderate" in portfolio.risk_category:
        st.warning(f"Risk: {portfolio.risk_category}")
    else:
        st.success(f"Risk: {portfolio.risk_category}")

with col2:
    if "Poor" in portfolio.diversification:
        st.error(f"Diversification: {portfolio.diversification}")
    elif "Moderate" in portfolio.diversification:
        st.warning(f"Diversification: {portfolio.diversification}")
    else:
        st.success(f"Diversification: {portfolio.diversification}")




#  PIE CHART 
st.subheader("Asset Allocation")
fig, ax = plt.subplots(figsize=(4, 3)) 

# fig, ax = plt.subplots()

ax.pie(
    list(allocation.values()),
    labels=list(allocation.keys()),
    autopct="%1.1f%%"
)

st.pyplot(fig,use_container_width=False)


# TABLE + PROGRESS BARS
st.subheader("Allocation Breakdown")

total = sum(allocation.values())

for asset, value in allocation.items():

    percentage = (value / total) * 100 if total > 0 else 0

    col1, col2 = st.columns([3, 1])

    col1.write(f"**{asset}**")
    col2.write(f"{percentage:.1f}%")

    st.progress(int(percentage))




# RECOMMENDATIONS
st.subheader("Recommendations")

recommendations = generate_recommendations(portfolio)

if not recommendations:
    st.success("Your portfolio is well balanced")
else:
    for rec in recommendations:
        msg = rec["message"]

        if rec["type"] == "risk":
            st.error(f"{msg}")
        elif rec["type"] == "allocation":
            st.warning(f"{msg}")
        else:
            st.info(f"{msg}")

#AI integ.
st.subheader("AI Explanation")

with st.spinner("Generating explanation..."):
    explanation = explain_recommendations(recommendations, portfolio)

st.info(explanation)