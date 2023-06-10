from transformers import  pipeline
from create_prompt import generate_full_prompt

def generate_response(prompt, model_name='gpt2'):
    # Create the text generation pipeline
    generator = pipeline('text-generation', model=model_name)
    
    # Generate the response
    response = generator(prompt, max_length=100, num_return_sequences=1, temperature=0.7)
    
    # Extract the generated text
    generated_text = response[0]['generated_text']
    
    return generated_text

# Create and print the generated prompt
full_prompt = generate_full_prompt(2)
print(full_prompt)

# Observe the answer from the model
response = generate_response(full_prompt)
print(response)