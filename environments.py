from langchain.llms import OpenAI

from itertools import islice
from typing import Iterable
import json

from rewards import GPT2Reward

class MathEnvironment:

    def __init__(self, n_examples:int) -> None:
        self._n_examples = n_examples

    def read(self) -> Iterable[dict]:

        # Create a question-answering pipeline
        #qa_pipeline = pipeline('text-generation', model='gpt2')
        llm = OpenAI(temperature=0.01, max_tokens=500, openai_api_key="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")


        with open('./datasets/grade-school-math/grade_school_math/data/train.jsonl', 'r') as f:

            examples = list(map(json.loads,islice(f,self._n_examples)))

            for line in f:
                new_problem = json.loads(line)  # this is our new problem to be solved

                context = new_problem['question']
                answer  = new_problem['answer'][new_problem['answer'].find("#### ")+5:]
                actions = examples
                rewards = GPT2Reward(context, answer, llm)

                yield { 'context': context, 'actions': actions, 'rewards': rewards }
