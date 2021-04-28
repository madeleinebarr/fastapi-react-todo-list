from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

origins = [
    "http://localhost:3000",
    "localhost:3000"
]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

# create a base route


@app.get("/", tags=["root"])
async def read_root() -> dict:
    return {"message": "Welcome to your todo list."}

# sample data

todos = [
    {
        "id": 1,
        "item": "Go for a bike ride"
    },
    {
        "id": 2,
        "item": "Read FastAPI documentation"
    },
    {
        "id": 3,
        "item": "Make tzatziki"
    }
]

# get all todos


@app.get("/todos", tags=["todos"])
async def get_todos() -> dict:
    return {"data": todos}


# create a todo

@app.post("/todos", tags=["todos"])
async def add_todo(todo: dict) -> dict:
    todos.append(todo)
    return {
        "data": {"Todo added."}
    }

# update a todo


@app.put("/todos/{id}", tags=["todos"])
async def update_todo(id: int, body: dict) -> dict:
    for todo in todos:
        if int(todo["id"]) == id:
            todo["item"] = body["item"]
            return {
                "data": f"Todo with id {id} has been updated."
            }

    return {
        "data": f"Todo with id {id} not found."
    }

# delete a todo


@app.delete("/todos/{id}", tags=["todos"])
async def delete_todo(id: int) -> dict:
    for todo in todos:
        if int(todo["id"]) == id:
            todos.remove(todo)
            return {
                "data": f"Todo with id {id} has been removed."
            }

    return {
        "data": f"Todo with id {id} not found."
    }
