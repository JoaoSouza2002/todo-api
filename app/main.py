from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from app import crud, models, db
from pydantic import BaseModel

app = FastAPI()

class TodoItemCreate(BaseModel):
    title: str
    description: str

class TodoItemResponse(BaseModel):
    id: int
    title: str
    description: str
    done: int

    class Config:
        from_attributes = True

@app.post("/todos/", response_model=TodoItemResponse)
def create_todo_item(todo: TodoItemCreate, db: Session = Depends(db.get_db)):
    return crud.create_todo_item(db=db, title=todo.title, description=todo.description)

@app.get("/todos/", response_model=list[TodoItemResponse])
def get_todo_items(skip: int = 0, limit: int = 100, db: Session = Depends(db.get_db)):
    return crud.get_todo_items(db=db, skip=skip, limit=limit)

@app.get("/todos/{todo_id}", response_model=TodoItemResponse)
def get_todo_item(todo_id: int, db: Session = Depends(db.get_db)):
    db_item = crud.get_todo_item(db=db, todo_id=todo_id)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Todo not found")
    return db_item
