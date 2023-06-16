from transformers import GPT2LMHeadModel, GPT2Tokenizer

tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
model = GPT2LMHeadModel.from_pretrained("gpt2")

question = "Hello, how are you?"

input_text = f"{question}\nResponse:"
encoded_input = tokenizer(input_text, return_tensors='pt')

# Get the attention mask
attention_mask = encoded_input['attention_mask']

output = model.generate(input_ids=encoded_input['input_ids'], 
                        max_length=100, 
                        num_return_sequences=1, 
                        no_repeat_ngram_size=2, 
                        do_sample=True, 
                        temperature=0.001, 
                        attention_mask=attention_mask, 
                        pad_token_id=tokenizer.eos_token_id)

decoded_output = tokenizer.decode(output[0], skip_special_tokens=True)

answer = decoded_output[len(tokenizer.decode(encoded_input['input_ids'][0], skip_special_tokens=True)):]

print('---------------')
print(answer.strip())
