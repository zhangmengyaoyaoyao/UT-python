
from openai import OpenAI
import os

# IMPORTANT: DO NOT MODIFY THIS FILE

API_KEY = "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"
CLIENT = OpenAI(api_key=API_KEY)

def query_llm(message: str) -> str:
    """
    Provided function to query the LLM.
    Args:
        message: The prompt to send to the LLM
    Returns:
        The LLM's response as a string
    """
    response = CLIENT.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": message}
    ]
    )
    return response.choices[0].message.content
    