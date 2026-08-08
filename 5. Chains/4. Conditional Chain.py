from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from pydantic import BaseModel, Field
from typing import Literal

load_dotenv()

gemini = ChatGoogleGenerativeAI(
    model="gemini-3.6-flash"
)

# Structured Output Schema
class Sentiment(BaseModel):
    sentiment: Literal["positive", "negative"] = Field(
        description="Provide the sentiment of the review."
    )

structured_model = gemini.with_structured_output(Sentiment)

review = """I've been using the OnePlus 7 for several years, and it still performs surprisingly well for everyday tasks. The Snapdragon 855 processor keeps the phone responsive, apps open quickly, and multitasking is smooth."""

prompt = PromptTemplate(
    template="Determine whether this review is positive or negative.\n\n{review}",
    input_variables=["review"],
)

positive_prompt = PromptTemplate(
    template="Write an appropriate response to this positive review.\n\n{feedback}",
    input_variables=["feedback"],
)

negative_prompt = PromptTemplate(
    template="Write an appropriate response to this negative review.\n\n{feedback}",
    input_variables=["feedback"],
)

parser = StrOutputParser()

# Get structured sentiment
sentiment_chain = prompt | structured_model

result = sentiment_chain.invoke({"review": review})

print(result)
print(result.sentiment)

# Choose response chain
if result.sentiment == "positive":
    chain = positive_prompt | gemini | parser
else:
    chain = negative_prompt | gemini | parser

response = chain.invoke({"feedback": review})

print(response)