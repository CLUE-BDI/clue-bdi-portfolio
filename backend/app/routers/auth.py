from fastapi import APIRouter, HTTPException, status
from ..models import RegisterRequest, LoginRequest, AuthResponse, UserProfile
from ..mock_db import db

router = APIRouter(prefix="/auth", tags=["auth"])

@router.post("/register", response_model=AuthResponse, status_code=status.HTTP_201_CREATED)
async def register(request: RegisterRequest):
    if db.get_user_by_email(request.email):
        raise HTTPException(status_code=400, detail="User already exists")
    
    user_data = {
        "email": request.email,
        "password": request.password,
        "fullName": request.fullName,
        "accountType": request.accountType
    }
    new_user = db.add_user(user_data)
    
    return AuthResponse(
        token="mock-jwt-token",
        user=UserProfile(id=new_user["id"], email=new_user["email"], fullName=new_user["fullName"])
    )

@router.post("/login", response_model=AuthResponse)
async def login(request: LoginRequest):
    user = db.get_user_by_email(request.email)
    if not user or user["password"] != request.password:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    
    return AuthResponse(
        token="mock-jwt-token",
        user=UserProfile(id=user["id"], email=user["email"], fullName=user.get("fullName"))
    )
