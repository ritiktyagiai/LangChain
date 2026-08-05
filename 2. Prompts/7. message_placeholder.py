# using previous chat_history which is store in some file or database, we can load it and continue the conversation.
# 
# message_placeholder helps in loading the previous chat history and continue the conversation with the AI model.
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-3.6-flash")

chat_template = ChatPromptTemplate([
    ('system','You are a helpful customer support agent'), # System prompt
    MessagesPlaceholder(variable_name='prev_chat'), # Message placeholder to load previous chat history
    ('human', '{query}') # user prompt
])

chat_history = []
# load chat history from a file
with open('chat_history.txt') as f:
    chat_history.extend(f.readlines())

user_query = input("You: ")

prompt = chat_template.invoke({'prev_chat':chat_history, 'query': user_query})

response = model.invoke(prompt)

print(f"AI: {response.text}")