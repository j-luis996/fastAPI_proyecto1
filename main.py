#python
from typing import Optional
from fastapi.param_functions import Query
#pydantic
from pydantic import BaseModel
#FastAPI
from fastapi import FastAPI
from fastapi import Body
from fastapi import Query

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
@app.post("/api/person/new")
def create_person(person: Person = Body(...)):
    return person

#validaciones query parameters
@app.get("/person/detail")
def show_person(
    name: Optional[str] = Query(None,min_length=1,max_length=50),
    age: int = Query(...)
):
    return {name: age}