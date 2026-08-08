#                     summary-------\  
#                   /                \
# Paragraph >>>                   Combine both into Notes.
#                   \                / 
#                    Quiz-----------/


from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableParallel
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(
    model = "gemini-3.6-flash"
)

Paragraph = """A Transformer is a deep learning architecture introduced in 2017 that uses a self attention mechanism to understand relationships between different parts of the input data. Unlike RNNs and LSTMs, it processes all input tokens simultaneously, making training faster and more efficient. Transformers are highly effective at capturing long range dependencies and understanding context, which leads to better performance in language tasks. They form the foundation of modern AI models such as GPT, BERT, Gemini, Claude, and Llama. Today, Transformers are widely used in natural language processing, computer vision, speech recognition, and multimodal AI applications.
"""

prompt1 = PromptTemplate(
    template="Write a summary of 20-30 words explaining the paragraph in simple words. \n {paragraph}",
    input_variables=["paragraph"]
)

prompt2 = PromptTemplate(
    template="Write 5 important question from this paragraph for exam.  \n {paragraph}",
    input_variables=["paragraph"]
)

prompt3 = PromptTemplate(
    template="Combine the summary and questions as a notes for exam. \n summary : {summary} , questions: {questions}",
    input_variables=["summary", "questions"]
)

parser = StrOutputParser()

parallel_chain =  RunnableParallel(
    summary  = prompt1 | model | parser,
    questions =  prompt2 | model | parser
)

merge_chain = prompt3 | model | parser

chain = parallel_chain | merge_chain

response = chain.invoke(Paragraph)
print(response)



