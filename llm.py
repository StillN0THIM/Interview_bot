import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

model_name = "microsoft/DialoGPT-medium"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

step = 0
chat_history_ids = None

while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "quit"]:
        break

    new_input_ids = tokenizer.encode(user_input + tokenizer.eos_token, return_tensors='pt')

    if step == 0:
        bot_input_ids = new_input_ids
    else:
        bot_input_ids = torch.cat([chat_history_ids, new_input_ids], dim=-1)

    chat_history_ids = model.generate(bot_input_ids, 
    max_length=1000,
    pad_token_id=tokenizer.eos_token_id,
    temperature=0.7)

    bot_response = tokenizer.decode(chat_history_ids[:, bot_input_ids.shape[-1]:][0], skip_special_tokens=True)
    print(f"Bot: {bot_response}")

    step += 1
