from dotenv import load_dotenv
from langchain_google_genai import GoogleGenerativeAIEmbeddings

load_dotenv()



embeddings = GoogleGenerativeAIEmbeddings(model="gemini-embedding-2-preview", output_dimensionality=768)

input = input("Enter a query to embed: ")
vector = embeddings.embed_query(input)

print("Embedding vector (first 5 dimensions):")
print(vector[:5])