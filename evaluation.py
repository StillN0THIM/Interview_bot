def evaluate_answer(role, mode, domain, question, user_answer):
    prompt = (
        f"You are an expert interviewer.\n"
        f"Role: {role}\nMode: {mode}\nDomain: {domain}\n"
        f"Interview Question: {question}\n"
        f"Candidate's Answer: {user_answer}\n\n"
        f"Provide only a numeric score from 1 to 10 evaluating this answer."
    )

    inputs = tokenizer(prompt, return_tensors="pt")
    outputs = model.generate(
        **inputs,
        max_length=10,   
        temperature=0.0,
        do_sample=False
    )

    score = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return score.strip()  
