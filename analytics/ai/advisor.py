
from .core.prompt_builder import build_prompt
from .core.llm_client import call_llm


def generate_advice(context):
    prompt = build_prompt(context, "Give overall financial advice")
    return call_llm(prompt)