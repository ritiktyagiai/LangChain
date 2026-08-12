# from langchain_core.runnables import RunnableBranch

# branch = RunnableBranch(
#     (condition1, runnable1),
#     (condition2, runnable2),
#     default_runnable
# )

from dotenv import load_dotenv

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import (
    RunnableSequence,
    RunnableBranch,
    RunnablePassthrough,
    RunnableLambda,
)

load_dotenv()

# Prompt to generate a detailed report
prompt1 = PromptTemplate(
    template="Write a detailed report on {topic}",
    input_variables=["topic"],
)

# Prompt to summarize the report
prompt2 = PromptTemplate(
    template="Summarize the following text:\n\n{text}",
    input_variables=["text"],
)

# Gemini Model
model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",      # or "gemini-3.6-flash"
    temperature=0.7,
)

# Convert AIMessage -> String
parser = StrOutputParser()

# Report Generation Chain
report_gen_chain = prompt1 | model | parser

# Summary Chain
summary_chain = (
    RunnableLambda(lambda report: {"text": report})
    | prompt2
    | model
    | parser
)

# RunnableBranch works like if-else
branch_chain = RunnableBranch(
    (
        lambda report: len(report.split()) > 300,
        summary_chain,                     # If report > 300 words, summarize it
    ),
    RunnablePassthrough(),                 # Else, return the original report
)

# Complete Pipeline
final_chain = RunnableSequence(
    report_gen_chain,
    branch_chain,
)

# Run the chain
result = final_chain.invoke(
    {"topic": "AI vs Human"}
)

print(result)