# Asks the user for their name and returns it for use throughout the chat
def greet_user():
    user_name = input("Hi! What's your name? ").strip()
    if not user_name:
        user_name = "Friend"              # fallback if the user just pressed Enter
    print(f"\nNice to meet you, {user_name}! Type 'help' to see what I can do.\n")
    return user_name                      # send the name back so other functions can use it

# Looks at what the user typed and returns the best matching reply
def get_response(user_message, user_name):
    clean = user_message.lower()          # lowercase so 'Hello' and 'hello' both match
    if "hello" in clean or "hi" in clean:
        return f"Hey {user_name}! Great to hear from you. 😊"
    elif "how are you" in clean:
        return "I'm doing great, thanks for asking! How about you?"
    elif "help" in clean:
        return "You can say: 'hello', 'how are you', 'joke', or 'bye' to exit."
    elif "joke" in clean:
        return "Why did the programmer quit? Because he didn't get arrays! 😄"
    elif "thank" in clean:
        return f"You're very welcome, {user_name}! 😊"
    else:
        return f"I'm not sure about that, {user_name}. Try typing 'help'!"  # default reply

# Keeps the conversation going until the user types 'bye' or 'quit'
def run_chat(user_name):
    while True:                                    # keep looping until we hit 'break'
        user_input = input(f"{user_name}: ").strip()
        if not user_input:                         # skip empty lines
            continue                               # jump back to the top of the loop
        if user_input.lower() in ("bye", "quit"):
            print(f"\nPyBot: Goodbye, {user_name}! Happy coding! 👋\n")
            break                                  # exit the loop and end the program
        reply = get_response(user_input, user_name)
        print(f"PyBot: {reply}\n")

# Ties everything together — this is where the program starts
def main():
    print("=" * 40)
    print("        Welcome to PyBot! 🤖")
    print("=" * 40 + "\n")
    user_name = greet_user()    # step 1: get the user's name
    run_chat(user_name)         # step 2: start chatting

if __name__ == "__main__":      # only run main() if this file is executed directly
    main()
