from langchain.llms import OpenAI

class GPT2Reward:

    def __init__(self, context:str, answer:str, llm: OpenAI):
        self._context = context
        self._answer = answer
        self._llm = llm

    def eval(self, action):

        prompt = "I am a helpful assistant that can solve grade school math problems. Here are a couple of examples:\n\n"
        for i, example in enumerate(action):
            prompt += f"Problem {i+1}: {example['question']}\nSolution: {example['answer']}\n\n"
        prompt += "Now, solve a new problem:\n\nProblem: "
        prompt += self._context

        # Generate the response
        response = self._llm(prompt)

        if str(self._answer) in response:
            return 1
        else:
            return 0

        #return int(self._answer == response)
