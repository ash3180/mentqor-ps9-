import streamlit as st
from analytics.optimization.rebalancer import rebalance_portfolio

st.title("Rebalancing Engine")

if "portfolio" not in st.session_state:
    st.stop()

rebalance = rebalance_portfolio(st.session_state.portfolio)
st.session_state.rebalance = rebalance

#  TARGET ALLOCATION
st.subheader("1. Target Allocation")

for asset, value in rebalance.target.items():
    col1, col2 = st.columns([3, 1])
    col1.write(f"**{asset}**")
    col2.write(f"{value}%")
st.space()
st.space()

# BAR CHART

st.bar_chart(rebalance.target)


#  ACTION PLAN
st.subheader("2. Recommended Actions")

for action in rebalance.actions:
    st.success(f"{action}")