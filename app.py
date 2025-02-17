import streamlit as st
from src.chatbot import get_response
from src.roast_mode import get_roast

# Streamlit Page Config
st.set_page_config(page_title="🔥Roast", page_icon="🔥", layout="wide")

# Custom CSS for Styling
st.markdown(
    """
    <style>
    body {
        background-color: #D8B9FF;  /* Light purple background */
        color: #1e1e1e;  /* Dark text color for contrast */
    }
    .stTextInput, .stButton>button {
        border-radius: 10px;
        font-size: 18px;
        background-color: #9c7aff;  /* Light purple button */
        color: white;
    }
    .stTextInput>div>div>input {
        color: black !important;  /* Input text in black for readability */
        padding: 10px;
        border-radius: 8px;
    }
    h1 {
        text-align: center;
        color: #6A0DAD;  /* Dark purple for the header */
        font-size: 36px;
    }
    h2 {
        text-align: center;
        color: #8A2BE2;  /* Medium purple for secondary headers */
        font-size: 24px;
    }
    .stWrite {
        font-size: 20px;
        color: #FFD700;  /* Gold text color */
    }
    footer {
        text-align: center;
        font-size: 16px;
        color: white;
    }
    </style>
    """,
    unsafe_allow_html=True
)


# UI Header
st.markdown("<h1 style='text-align: center; color: red;'>🔥 Roast 🔥</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center;'>Talk to the bot in ATL slang or type 'Roast me' for a burn! 😂</h3>", unsafe_allow_html=True)

# Chat Input
user_input = st.text_input("You: ", "")

if st.button("Send 🚀"):
    if user_input.lower() == "roast me":
        response = get_roast()
    else:
        response = get_response(user_input)

    # Display Chatbot Response
    st.markdown(f"🤖 **Chatbot:** {response}", unsafe_allow_html=True)

# Footer
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size: 18px; color: white;'>Developed by KRIS | Love & Humor 💙</p>", unsafe_allow_html=True)
