import streamlit as st
from text_sql_pipeline import get_sql_query
from transformers import AutoModelForCausalLM, AutoTokenizer

st.title("📑 Convert Text to SQL-Query")

# Input for the main question
question = st.text_input("Question", key="question", placeholder="Enter your text")

# Initialize session state for schemas
if "schemas" not in st.session_state:
    st.session_state.schemas = [""]  # Start with one input field

# Initialize validation flag
valid_input = True

# Display text inputs for schemas with validation
for i in range(len(st.session_state.schemas)):
    st.session_state.schemas[i] = st.text_input(
        f"Enter Table Schema {i+1}",
        value=st.session_state.schemas[i],
        key=f"schema_{i}",
        placeholder="CREATE TABLE Order_Items (order_id INTEGER, product_id INTEGER);",
    )

    # Validation check: Ensure schema starts with "CREATE TABLE"
    if not st.session_state.schemas[i].strip().upper().startswith("CREATE TABLE"):
        valid_input = False
        st.error(f"❌ Error in Table {i+1}: Schema must start with 'CREATE TABLE'. Please correct it.")

# Button to add another schema field
if st.button("➕ Add another table schema"):
    st.session_state.schemas.append("")  # Add a new empty schema field
    st.rerun()  # 🔄 Force an immediate rerun to reflect changes instantly

# Only proceed if all schemas are valid
if valid_input:
    context = [schema for schema in st.session_state.schemas if schema]
    st.write("### ✅ Table Schemas Entered:")
    st.write(context)
else:
    st.warning("⚠️ Please correct the schema errors before proceeding.")
