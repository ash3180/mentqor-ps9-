
from .router import route_input
from .commands import execute_command
from .context_builder import build_full_context
from .memory import add_message, get_history
from analytics.ai.core.prompt_builder import build_prompt
from analytics.ai.core.llm_client import call_llm


def chat_with_ai(user_input, profile, portfolio, rebalance):

   
    #ROUTING
    
    route = route_input(user_input)

    
    #COMMAND FLOW
    
    if route == "command":
        return execute_command(user_input, profile, portfolio, rebalance)

    
    #CHAT FLOW (LLM)
    
    context = build_full_context(profile, portfolio, rebalance)
    history = get_history()

    prompt = f"""
Chat History:
{history}

{build_prompt(context, user_input)}
"""

    add_message("user", user_input)

    response = call_llm(prompt)

    add_message("ai", response)

    return response