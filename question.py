from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

model_name = "google/flan-t5-small"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

def generate_question(role, mode, domain):
    prompt = f"Generate a {mode} interview question for the role of {role}"
    if domain:
        prompt += f" in the domain of {domain}"
    prompt += "."

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
