from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

model_name = "google/flan-t5-small"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

def evaluate_answer(role, mode, domain, question, user_answer):
    prompt = (
        f"You are an expert interviewer providing a numeric evaluation score.\n"
        f"Role: {role}\nMode: {mode}\nDomain: {domain}\n"
        f"Interview Question: {question}\n"
        f"Candidate's Answer: {user_answer}\n\n"
        f"Only respond with a single number from 1 to 10 that represents the score."
    )

    inputs = tokenizer(prompt, return_tensors="pt")
    outputs = model.generate(
        **inputs,
        max_length=5,
        do_sample=False
    )

    score = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return score.strip()
