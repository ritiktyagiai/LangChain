# //  we use json when our project is form in different languages and we want to use the same output format for all the languages.

from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

# Initialize Gemini
model = ChatGoogleGenerativeAI(
    model="gemini-3.6-flash",
    temperature=0
)

# JSON Schema
json_schema = {
    "title": "Review",
    "type": "object",
    "properties": {
        "summary": {
            "type": "string",
            "description": "Brief summary of the review"
        },
        "sentiment": {
            "type": "string",
            "enum": ["pos", "neg"],
            "description": "Overall sentiment"
        }
        
    },
    "required": ["summary", "sentiment"]
}

# Structured Output
structured_model = model.with_structured_output(json_schema)

result = structured_model.invoke("""
The Samsung Galaxy S24 Ultra is an amazing phone.
The camera is excellent and the battery lasts all day.
However, it is expensive and quite heavy.
""")

print(result)