import streamlit as st
from text_sql_pipeline import get_sql_query
from transformers import AutoModelForCausalLM, AutoTokenizer


st.title("📑 Convert Text to SQL-Query")

question = st.text_input("Question",key=1,place_holder="Enter your text")
st.subheader(question)
