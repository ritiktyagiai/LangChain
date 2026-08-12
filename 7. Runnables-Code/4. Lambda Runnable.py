# convert any python fnx into runnable.

from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableLambda, RunnableParallel, RunnableSequence , RunnablePassthrough
from langchain_google_genai import ChatGoogleGenerativeAI

from dotenv import load_dotenv

def wordcount(word):
    return len(word.split(" "))

load_dotenv()

prompt = PromptTemplate(
    template='Write a joke about {topic}',
    input_variables=['topic']
)


model = ChatGoogleGenerativeAI(
    model="gemini-3.6-flash"
)

parser = StrOutputParser()

joke_gen_chain = RunnableSequence(prompt, model, parser)

parallel_chain = RunnableParallel({
    'joke': RunnablePassthrough(),
    'word_count': RunnableLambda(wordcount)
})

chain = RunnableSequence(joke_gen_chain, parallel_chain)
response = chain.invoke("AI")

result = '''{} \n Word count - {}'''.format(response['joke'], response['word_count'])

print(result)