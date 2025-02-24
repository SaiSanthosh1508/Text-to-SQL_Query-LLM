from transformers import pipeline
import re

def get_sql_query(model ,tokenizer,question,context):

    """
    Generate an SQL query and explanation based on a natural language question and table schema context.

    Parameters:
    ----------
    model : str
        The instance of the transformers model e.g. model = AutoModelForCausalLM.from_pretrained(model_name)
    tokenizer : str
        The name or path of the tokenizer associated with the model.
    question : str
        The natural language question to be converted into an SQL query.
    context : str
        The schema or table structure (provided as a `CREATE TABLE` statement) to help the model understand the database format.
        

    Returns: None
    """

    pipe = pipeline(
    "text-generation", model=model, tokenizer=tokenizer)

    system_prompt = """Provide the SQL query to the question based on the context in below format
                                                    1. SQL Query: start with ```sql
                                                    2. Explanation of the query: start with ```explanation

            make the explanation clear and detail in less than 75 words"""

    prompt = pipe.tokenizer.apply_chat_template(
        [   {"role": "system", "content" : system_prompt},
            {"role": "user", "content": f"Question: {question} Context: {context}"}],
        tokenize=False,
        add_generation_prompt=True,
    )


    outputs = pipe(
        prompt,
        max_length=350,
        clean_up_tokenization_spaces=True
    )

    generated_text = outputs[0]['generated_text']

    generated_text = generated_text.replace(system_prompt,"")
    sql_query_pattern = r"```sql\n(.*?)\n```"
    sql_query_match = re.search(sql_query_pattern, generated_text, re.DOTALL)
    sql_query = sql_query_match.group(1).strip() if sql_query_match else None

    explanation_pattern = r"\*\*Explanation\:\*\*(.*)"
    explanation_match = re.search(explanation_pattern, generated_text, re.DOTALL)
    explanation = explanation_match.group(1).strip() if explanation_match else None

    # print("\n\nQuery:\n-----------\n",sql_query)
    # print("\n\nExplanation:\n-----------\n",explanation)
    return query,explanation
