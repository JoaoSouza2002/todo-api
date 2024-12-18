from sqlalchemy import Column, Integer, String
from app.database import Base  # Importa a Base criada no database.py

# Modelo da tabela User
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    password = Column(String, nullable=False)