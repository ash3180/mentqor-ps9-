import requests
from .config import MODEL_NAME, OLLAMA_URL, TIMEOUT


def call_llm(prompt):
    try:
        response = requests.post(
            OLLAMA_URL,
            json={
                "model": MODEL_NAME,
                "prompt": prompt,
                "stream": False
            },
            timeout=TIMEOUT
        )

        return response.json().get("response", "")

    except Exception as e:
        return f"LLM Error: {str(e)}"