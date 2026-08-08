from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from pydantic import BaseModel, Field
from typing import Literal
from langchain_core.prompts import PromptTemplate

load_dotenv()

model = ChatGoogleGenerativeAI(
    model = "gemini-3.6-flash"
)

#  simple pipeline using chain
# Reviews >>>> LLM >>> sentiment

class feedback(BaseModel):
    sentiment : Literal["Positive", "Negative"] = Field (description="Provide sentiment for the review.")

structured_model = model.with_structured_output(feedback)

prompt = PromptTemplate(
    template="Provide the sentiment of the review either Positive or Negative. \n {Review}",
    input_variables=["Review"]
)

Review = "I've been using the OnePlus 7 for several years, and it still performs surprisingly well for everyday tasks. The Snapdragon 855 processor keeps the phone responsive, apps open quickly, and multitasking is smooth."

# Building Simple Chain

chain = prompt | structured_model

response = chain.invoke(Review)

print(response)







