import random

quotes = [
    "Believe in yourself and all that you are.",
    "Success is not final, failure is not fatal.",
    "Do something today that your future self will thank you for.",
    "Dream big and dare to fail.",
    "Hard work beats talent when talent doesn't work hard.",
    "Stay positive, work hard, make it happen.",
    "Push yourself, because no one else is going to do it for you.",
    "Great things never come from comfort zones."
]

print("✨ RANDOM QUOTE GENERATOR ✨\n")

while True:
    user_input = input("Press ENTER to get a quote or type 'exit' to quit: ").lower()

    if user_input == "exit":
        print("\n👋 Goodbye! Stay motivated.")
        break

    quote = random.choice(quotes)
    print(f"\n💬 {quote}\n")
    