import argparse
import re
from transformers import pipeline, AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig
import warnings

def generate(question, context):
    """
    Generate an SQL query and explanation based on a natural language question and table schema context.

    Parameters:
    ----------
    question : str
        The natural language question to be converted into an SQL query.
    context : list
        A list of schema or table structures (provided as `CREATE TABLE` statements) to help the model understand the database format.

    Returns: None
    """
    # Combine multiple context statements into one
    context_str = " ".join(context)

    # Load model in 4-bit mode
    bnb_config = BitsAndBytesConfig(load_in_4bit=True)
    model = AutoModelForCausalLM.from_pretrained("sai-santhosh/text-2-sql-Llama-3.2-3B", quantization_config=bnb_config)
    tokenizer = AutoTokenizer.from_pretrained("sai-santhosh/text-2-sql-Llama-3.2-3B")

    # Initialize text generation pipeline
    pipe = pipeline("text-generation", model=model, tokenizer=tokenizer)

    # Define system instruction
    system_prompt = """Provide the SQL query to the question based on the context in the following format:
                       1. SQL Query: start with ```sql
                       2. Explanation of the query: start with ```explanation
                       
                       Make the explanation clear and detailed in less than 75 words."""

    # Create prompt
    prompt = pipe.tokenizer.apply_chat_template(
        [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": f"Question: {question} Context: {context_str}"},
        ],
        tokenize=False,
        add_generation_prompt=True,
    )

    # Generate response
    outputs = pipe(prompt, max_length=350, clean_up_tokenization_spaces=True)
    generated_text = outputs[0]['generated_text'].replace(system_prompt, "")

    # Extract SQL query
    sql_query_pattern = r"```sql\n(.*?)\n```"
    sql_query_match = re.search(sql_query_pattern, generated_text, re.DOTALL)
    sql_query = sql_query_match.group(1).strip() if sql_query_match else None

    # Extract explanation
    explanation_pattern = r"\*\*Explanation\:\*\*(.*)"
    explanation_match = re.search(explanation_pattern, generated_text, re.DOTALL)
    explanation = explanation_match.group(1).strip() if explanation_match else None

    # Print results
    print("\n\nQuery:\n-----------\n", sql_query)
    print("\n\nExplanation:\n-----------\n", explanation)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate an SQL query based on a natural language question and database schema.")
    
    parser.add_argument("-q", "--question", type=str, required=True, help="The natural language question to be converted into an SQL query.")
    parser.add_argument("-c", "--context", type=str, nargs='+', required=True, help="One or more CREATE TABLE statements describing the database schema.")
    
    args = parser.parse_args()
    warnings.filterwarnings("ignore")
    generate(args.question, args.context)
