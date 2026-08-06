from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from typing import Annotated, Optional, Literal
from pydantic import BaseModel, Field


load_dotenv()

# schema building

class feedback(BaseModel):
    Summary : str = Field( description="A 20 words summary about feedback.")
    sentiment: Literal["+ve", "-ve"] = Field( description="Return either postive feedback or negative feedback"
    )

review = """I bought google pixel 10A phone , it works very smoothly, i loved the iphone."""

model = ChatGoogleGenerativeAI(
    model="gemini-3.6-flash"
)

structured_model = model.with_structured_output(feedback)

response = structured_model.invoke(review)


print(response)