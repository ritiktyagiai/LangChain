from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash" # model name,
    temperature=0.7 # randomness of the output, higher value means more random
, max_output_tokens=128 # maximum number of tokens in the output, default is 512
)

print("Welcome to the Gemini Chat LLM interface!")
input = input("Enter your question: ")

response = llm.invoke(input) # Text input ---> LLM ---> Text output + other information 
result = response.content  # for text output only use response.content

print("\nwhoami@LLM >> ",result)
