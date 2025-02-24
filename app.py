import streamlit as st

st.title("📑 Convert Text to SQL-Query")

# Initialize session state for question and schemas
if "question" not in st.session_state:
    st.session_state.question = ""

if "schemas" not in st.session_state:
    st.session_state.schemas = [""]  # Start with one input field

# Function to handle adding a new schema
def add_schema():
    """Adds a new empty schema input field if all previous ones are valid."""
    valid_input = True
    for i, schema in enumerate(st.session_state.schemas):
        if not schema.strip().upper().startswith("CREATE TABLE"):
            valid_input = False
            st.error(f"❌ Error in Table {i+1}: Schema must start with 'CREATE TABLE'. Please correct it.")
    
    if valid_input:
        st.session_state.schemas.append("")  # Add a new empty schema

# Question input
question = st.text_input(
    "Question", 
    value=st.session_state.question, 
    key="question", 
    placeholder="Enter your text"
)

if "question" not in st.session_state:
    st.session_state.question = question

# Display text inputs for schemas
for i in range(len(st.session_state.schemas)):
    st.session_state.schemas[i] = st.text_input(
        f"Enter Table Schema {i+1}",
        value=st.session_state.schemas[i],
        key=f"schema_{i}",
        placeholder="CREATE TABLE Order_Items (order_id INTEGER, product_id INTEGER);",
    )

# Button to add another schema field with function call
st.button("➕ Add another table schema", on_click=add_schema)
