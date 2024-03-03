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
Made with ❤️ by [Soumya](https://github.com/imsoumya18)\n
Star ⭐ this repo on [GitHub](https://github.com/imsoumya18/E-commerce_FAQ)
""", unsafe_allow_html=True)
st.title("E-commerce FAQ 🛒")

st.markdown("""
The model is just for **demonstration purpose only**. It is trained using **only 80 Question - Answer pairs**.
So, expecting it to answer any question other then used for training with high accuracy is not a good idea.
You can [have a look at all the 80 questions](https://github.com/imsoumya18/E-commerce_FAQ/blob/main/Ecommerce_FAQs.csv)
and ask something similar or combined of multiple questions.\n
e.g. ***"How can I create an account?"*** or,\n
***"What payment methods do you accept?"*** or even,\n
***"How can I create an account and what payment methods do you accept?"*** , etc.
""", unsafe_allow_html=True)

query = st.text_input("Question: ")

if query:
    response = get_response(query)

    st.header("Response: ")
    st.write(response)
