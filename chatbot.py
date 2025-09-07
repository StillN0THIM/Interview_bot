from question import generate_question
from evaluation import evaluate_answer

# Ask for role, mode, domain once
role = input("Enter role (e.g., software engineer): ")
mode = input("Enter mode (e.g., technical, HR): ")
domain = input("Enter domain (optional, e.g., AI, cloud): ")

print("\nType 'generate' to get a question, 'evaluate' to evaluate your answer, 'quit' to stop.\n")

current_question = None

while True:
    user_input = input("You: ")

    if user_input.lower() in ["exit", "quit"]:
        break

    if "generate" in user_input.lower():
        current_question = generate_question(role, mode, domain)
        print("Bot (Question):", current_question)

    elif "evaluate" in user_input.lower():
        if not current_question:
            print("Bot: First, generate a question.")
            continue

        user_answer = input("Your Answer: ")
        feedback = evaluate_answer(role, mode, domain, current_question, user_answer)
        
        # ✅ Print the evaluation result here
        print("\nBot (Evaluation Feedback):")
        print(feedback)

    else:
        print("Bot: Type 'generate' to get a question or 'evaluate' to evaluate your answer.")
