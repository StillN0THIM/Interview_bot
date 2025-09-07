from question import generate_question

# Ask for details once at the beginning
role = input("Enter role (e.g., software engineer): ")
mode = input("Enter mode (e.g., technical, HR): ")
domain = input("Enter domain (optional, e.g., AI, cloud): ")

print("\nType 'exit' or 'quit' to stop.\n")

# Interactive loop
while True:
    user_input = input("You: ")

    if user_input.lower() in ["exit", "quit"]:
        break

    if "generate" in user_input.lower():
        print("Bot:", generate_question(role, mode, domain))
    else:
        print("Bot: Type 'generate' to get an interview question.")
