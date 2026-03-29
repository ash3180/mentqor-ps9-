# import streamlit as st

# st.title("💡 Insights")

# if "portfolio" not in st.session_state:
#     st.warning("Run portfolio first")
#     st.stop()

# for i in st.session_state.portfolio.insights:
#     st.write("-", i)

import streamlit as st

st.title("Portfolio Insights")

if "portfolio" not in st.session_state:
    st.stop()

insights = st.session_state.portfolio.insights

for insight in insights:
    if "🚨" in insight:
        st.error(insight)
    elif "⚠️" in insight:
        st.warning(insight)
    else:
        st.success(insight)