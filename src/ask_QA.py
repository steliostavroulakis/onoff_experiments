from transformers import AutoTokenizer, AutoModelForQuestionAnswering, pipeline
from create_prompt import generate_prompt_with_example
import json

tokenizer = AutoTokenizer.from_pretrained("deepset/roberta-base-squad2")
model = AutoModelForQuestionAnswering.from_pretrained("deepset/roberta-base-squad2")

# Create a question-answering pipeline
qa_pipeline = pipeline("question-answering", model=model, tokenizer=tokenizer)


with open('../datasets/grade-school-math/grade_school_math/data/train.jsonl', 'r') as f:
    new_problem = json.loads(f.readline())  # this is our new problem to be solved

# Define a context and a question
context = generate_prompt_with_example(1)
print("Context: ----------------------------")
print(context)
question = new_problem['question']
print("Question: ----------------------------")
print(question)

# Use the pipeline to answer the question
answer = qa_pipeline({
    'context': context,
    'question': question
})

print(answer)