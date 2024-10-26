import uvicorn
from fastapi import FastAPI

from pydantic import EmailStr, BaseModel

app = FastAPI()

class CreateUser(BaseModel):
    email: EmailStr

@app.get("/")
def index():
    return {"message": "Hello World"}

@app.get("/hello")
def hello(name: str = "World"):
    name = name.strip().title()
    return {"message": f"Hello {name}"}

@app.post("/users/")
def create_user(user: CreateUser):
    return {
        "message": "User created",
        "Email": f"User {user.email}"
    }

@app.post("/calc/add")
def add(a: int, b: int):
    return {
        "a": a,
        "b": b,
        "result": a + b
        }


@app.get("/items/")
def items():
    return [
        "item1",
        "item2",
    ]

@app.get("/items/latest/")
def get_latest():
    return {"items": {"id": 0, "name": "LATEST"}}


@app.get("/items/{item_id}/")
def  get_item(item_id: int):
    return {"item": {
            "id": item_id,
        }}


if "__main__" == __name__:
    uvicorn.run("main:app", reload=True)
