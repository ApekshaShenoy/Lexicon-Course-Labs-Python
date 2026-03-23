# ============================================================
#  Simple Terminal Chatbot
#  For beginner Python students — no external libraries needed
# ============================================================

def get_response(user_message, user_name):
    """
    Look at what the user typed and return an appropriate reply.
    We convert to lowercase so 'Hello' and 'hello' both work.
    """
    message = user_message.lower()  # make matching case-insensitive

    # --- Keyword checks ---

    if "hello" in message or "hi" in message or "hey" in message:
        return f"Hey {user_name}! Great to hear from you. 😊"

    elif "how are you" in message or "how r u" in message:
        return "I'm doing wonderfully, thanks for asking! How about you?"

    elif "help" in message:
        return (
            "Sure! Here are some things you can say:\n"
            "  • 'hello'       — say hi\n"
            "  • 'how are you' — check in with me\n"
            "  • 'joke'        — hear something funny\n"
            "  • 'your name'   — find out who I am\n"
            "  • 'bye' / 'quit'— end the chat"
        )

    elif "joke" in message or "funny" in message or "laugh" in message:
        return "Why did the programmer quit his job? Because he didn't get arrays! 😄"

    elif "your name" in message or "who are you" in message:
        return "I'm PyBot — a simple chatbot made with pure Python. Nice to meet you!"

    elif "thank" in message:
        return f"You're very welcome, {user_name}! Happy to help. 😊"

    elif "age" in message or "how old" in message:
        return "I was born the moment you ran this script, so I'm brand new! 🐣"

    else:
        # Default friendly reply when nothing matches
        return (
            f"Hmm, I'm not sure how to respond to that, {user_name}. "
            "Try typing 'help' to see what I can do!"
        )


def main():
    # ── Welcome banner ──────────────────────────────────────
    print("=" * 45)
    print("       Welcome to PyBot! 🤖")
    print("=" * 45)

    # ── Ask for the user's name ─────────────────────────────
    user_name = input("Before we start, what's your name? ").strip()

    # Handle blank input gracefully
    if not user_name:
        user_name = "Friend"

    print(f"\nNice to meet you, {user_name}! 👋")
    print("I'm PyBot. Type 'help' to see what I can do.")
    print("Type 'quit' or 'bye' whenever you want to leave.\n")

    # ── Conversation loop ───────────────────────────────────
    while True:
        # Get input from the user
        user_input = input(f"{user_name}: ").strip()

        # Ignore empty input (user just pressed Enter)
        if not user_input:
            continue

        # Check if the user wants to exit
        if user_input.lower() in ("quit", "bye", "goodbye", "exit"):
            print(f"\nPyBot: It was lovely chatting with you, {user_name}! "
                  "Take care and happy coding! 👋🎉\n")
            break  # exit the loop and end the program

        # Get and print the chatbot's response
        response = get_response(user_input, user_name)
        print(f"PyBot: {response}\n")


# ── Run the program ─────────────────────────────────────────
if __name__ == "__main__":
    main()
