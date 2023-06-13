from transformers import pipeline

class GPT2Reward:

    def __init__(self, context:str, answer:str, qa_pipeline: pipeline):
        self._context = context
        self._answer = answer
        self._qa_pipeline = qa_pipeline

    def eval(self, action):

        prompt = "I am a helpful assistant that can solve grade school math problems. Here are a couple of examples:\n\n"
        for i, example in enumerate(action):
            prompt += f"Problem {i+1}: {example['question']}\nSolution: {example['answer']}\n\n"
        prompt += "Now, solve a new problem:\n\nProblem: "
        prompt += self._context

        # Generate the response
        response = self._qa_pipeline(prompt, max_length=250, num_return_sequences=1, temperature=0.1)

        # Extract the generated text
        response = response[0]['generated_text']

        return int(self._answer == response)
