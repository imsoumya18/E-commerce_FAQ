import streamlit as st
from langchain_helper import create_vectordb, get_response

# st.markdown("""
# <style>
#     #MainMenu
#     {
#         visibility: hidden;
#     }
# </style>
# """, unsafe_allow_html=True)
st.markdown("""
<footer>
  <p>Made by Soumya 🙋‍♂️</p>
  <p><a href="mailto:hege@example.com">hege@example.com</a></p>
</footer>
""", unsafe_allow_html=True)
st.title("E-commerce FAQ 🛒")

query = st.text_input("Question: ")

if query:
    response = get_response(query)

    st.header("Response: ")
    st.write(response)
