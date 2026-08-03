from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
import os


load_dotenv()

print(os.getenv("HUGGINGFACEHUB_API_TOKEN"))

llm = HuggingFaceEndpoint(
    repo_id="Qwen/Qwen3-0.6B",
    task="text-generation"
    
)

chat_model = ChatHuggingFace(llm=llm)

print("Welcome to the Hugging Face Chat LLM interface!\n")
input_text = input("Enter your question: ")

response = chat_model.invoke(input_text)  # Text input ---> LLM ---> Text output + other information
result = response.content  # for text output only use response.content  

print("\nwhoami@HF-LLM >> ", result)
