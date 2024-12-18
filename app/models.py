from sqlalchemy import Column, Integer, String
from app.db import Base
class TodoItem(Base):
    __tablename__ = "todo_items"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String)
    done = Column(Integer, default=0) 
