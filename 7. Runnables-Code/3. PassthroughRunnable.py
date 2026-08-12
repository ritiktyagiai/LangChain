# Data ---> Model ---> Return Same (Data)
# why this is helpful ? , if you want to save inbetween result of model

from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableParallel, RunnableSequence, RunnablePassthrough
from langchain_google_genai import ChatGoogleGenerativeAI

from dotenv import load_dotenv


load_dotenv()

prompt1 = PromptTemplate(
    template='Write a joke about {topic}',
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template='Rate the joke out of 10 , joke : {joke}',
    input_variables=['joke']
)

model = ChatGoogleGenerativeAI(
    model="gemini-3.6-flash"
)

parser = StrOutputParser()

generate_joke_chain = RunnableSequence(
    prompt1, model , parser
)

parallel_chain = RunnableParallel({
    'Joke_input_chain' : RunnablePassthrough(),
    'Rating_Chain': RunnableSequence(prompt2, model, parser) 
})

chain = RunnableSequence(generate_joke_chain, parallel_chain)
response = chain.invoke("AI")

print(response)
