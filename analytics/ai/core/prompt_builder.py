
def build_prompt(context, user_query):
    return f"""
You are a professional financial advisor.

Context:
{context}

User Question:
{user_query}

Instructions:
- Answer clearly and simply
- Give actionable advice
- Use numbers when helpful
- Be concise but useful
"""