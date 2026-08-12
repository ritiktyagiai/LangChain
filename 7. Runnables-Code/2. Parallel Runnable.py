from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableParallel, RunnableSequence
from langchain_google_genai import ChatGoogleGenerativeAI

from dotenv import load_dotenv


load_dotenv()

prompt1 = PromptTemplate(
    template='Write a joke about {topic}',
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template='Rate the joke from 0 to 10 \n Write a joke about {topic}',
    input_variables=['topic']
)

model = ChatGoogleGenerativeAI(
    model="gemini-3.6-flash"
)

parser = StrOutputParser()

# take dict
chain = RunnableParallel(
    {
        'chain1' : RunnableSequence(prompt1, model , parser),
        'chain2' : RunnableSequence(prompt2, model, parser)
    }
)

response = chain.invoke("AI")

print(response)