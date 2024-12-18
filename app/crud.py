from sqlalchemy.orm import Session
from app import models

def create_todo_item(db: Session, title: str, description: str):
    db_item = models.TodoItem(title=title, description=description)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

def get_todo_items(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.TodoItem).offset(skip).limit(limit).all()

def get_todo_item(db: Session, todo_id: int):
    return db.query(models.TodoItem).filter(models.TodoItem.id == todo_id).first()
