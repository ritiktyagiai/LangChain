# with strctured output TypedDict fnx with Langchain

from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from typing import TypedDict, Annotated, Literal,Optional


load_dotenv()

model = ChatGoogleGenerativeAI(
    model="gemini-3.6-flash"
)

feedback = """I bought google pixel 10A phone , it works very smoothly, i loved the iphone."""

class Feedback(TypedDict):
    Summary : Annotated[str, "A 20 words summary about feedback."]
    sentiment: Annotated[Literal["+ve", "-ve"], "Return either postive feedback or negative feedback"]
    name: Annotated[Optional[str], "Write the name of the reviewer"]

structured_model = model.with_structured_output(Feedback)

response = structured_model.invoke(feedback)


print(response)

