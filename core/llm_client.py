import ollama
from config.settings import OLLAMA_MODEL, OLLAMA_TEMPERATURE

def call_llm(prompt):
    response = ollama.chat(
        model=OLLAMA_MODEL,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        options={
            "temperature": OLLAMA_TEMPERATURE
        }
    )
    return response["message"]["content"]
