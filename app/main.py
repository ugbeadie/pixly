# import uvicorn

# if __name__ == "__main__":
#     uvicorn.run(
#         "app.app:app",
#         host="0.0.0.0",
#         port=8000,
#         reload=True,
#     )

from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "hello world"}

@app.get("/greet")
def greet():
    return {"Message": "hello mama"}

@app.get("/greet/{name}")
def greet(name: str, age: Optional[int] = None):
    return {"Message": f"hello {name} and you are {age} years old"}

class Student(BaseModel):
    name: str
    age: int
    roll: int

@app.post("/create_student")
def create_student(student: Student):
    return {"Message": f"Student {student.name} created successfully with age {student.age} and roll number {student.roll}"}    