#python
from typing import Optional
from fastapi.param_functions import Path, Query,Path
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
    name: Optional[str] = Query(
        None,
        min_length=1,
        max_length=50,
        title = "Perosn Name",
        description= "this is the person name"
        ),
    age: int = Query(
        ...,
        title = "Persos age",
        description= "This is the person age, It´s required"
        )
):
    return {name: age}

#validaciones: path parameters

@app.get("/person/detail/{person_id}")
def show_person(
    person_id: int = Path(
        ...,
        gt=0,
        title= "person´s Id",
        description = "This is the ID person, It´s required"
        )
):
    return {person_id: "It_exist!!"}