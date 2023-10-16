from fastapi import FastAPI

app = FastAPI()

# TODO items database
todos = {}

# Create a TODO item
@app.post("/todos/")
async def create_todo(todo: str, todo_id: int):
    todos[todo_id] = todo
    return {"message": "TODO item created successfully!"}

# Get all TODO items
@app.get("/todos/")
async def get_all_todos():
    return todos

# Get a single TODO item
@app.get("/todos/{todo_id}")
async def get_todo(todo_id: int):
    try:
        todo = todos[todo_id]
        return todo
    except KeyError:
        # Return a 404 response if the TODO item is not found
        return {"message": "TODO item not found."}, 404

# Update a TODO item
@app.put("/todos/{todo_id}")
async def update_todo(todo_id: int, todo: str):
    try:
        todos[todo_id] = todo
        return {"message": "TODO item updated successfully!"}
    except KeyError:
        # Return a 404 response if the TODO item is not found
        return {"message": "TODO item not found."}, 404

# Delete a TODO item
@app.delete("/todos/{todo_id}")
async def delete_todo(todo_id: int):
    try:
        del todos[todo_id]
        return {"message": "TODO item deleted successfully!"}
    except KeyError:
        # Return a 404 response if the TODO item is not found
        return {"message": "TODO item not found."}, 404

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)

