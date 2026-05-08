from fastapi import APIRouter, Depends, HTTPException, status
from ..models import UserProfile
from ..mock_db import db
from typing import List

router = APIRouter(prefix="/admin", tags=["admin"])

@router.get("/users", response_model=List[UserProfile])
async def get_users():
    # In a real app, we would check for admin role here
    # For this mock, we just return the users
    return db.get_all_users()
