# BUILD, store and download the prompt template in a file, and then load it from the file for future use.
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(
    model="gemini-3.6-flash")

# build the prompt template
prompt_template = PromptTemplate(
    template="You are a helpful Summary assistant. Answer the following question with in 20-30 words, Here is your question: {question}",
    input_variables=["question"]
)

#  use the prompt template to generate a prompt
user_question = input("Enter your question: ")

prompt = prompt_template.invoke({"question": user_question})
response = model.invoke(prompt)

print("AI: ", response.text)




#  store the prompt template in a file

prompt_template.save("my_template.json")