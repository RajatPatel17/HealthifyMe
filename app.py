import os 
import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI

gemini_api_key = os.getenv('Google_API_KEY2')

# Configure THe Model

model = ChatGoogleGenerativeAI(
    model = 'gemini-2.5-flash-lite',
    api_key = gemini_api_key
)


# Design the UI of Application
st.title("HealthifyMe : Your Personal Health Assistant")