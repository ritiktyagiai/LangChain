from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash"
)

print("Welcome to the Gemini Chat LLM interface!")
input = input("Enter your question: ")

response = llm.invoke(input)
result = response.content

print("\nwhoami@LLM >> ",result)
