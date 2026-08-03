from dotenv import load_dotenv
from langchain_google_genai import GoogleGenerativeAI

load_dotenv() # load api from .env file

llm = GoogleGenerativeAI(
    model="gemini-2.5-flash"
)

print("Welcome to the Gemini LLM interface!")
input = input("Enter your question: ")

result = llm.invoke(input)

print("Response from Gemini LLM:\n")
print(result)


# text input ---> LLM ---> only text output 