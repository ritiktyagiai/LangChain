#  Getting strcuture output froma LLMs , show that it can give to machine, Agents also need strctured output to work with LLMs.

# 3 methods to get structured output from LLMs
# 1. Using TypedDicts : only tell not validate
# 2. Using Pydantic : tell and validate
# 3. jsonschema : tell and validate

# 2 types of LLMs : 
# 1. that support structured output natively : OpenAI, LlamaIndex, LangChain ---------> Langchain provide with structured output fnx.
# 2. that don't support structured output natively : HuggingFace, Cohere, Mistral, MosaicML -----> Output parsers 

from typing import TypedDict

class Person(TypedDict):
    name: str
    age: int
    email: str

new_person1: Person = {
    "name": "John Doe",
    "age": 30,  # only tell to use int , but also accept string 
    "email": "john@gmail.com"
} 

new_person2: Person = {
    "name": "Jane Doe",
    "age": "25",  # only tell to use int , but also accept string
    "email": "john@gmail.com"
}

print(new_person1)
print(new_person2) # will not give error but age is string not int, so we need to validate it.