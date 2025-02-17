# Text-to-SQL_Query-LLM

This repository contains a fine-tuned version of the LLaMA-3.2-3B model for generating SQL queries from natural language questions. The model was fine-tuned using QLoRA (Quantized Low-Rank Adaptation) to efficiently handle large-scale parameter updates.

## Overview

This project fine-tunes the LLaMA-3.2-3B model for the task of converting natural language questions into SQL queries. This fine-tuned model is designed to allow non-technical users to interact with databases.
The model requires two inputs to accurately generate the SQL-Query
1. Question - the question you want to ask or retrieve based on some restrictions
2. Context - This involves passing the schema of the table as like when CREATE TABLE ... . this helps the model to better understand the schema of the tables

## Model Details
* **Base Model:** LLaMA-3.2-3B
* **Fine-tuning Method:** QLoRA (Quantized Low-Rank Adaptation)
* **Task:** Text-to-SQL query generation
* **Framework:** Hugging Face Transformers


### Model Usage

The model can be found in Huggingface Hub or can directly access through the link below

[View Model Repository on Hugging Face](https://huggingface.co/sai-santhosh/text-2-sql-Llama-3.2-3B) 🤗


