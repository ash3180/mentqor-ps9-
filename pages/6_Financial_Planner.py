
import streamlit as st
from Financial_Engine.tax import calculate_tax
from Financial_Engine.insurance import calculate_insurance
from analytics.financial.fire_engine import calculate_fire_streamlit
from analytics.financial.goals_engine import calculate_goal_streamlit

st.title("Financial Planner")


if "profile" not in st.session_state:
    st.warning("Please fill input first")
    st.stop()

profile = st.session_state.profile


# TAX

st.subheader("1. Tax Analysis")

tax_data = calculate_tax(profile)

col1, col2, col3 = st.columns(3)
col1.metric("Total Income", f"₹{tax_data['total_income']}")
col2.metric("Taxable Income", f"₹{tax_data['taxable_income']}")
col3.metric("Tax", f"₹{tax_data['tax']}")

for s in tax_data["suggestions"]:
    st.info(s)


#INSURANCE
st.subheader("2. Insurance")

ins_data = calculate_insurance(profile)

col1, col2 = st.columns(2)
col1.metric("Life Cover", f"₹{ins_data['life_insurance_needed']}")
col2.metric("Health Cover", f"₹{ins_data['health_insurance_needed']}")

for s in ins_data["suggestions"]:
    st.warning(s)


#FIRE
st.subheader("3. Retirement Planning")

xirr = st.slider("Expected Return (%)", 1, 20, 10) / 100
retirement_age = st.number_input("Retirement Age", 40, 80, 60)

fire_data = calculate_fire_streamlit(profile, xirr, retirement_age)

col1, col2 = st.columns(2)
col1.metric("Corpus Required", f"₹{int(fire_data['corpus_required'])}")
col2.metric("Monthly SIP", f"₹{int(fire_data['sip'])}")


#GOAL
st.subheader("4. Goal Planning")

goal_cost = st.number_input("Goal Cost", 10000)
years = st.slider("Years", 1, 30, 10)

goal = calculate_goal_streamlit(goal_cost, years, 0.06, xirr)

col1, col2 = st.columns(2)
col1.metric("Future Cost", f"₹{int(goal['inflated_cost'])}")
col2.metric("Required SIP", f"₹{int(goal['sip'])}")