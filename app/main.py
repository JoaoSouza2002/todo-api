from fastapi import FastAPI
from app.routes import users, auth, products
from fastapi.responses import FileResponse
import os

# Inicialização da aplicação
app = FastAPI(title="Projeto FastAPI")

@app.get("/favicon.ico", include_in_schema=False)
async def favicon():
    return FileResponse(os.path.join(os.getcwd(), "static", "favicon.ico"))

# Inclusão das rotas
app.include_router(users.router, prefix="/api/v1/users", tags=["Users"])
app.include_router(auth.router, prefix="/api/v1/auth", tags=["Authentication"])
app.include_router(products.router, prefix="/api/v1/products", tags=["Products"])

# Rota raiz
@app.get("/")
def root():
    return {"message": "Welcome to the FastAPI Project"}
