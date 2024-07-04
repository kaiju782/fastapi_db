import streamlit as st
from db import Database
from db_manager import DatabaseManager

# 데이터베이스 초기화
db = Database("legal_cases.db")
db_manager = DatabaseManager(db)

st.title("Legal Cases Database")

search_term = st.text_input("Enter a search term:")

if st.button("Search"):
    if search_term:
        results = db_manager.search_cases(search_term)
        for result in results:
            st.write(f"Case ID: {result[0]}")
            st.write(f"Title: {result[1]}")
            st.write(f"Content: {result[2]}")
            st.write("---")
    else:
        st.write("Please enter a search term.")
