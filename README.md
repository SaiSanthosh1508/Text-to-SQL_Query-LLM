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
