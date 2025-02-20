# 🎈 Blank app template

A simple Streamlit app template for you to modify!

[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://blank-app-template.streamlit.app/)

### How to run it on your own machine

1. Install the requirements

   ```
   $ pip install -r requirements.txt
   ```

2. Run the app

   ```
   $ streamlit run streamlit_app.py
   ```
import streamlit as st

st.title("Therapy Assistant")

query = st.text_input("Ask about your past therapy sessions:")
if st.button("Search"):
    response = query_therapy_notes(query)  # Function from LlamaIndex
    st.write(response)