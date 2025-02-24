import streamlit as st
from text_sql_pipeline import get_sql_query
from transformers import AutoModelForCausalLM, AutoTokenizer

st.title("📑 Convert Text to SQL-Query")

# Initialize session state for question and schemas
if "question" not in st.session_state:
    st.session_state.question = ""

if "schemas" not in st.session_state:
    st.session_state.schemas = [""]  # Start with one input field

# Question input, using on_change callback to update session state
question = st.text_input(
    "Question", 
    value=st.session_state.question, 
    key="question", 
    placeholder="Enter your text"
)

# Update session state only if input is modified
if question != st.session_state.question:
    st.session_state.question = question  # Update stored question

# Display text inputs for schemas
valid_input = True  # Track if all schemas are valid
for i in range(len(st.session_state.schemas)):
    schema_input = st.text_input(
        f"Enter Table Schema {i+1}",
        value=st.session_state.schemas[i],
        key=f"schema_{i}",
        placeholder="CREATE TABLE Order_Items (order_id INTEGER, product_id INTEGER);",
    )

    # Update session state only if input is modified
    if schema_input != st.session_state.schemas[i]:
        st.session_state.schemas[i] = schema_input

    # Validation check: Ensure schema starts with "CREATE TABLE"
    if not schema_input.strip().upper().startswith("CREATE TABLE"):
        valid_input = False
        st.error(f"❌ Error in Table {i+1}: Schema must start with 'CREATE TABLE'. Please correct it.")

# Button to add another schema field, but only if all current schemas are valid
if st.button("➕ Add another table schema") and valid_input:
    st.session_state.schemas.append("")  # Add a new empty schema field
    st.rerun()  # 🔄 Force an immediate rerun to reflect changes instantly
elif not valid_input:
    st.warning("⚠️ Please correct the schema errors before adding another table.")

# Show valid schemas if all are correct
if valid_input:
    context = [schema for schema in st.session_state.schemas if schema]
    st.write("### ✅ Table Schemas Entered:")
    st.write(context)
