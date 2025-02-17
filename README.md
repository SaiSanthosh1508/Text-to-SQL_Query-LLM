# Text-to-SQL Query LLM

This repository contains a fine-tuned version of the **LLaMA-3.2-3B** model for generating SQL queries from natural language inputs. The model was fine-tuned using **QLoRA (Quantized Low-Rank Adaptation)** to efficiently handle large-scale parameter updates while minimizing resource requirements.  

---

## Overview

This project fine-tunes the **LLaMA-3.2-3B** model for the task of converting natural language questions into SQL queries. It is designed to allow non-technical users to easily interact with databases by generating precise SQL queries based on questions and the provided table schema.

The model takes two inputs to accurately generate the SQL query:

1. **Question**: The natural language question, such as “List all customers with orders over $500.”  
2. **Context**: The table schema provided as part of a `CREATE TABLE` SQL statement. This helps the model understand table relationships and structure for more accurate query generation.

### Use Cases
- **Conversational AI**: Enhances chatbots to answer questions based on relational data.
- **Educational Tools**: Aids in learning and practicing SQL through query examples.
  
---

## Model Details
- **Base Model**: LLaMA-3.2-3B  
- **Fine-tuning Method**: QLoRA (Quantized Low-Rank Adaptation), which reduces memory usage and enables efficient fine-tuning.  
- **Task**: Text-to-SQL query generation  
- **Framework**: Hugging Face Transformers  

---

## Installation & Requirements

To use this model, ensure the required dependencies are installed:

```bash
pip install transformers
```

## Usage Example
```
!git clone https://github.com/SaiSanthosh1508/Text-to-SQL_Query-LLM
!mv Text-to-SQL_Query-LLM/text_sql_pipeline.py text_sql_pipeline.py
```

```python
from transformers import AutoModelForCausalLM, AutoTokenizer

model = AutoModelForCausalLM.from_pretrained("sai-santhosh/text-2-sql-Llama-3.2-3B",load_in_4bit=True)
tokenizer = AutoTokenizer.from_pretrained("sai-santhosh/text-2-sql-Llama-3.2-3B")

from text_sql_pipeline import get_sql_query

question = "List all employees in the 'Sales' department hired after 2020."
context = "CREATE TABLE employees (id INT, name TEXT, department TEXT, hire_date DATE);"

get_sql_query(model,tokenizer,question,context)
```
For queries involving multiple table see the usage below

```python

```

