def evaluate_answer(role, mode, domain, question, user_answer):
    prompt = (
        f"You are an expert interviewer providing structured feedback.\n"
        f"Role: {role}\nMode: {mode}\nDomain: {domain}\n"
        f"Interview Question: {question}\n"
        f"Candidate's Answer: {user_answer}\n\n"
        f"Provide a detailed evaluation in the following format:\n"
        f"Score (out of 10): \n"
        f"Clarity: \n"
        f"Correctness: \n"
        f"Completeness: \n"
        f"Improvement Suggestion: "
    )

    inputs = tokenizer(prompt, return_tensors="pt")
    outputs = model.generate(
        **inputs,
        max_length=600, 
        temperature=0.7,
        do_sample=True,
        top_p=0.9
    )

    evaluation = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return evaluation
 