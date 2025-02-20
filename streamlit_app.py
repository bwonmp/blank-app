import streamlit as st

st.title("Therapy Assistant")

query = st.text_input("Ask about your past therapy sessions:")
if st.button("Search"):
    response = query_therapy_notes(query)  # Function from LlamaIndex
    st.write(response)