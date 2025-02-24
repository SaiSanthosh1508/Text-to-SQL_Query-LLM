import streamlit as st
from text_sql_pipeline import get_sql_query
from transformers import AutoModelForCausalLM, AutoTokenizer

st.title("📑 Convert Text to SQL-Query")

# Input for the main question
question = st.text_input("Question", key="question", placeholder="Enter your text")

# Initialize session state for schemas and validation trigger
if "schemas" not in st.session_state:
    st.session_state.schemas = [""]  # Start with one input field

if "validate_clicked" not in st.session_state:
    st.session_state.validate_clicked = False  # Track if validation should trigger

# Display text inputs for schemas
for i in range(len(st.session_state.schemas)):
    st.session_state.schemas[i] = st.text_input(
        f"Enter Table Schema {i+1}",
        value=st.session_state.schemas[i],
        key=f"schema_{i}",
        placeholder="CREATE TABLE Order_Items (order_id INTEGER, product_id INTEGER);",
    )

# Button to add another schema field
if st.button("➕ Add another table schema"):
    st.session_state.schemas.append("")  # Add a new empty schema field
    st.session_state.validate_clicked = False  # Reset validation when adding new schema
    st.rerun()  # 🔄 Force an immediate rerun to reflect changes instantly

# Button to validate and proceed
if st.button("✅ Submit"):
    st.session_state.validate_clicked = True  # Enable validation

# Validation only occurs after Submit is clicked
valid_input = True
if st.session_state.validate_clicked:
    for i, schema in enumerate(st.session_state.schemas):
        if not schema.strip().upper().startswith("CREATE TABLE"):
            valid_input = False
            st.error(f"❌ Error in Table {i+1}: Schema must start with 'CREATE TABLE'. Please correct it.")

# Show valid schemas only if validation is triggered and valid
if st.session_state.validate_clicked and valid_input:
    context = [schema for schema in st.session_state.schemas if schema]
    st.write("### ✅ Table Schemas Entered:")
    st.write(context)
elif st.session_state.validate_clicked:
    st.warning("⚠️ Please correct the schema errors before proceeding.")
