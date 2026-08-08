from urllib import response

from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

model = ChatGoogleGenerativeAI(
    model = "gemini-3.6-flash"
)

prompt = PromptTemplate(
    template="Write an appropriate reply to the customer based on the review of customer like Thankyou or sorry , etc just 3-4 words. \n {review}",
    input_variables=["review"]
)

parser = StrOutputParser()

review = "I've been using the OnePlus 7 for several years, and it still performs surprisingly well for everyday tasks. The Snapdragon 855 processor keeps the phone responsive, apps open quickly, and multitasking is smooth."

# Chain

chain = prompt | model | parser

response = chain.invoke(review)

print(response)
