from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(
    model="gemini-3.6-flash",
    temperature=0,  # Gemini 3.0+ defaults to 1.0
)

while True:
    prompt = input("ritik@root# Enter your prompt: ")

    if prompt.lower() in ["exit", "quit"]:
        print("Exiting...")
        break
    response = model.invoke(prompt)
    print("AI: " , response.text)


# user can take advantage of this prompt feature because there is no restrictions.