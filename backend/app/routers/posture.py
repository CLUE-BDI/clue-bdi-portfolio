from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..models import Posture as PostureSchema
from ..db_models import Posture
from ..database import get_db
from typing import List

router = APIRouter(prefix="/security/posture", tags=["security"])

@router.get("", response_model=List[PostureSchema])
async def get_posture(db: Session = Depends(get_db)):
    return db.query(Posture).all()
