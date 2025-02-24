# Text-to-SQL Query Generation

This repository contains a fine-tuned version of the **LLaMA-3.2-3B** model for generating SQL queries from natural language inputs. The model was fine-tuned using **QLoRA (Quantized Low-Rank Adaptation)** to efficiently handle large-scale parameter updates while minimizing resource requirements.

---
## Overview
This project fine-tunes the **LLaMA-3.2-3B** model for the task of converting natural language questions into SQL queries. It allows non-technical users to interact with databases by generating precise SQL queries based on questions and the provided table schema.

The model takes two inputs to generate accurate SQL queries:

1. **Question**: The natural language question, e.g., “List all customers with orders over $500.”  
2. **Context**: The table schema provided as `CREATE TABLE` SQL statements to help the model understand table relationships and structure.

### Use Cases
- **Conversational AI**: Enhances chatbots to answer questions based on relational data.
- **Educational Tools**: Aids in learning and practicing SQL through query examples.

---
## Model Details
- **Base Model**: LLaMA-3.2-3B  
- **Fine-tuning Method**: QLoRA (Quantized Low-Rank Adaptation) for efficient memory usage.  
- **Task**: Text-to-SQL query generation  
- **Framework**: Hugging Face Transformers  

---
## Installation & Requirements

To use this model, install the required dependencies:

```bash
pip install -q -U transformers bitsandbytes
```

---
## Usage Examples
### **1. Python API Usage**
#### ⚠️ Ensure you are connected to a GPU for faster generation
Clone the repository and import the model:

```bash
git clone https://github.com/SaiSanthosh1508/Text-to-SQL_Query-LLM
mv Text-to-SQL_Query-LLM/* ./
```

Load the model and generate SQL queries using Python:

```python
from transformers import AutoModelForCausalLM, AutoTokenizer
from text_sql_pipeline import get_sql_query

# Load Model
model = AutoModelForCausalLM.from_pretrained("sai-santhosh/text-2-sql-Llama-3.2-3B", load_in_4bit=True)
tokenizer = AutoTokenizer.from_pretrained("sai-santhosh/text-2-sql-Llama-3.2-3B")

# Single Table Example
question = "List all employees in the 'Sales' department hired after 2020."
context = "CREATE TABLE employees (id INT, name TEXT, department TEXT, hire_date DATE);"

print(get_sql_query(model, tokenizer, question, context))
```

For multiple tables:

```python
question_4 = "Find customers who placed orders above the average order amount."
context_4 = "CREATE TABLE Customers (customer_id INTEGER, name VARCHAR); CREATE TABLE Orders (order_id INTEGER, customer_id INTEGER, amount INTEGER);"

print(get_sql_query(model, tokenizer, question_4, context_4))
```

---
### **2. Command-Line Interface (CLI) Usage**

#### ⚠️ Ensure you are connected to a GPU for faster generation

Clone the repository:

```bash
git clone https://github.com/SaiSanthosh1508/Text-to-SQL_Query-LLM
mv Text-to-SQL_Query-LLM/* ./
```

#### **Single Table Example**
Run the command below to generate an SQL query from a natural language question and a single table schema:

```bash
python generate.py -q "Find the zip code where the mean visibility is lower than 10." -c "CREATE TABLE weather (zip_code VARCHAR, mean_visibility_miles INTEGER);"
```

#### **Multiple Tables Example**
To pass multiple table schemas, use `-c` before each table schema:

```bash
python generate.py -q "Find all cities with temperatures above 90°F." \
-c "CREATE TABLE weather (zip_code VARCHAR, city VARCHAR, temperature INTEGER);" \
-c "CREATE TABLE population (city VARCHAR, population INTEGER);"
```

This will generate an SQL query based on the provided context and return an explanation along with the query.

---
## Future Enhancements
- **Integrate a Streamlit UI** for an interactive web interface.
