import json
import sys

def generate_prompt_with_example(number_of_examples):
    examples = []

    # Fetching examples from the dataset
    with open('../datasets/grade-school-math/grade_school_math/data/train.jsonl', 'r') as f:
        for _ in range(number_of_examples):
            example = json.loads(f.readline())
            examples.append(example)

    # Formulate the prompt
    prompt = "I am a helpful assistant that can solve grade school math problems. Here are a couple of examples:\n\n"

    for i, example in enumerate(examples):
        prompt += f"Problem {i+1}: {example['question']}\nSolution: {example['answer']}\n\n"

    prompt += "Now, solve a new problem:\n\nProblem: "

    # Combine the prompt with the new problem
    return prompt