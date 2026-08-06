#  Pydantic is another way to get structured output but it is better than typedict beacuse it allow us to evaluate aswell.

from pydantic import BaseModel, Field
from typing import  Optional, Literal

class Reviewer_detail(BaseModel):
    name : str
    age: int
    father_name : Optional[str] = None
    father_age : Optional[int] = 50 # set deafult to 50
    review_rating : int = Field(gt=0, lt=5, description="A Int value represent rating , 5 is excellent and 1 is bad.")


Reviewer1 = Reviewer_detail(name="Ritik" , age=21, review_rating= 4) 

print(Reviewer1)

# Convert Pydantic into dict or json aswell

Reviewer1_dict = dict(Reviewer1)

Reviewer1_json = Reviewer1.model_dump_json()