from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.orm import Session
from ..models import RegisterRequest, LoginRequest, AuthResponse, UserProfile
from ..db_models import User
from ..database import get_db
import uuid

router = APIRouter(prefix="/auth", tags=["auth"])

@router.post("/register", response_model=AuthResponse, status_code=status.HTTP_201_CREATED)
async def register(request: RegisterRequest, db: Session = Depends(get_db)):
    existing_user = db.query(User).filter(User.email == request.email).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="User already exists")
    
    new_user = User(
        id=str(uuid.uuid4()),
        email=request.email,
        password=request.password,
        fullName=request.fullName,
        accountType=request.accountType or "User"
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    
    return AuthResponse(
        token="mock-jwt-token",
        user=UserProfile(
            id=new_user.id, 
            email=new_user.email, 
            fullName=new_user.fullName,
            accountType=new_user.accountType
        )
    )

@router.post("/login", response_model=AuthResponse)
async def login(request: LoginRequest, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == request.email).first()
    if not user or user.password != request.password:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    
    return AuthResponse(
        token="mock-jwt-token",
        user=UserProfile(
            id=user.id, 
            email=user.email, 
            fullName=user.fullName,
            accountType=user.accountType
        )
    )
