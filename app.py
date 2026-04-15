import streamlit as st
from agent import agent_response

st.title("🤖 AI Customer Support Agent")

if "messages" not in st.session_state:
    st.session_state.messages = []

user_input = st.chat_input("Ada yang bisa dibantu kakak...")

if user_input:
    st.session_state.messages.append(("user", user_input))
    response = agent_response(user_input)
    st.session_state.messages.append(("agent", response))

for role, msg in st.session_state.messages:
    if role == "user":
        st.chat_message("user").write(msg)
    else:
        st.chat_message("assistant").write(msg)
