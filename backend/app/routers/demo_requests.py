import uuid
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from ..models import DemoRequestCreate, DemoRequestResponse
from ..db_models import DemoRequest
from ..database import get_db
from typing import List

router = APIRouter(prefix="/demo-requests", tags=["demo-requests"])

@router.post("", response_model=DemoRequestResponse, status_code=status.HTTP_201_CREATED)
async def create_demo_request(payload: DemoRequestCreate, db: Session = Depends(get_db)):
    try:
        new_request = DemoRequest(
            id=str(uuid.uuid4()),
            name=payload.name,
            email=payload.email,
            organization=payload.organization,
            project_title=payload.project_title,
            message=payload.message
        )
        db.add(new_request)
        db.commit()
        db.refresh(new_request)
        return new_request
    except Exception as e:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Failed to create demo request: {str(e)}"
        )
