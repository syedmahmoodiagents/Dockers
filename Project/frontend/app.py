import os
import requests
import streamlit as st

API_URL = os.getenv("API_URL", "http://backend:8000")

st.title("Streamlit + FastAPI")
if st.button("Call API"):
    st.write(requests.get(f"{API_URL}/hello").json())