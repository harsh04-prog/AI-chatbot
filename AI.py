import streamlit as st
import google.generativeai as genai

# ---------------------------
# CONFIGURATION
# ---------------------------
API_KEY = "enter your API key"
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel("gemini-1.5-flash")

# ---------------------------
# STREAMLIT PAGE SETTINGS
# ---------------------------
st.set_page_config(page_title="Gemini Chatbot", page_icon="🤖", layout="centered")
st.title("🤖 Gemini Chatbot")
st.write("Chat with Google's Gemini! Type your message below.")

# ---------------------------
# SESSION STATE TO STORE CHAT HISTORY
# ---------------------------
if "chat" not in st.session_state:
    st.session_state.chat = model.start_chat(history=[])
if "messages" not in st.session_state:
    st.session_state.messages = []

# ---------------------------
# DISPLAY CHAT HISTORY
# ---------------------------
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# ---------------------------
# USER INPUT
# ---------------------------
user_input = st.chat_input("Type your message...")
if user_input:
    # Show user message
    st.chat_message("user").markdown(user_input)
    st.session_state.messages.append({"role": "user", "content": user_input})
    
    # Get Gemini response
    response = st.session_state.chat.send_message(user_input)
    bot_reply = response.text
    
    # Show Gemini response
    with st.chat_message("assistant"):
        st.markdown(bot_reply)
    st.session_state.messages.append({"role": "assistant", "content": bot_reply})
