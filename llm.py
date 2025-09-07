from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import torch

model_name = "google/flan-t5-small"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

def generate_interview_question(role="engineering"):
    prompt = f"Generate a challenging interview question for a {role} job interview."
    
    inputs = tokenizer(prompt, return_tensors="pt")
    outputs = model.generate(
        **inputs,
        max_length=100,
        temperature=0.7,
        do_sample=True,
        top_p=0.9
    )
    
    question = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return question

# Simple interactive loop
while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "quit"]:
        break

    if "question" in user_input.lower() or "generate" in user_input.lower():
        print("Bot:", generate_interview_question(role="engineering"))
    else:
        print("Bot: Please ask me to generate a question about an engineering job interview.")
