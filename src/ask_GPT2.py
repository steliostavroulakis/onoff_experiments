from transformers import  pipeline
from create_prompt import generate_prompt_with_example
import json

with open('../datasets/grade-school-math/grade_school_math/data/train.jsonl', 'r') as f:
    new_problem = json.loads(f.readline())  # this is our new problem to be solved

def generate_response(prompt, model_name='gpt2'):
    # Create the text generation pipeline
    generator = pipeline('text-generation', model=model_name)
    
    # Generate the response
    response = generator(prompt, max_length=250, num_return_sequences=1, temperature=0.1)
    
    # Extract the generated text
    generated_text = response[0]['generated_text']
    
    return generated_text

# Create and print the generated prompt
full_prompt = generate_prompt_with_example(0) + new_problem['question']
print(full_prompt)
# Observe the answer from the model
response = generate_response(full_prompt)
print(response)