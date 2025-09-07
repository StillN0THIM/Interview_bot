from question import generate_question
from evaluation import evaluate_answer
from session_tracker import SessionTracker

user_id = input("Enter User ID: ")
role = input("Enter role (e.g., software engineer): ")
mode = input("Enter mode (e.g., technical, HR): ")
domain = input("Enter domain (optional, e.g., AI, cloud): ")

tracker = SessionTracker(user_id, role, mode)

print("\nType 'generate' to get a question, 'evaluate' to answer, 'quit' to stop.\n")

current_question = None

while True:
    user_input = input("You: ")

    if user_input.lower() in ["exit", "quit"]:
        tracker.save_session()
        break

    elif "generate" in user_input.lower():
        current_question = generate_question(role, mode, domain)
        print("Bot (Question):", current_question)

    elif "evaluate" in user_input.lower():
        if not current_question:
            print("Bot: First, generate a question.")
            continue

        user_answer = input("Your Answer: ")
        score = evaluate_answer(role, mode, domain, current_question, user_answer)

        print("\nBot (Evaluation Feedback):")
        print(f"Score (1-10): {score}")

        tracker.add_record(
            question=current_question,
            answer=user_answer,
            score=int(score) if score.isdigit() else None,
            feedback=f"Score provided: {score}"
        )

    else:
        print("Bot: Type 'generate' to get a question or 'evaluate' to evaluate your answer.")
