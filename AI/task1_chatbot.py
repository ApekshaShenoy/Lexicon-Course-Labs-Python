"""
Simple Rule-Based Chatbot — no API, no cost, runs 100% locally.
Usage: python chatbot.py
"""

import random
import datetime

# ── Response rules: list of (keywords, responses) ──────────────────────────
RULES = [
    (["hello", "hi", "hey", "howdy", "hiya"],
     ["Hey there! 👋", "Hi! How can I help?", "Hello! What's up?"]),

    (["how are you", "how's it going", "how do you do"],
     ["I'm just a program, but I'm doing great!", "Running smoothly, thanks for asking!", "All good on my end!"]),

    (["your name", "who are you", "what are you"],
     ["I'm PyBot, your local chatbot!", "Call me PyBot 🤖", "I'm PyBot — no internet needed!"]),

    (["bye", "goodbye", "see you", "quit", "exit"],
     ["Goodbye! 👋", "See you later!", "Bye! Come back anytime."]),

    (["thanks", "thank you", "thx"],
     ["You're welcome! 😊", "Happy to help!", "Anytime!"]),

    (["help", "what can you do"],
     ["I can chat, tell jokes, share the time/date, and answer simple questions. Try me!",
      "Ask me jokes, the time, or just say hi!"]),

    (["joke", "funny", "make me laugh"],
     [
         "Why do programmers prefer dark mode? Because light attracts bugs! 🐛",
         "Why did the computer go to the doctor? It had a virus! 💻",
         "I told my computer I needed a break. Now it won't stop sending me Kit-Kat ads.",
         "Why is Python the best language? Because it doesn't have to deal with Java problems! ☕",
     ]),

    (["time", "what time"],
     [lambda: f"The current time is {datetime.datetime.now().strftime('%H:%M:%S')} ⏰"]),

    (["date", "what day", "today"],
     [lambda: f"Today is {datetime.datetime.now().strftime('%A, %B %d %Y')} 📅"]),

    (["weather"],
     ["I can't check the weather without internet, but I hope it's sunny where you are! ☀️"]),

    (["age", "how old"],
     ["I was born the moment you ran this script, so I'm very young! 👶"]),

    (["favorite", "like"],
     ["I'm a bot, so I don't have favorites — but I like talking to you! 😄"]),

    (["happy", "great", "awesome", "good"],
     ["That's great to hear! 😊", "Awesome! Keep it up! 🎉", "Love the positive vibes!"]),

    (["sad", "bad", "unhappy", "upset"],
     ["Sorry to hear that. 😔 Hope things get better soon!", "Hang in there! 💪"]),

    (["what is python", "python language"],
     ["Python is a popular, beginner-friendly programming language known for its clean syntax. You're using it right now! 🐍"]),
]

FALLBACKS = [
    "Hmm, I'm not sure about that. Try asking something else!",
    "I didn't quite get that. Can you rephrase?",
    "Interesting! But I'm a simple bot — try asking me a joke or the time. 😅",
    "That's beyond my knowledge. I'm just a local chatbot!",
]

# ── Matching logic ───────────────────────────────────────────────────────────
def get_response(user_input: str) -> str:
    text = user_input.lower().strip()

    for keywords, responses in RULES:
        if any(kw in text for kw in keywords):
            reply = random.choice(responses)
            return reply() if callable(reply) else reply  # support lambdas

    return random.choice(FALLBACKS)

# ── Main loop ────────────────────────────────────────────────────────────────
def main():
    print("\n" + "═" * 45)
    print("   🤖  PyBot  —  Local Chatbot (no API)")
    print("═" * 45)
    print("  Say hi, ask for a joke, or the time!")
    print("  Type 'quit' or 'exit' to stop.\n")

    while True:
        try:
            user_input = input("You: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nGoodbye! 👋")
            break

        if not user_input:
            continue

        response = get_response(user_input)
        print(f"PyBot: {response}\n")

        if any(kw in user_input.lower() for kw in ["bye", "goodbye", "quit", "exit"]):
            break

if __name__ == "__main__":
    main()
