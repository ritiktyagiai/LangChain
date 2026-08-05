# build a fix template so that user donot get too much power.

from langchain_core.prompts import PromptTemplate


# set restriction that user get 20-30 words answer only, answer from ai engineer pov. etc etc 

engineer_template = PromptTemplate(
    template = """
you are a expert ai engineer , summarize the AI term is easy way for a 5 year old child to understand.The term is {term_input} and the explanation should be in {style_input} style and the length of the explanation should be 20-30 words.
""" ,
input_variables = ['term_input', 'style_input'],
validate_template = True # must provide all the input variables when invoking the template otherwise it will raise an error

)


# save for future use
engineer_template.save("engineer_template.json")