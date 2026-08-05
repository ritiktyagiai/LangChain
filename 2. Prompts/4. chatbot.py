# chatbot without history, with history with list soln is messages , but we need a dict ---> Lang chain detetct it. 

from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

load_dotenv()

model = ChatGoogleGenerativeAI(
    model="gemini-3.6-flash")

chat_history = [SystemMessage(content='You are a helpful AI assistant')] # building history 

while True:
    user_input = input('You: ')

    if user_input == 'exit':
        print("Exiting...")
        break

    chat_history.append(HumanMessage(content=user_input)) # adding user input to history
    result = model.invoke(chat_history)
    print("AI: ", result.text)
    chat_history.append(AIMessage(content=result.text)) # adding AI response to histor



# print(chat_history)    