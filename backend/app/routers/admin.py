from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from ..models import UserProfile
from ..db_models import User
from ..database import get_db
from typing import List

router = APIRouter(prefix="/admin", tags=["admin"])

@router.get("/users", response_model=List[UserProfile])
async def get_users(db: Session = Depends(get_db)):
    # In a real app, we would check for admin role here
    # For this mock, we just return the users
    return db.query(User).all()
