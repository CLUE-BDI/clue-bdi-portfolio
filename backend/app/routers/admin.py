from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from ..models import UserProfile, DemoRequestResponse
from ..db_models import User, DemoRequest
from ..database import get_db
from typing import List

router = APIRouter(prefix="/admin", tags=["admin"])

@router.get("/users", response_model=List[UserProfile])
async def get_users(db: Session = Depends(get_db)):
    # In a real app, we would check for admin role here
    # For this mock, we just return the users
    return db.query(User).all()

@router.get("/demo-requests", response_model=List[DemoRequestResponse])
async def get_demo_requests(db: Session = Depends(get_db)):
    # Return all demo requests stored in the database
    return db.query(DemoRequest).all()

