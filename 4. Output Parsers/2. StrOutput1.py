# Now we do using Output Parser

# Stroutputparser extract response.content from O/P.

# Flow: topic > LLM > Detail content > LLM > summary 


from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

# Load environment variables
load_dotenv()

# Initialize Gemini model
model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0.7
)

# Prompt 1: Generate a detailed report
template1 = PromptTemplate(
    template="Write a detailed report on {topic}",
    input_variables=["topic"]
)

# Prompt 2: Summarize the generated report
template2 = PromptTemplate(
    template="Write a 5-line summary of the following text:\n\n{text}",
    input_variables=["text"]
)

# Output parser
parser = StrOutputParser()

# Build chain
chain = (
    template1
    | model
    | parser
    | template2
    | model
    | parser
)

# Run chain
result = chain.invoke({"topic": "black hole"})

print(result)