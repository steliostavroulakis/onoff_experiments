from langchain.llms import OpenAI

llm = OpenAI(temperature=0.01, openai_api_key="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")
text = "James creates a media empire.  He creates a movie for $2000.  Each DVD cost $6 to make.  He sells it for 2.5 times that much.  He sells 500 movies a day for 5 days a week.  How much profit does he make in 20 weeks?"
print(llm(text))