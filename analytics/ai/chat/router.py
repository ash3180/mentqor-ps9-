def route_input(user_input):
    user_input = user_input.strip()

    if user_input.startswith("/"):
        return "command"
    return "chat"
