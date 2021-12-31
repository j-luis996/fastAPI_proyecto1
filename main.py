#python
from typing import Optional
#pydantic
from pydantic import BaseModel
#FastAPI
from fastapi import FastAPI
from fastapi import Body

app = FastAPI()

#models
class Person(BaseModel):
    name: str 
    a_paterno: str
    a_materno: str
    age: Optional[int] = 0
    user_name: str
    email: str
    is_active: Optional[bool] = False

@app.get("/")
def home():
    return {"hello": "word"}

#reques an response body
@app.post("/person/new")
def create_person(person: Person = Body(...)):
    return person
