import streamlit as st
from langchain_helper import create_vectordb, get_response

# For Streamlit
__import__('pysqlite3')
import sys
sys.modules['sqlite3'] = sys.modules.pop('pysqlite3')

st.markdown("""
<style>
    #MainMenu
    {
        visibility: hidden;
    }
</style>
""", unsafe_allow_html=True)
st.markdown("""
Made with ❤ by [Soumya](https://github.com/imsoumya18)
""", unsafe_allow_html=True)
st.title("E-commerce FAQ 🛒")

query = st.text_input("Question: ")

if query:
    response = get_response(query)

    st.header("Response: ")
    st.write(response)
