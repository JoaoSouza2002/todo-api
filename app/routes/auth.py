from fastapi import APIRouter

router = APIRouter()

@router.post("/login")
def login(username: str, password: str):
    if username == "admin" and password == "admin":
        return {"token": "fake-token"}
    return {"error": "Invalid credentials"}