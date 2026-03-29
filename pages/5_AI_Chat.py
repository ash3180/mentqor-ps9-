
import streamlit as st
from analytics.ai.chat.chat_engine import chat_with_ai

st.title("AI Advisor")

if "profile" not in st.session_state:
    st.warning("Fill input first")
    st.stop()

if "portfolio" not in st.session_state:
    st.warning("Run portfolio first")
    st.stop()

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Show history
for chat in st.session_state.chat_history:
    with st.chat_message(chat["role"]):
        st.markdown(chat["content"])

user_input = st.chat_input("Ask about your portfolio...")

if user_input:
    st.session_state.chat_history.append({"role": "user", "content": user_input})

    response = chat_with_ai(
        user_input,
        st.session_state.profile,
        st.session_state.portfolio,
        st.session_state.rebalance
    )

    st.session_state.chat_history.append({"role": "assistant", "content": response})

    st.rerun()