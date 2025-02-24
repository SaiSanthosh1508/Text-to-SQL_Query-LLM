import streamlit as st
from text_sql_pipeline import get_sql_query
from transformers import AutoModelForCausalLM, AutoTokenizer

st.title("📑 Convert Text to SQL-Query")

# Input for the main question
question = st.text_input("Question", key="question", placeholder="Enter your text")

# Initialize session state for storing schemas
if "schemas" not in st.session_state:
    st.session_state.schemas = [""]  # Start with one input field

# Display all text inputs for schemas
for i in range(len(st.session_state.schemas)):
    st.session_state.schemas[i] = st.text_input(
        f"Enter Table Schema {i+1}",
        value=st.session_state.schemas[i],
        key=f"schema_{i}",
        placeholder="CREATE TABLE Order_Items (order_id INTEGER, product_id INTEGER);",
    )

# Button to add more schema inputs dynamically
if st.button("➕ Add another table schema"):
    st.write(st.session_state.schema.values())
    st.session_state.schemas.append("")  # Add a new empty schema field

# Store all schemas in the context list
context = [schema for schema in st.session_state.schemas if schema]

st.write("### Table Schemas Entered:")
st.write(context)
