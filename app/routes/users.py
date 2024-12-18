from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.db import SessionLocal
from app.schemas import UserCreate, UserResponse
from app.models import User

router = APIRouter()
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/users/", response_model=UserResponse)
def create_user(user: UserCreate, database: Session = Depends(get_db)):
    database_user = database.query(User).filter(User.email == user.email).first()
    if database_user:
        raise HTTPException(status_code=400, detail="Email já cadastrado!")

    new_user = User(name=user.name,email=user.email,password=user.password)

    database.add(new_user)
    database.commit()
    database.refresh(new_user)
    return new_user
    
@router.get("/")
def list_users(database: Session = Depends(get_db)):
    users = database.query(User).all()
    return users

@router.get("/{user_id}")
def get_user(user_id: int, database: Session = Depends(get_db)):
    user = database.query(User).filter(User.id == user_id).first()
    if not user:
         HTTPException(status_code=404, detail="User not found")
    return user







