from pydantic import BaseModel, EmailStr
#BaseModel: Classe base para criar esquemas.
#EmailStr: Valida se o campo é um email válido.

#UserBase: Define os campos básicos (nome e email).
class UserBase(BaseModel):
    name:str
    email:EmailStr

#UserCreate: Adiciona o campo de senha para criar um usuário.
class UserCreate(UserBase):
    password:str

#UserResponse: Define o formato da resposta, incluindo o id.
class UserResponse(UserBase):
    id: int

    #orm_mode = True Permite que objetos do SQLAlchemy sejam convertidos para o esquema automaticamente.
    class Config():
        from_attributes = True