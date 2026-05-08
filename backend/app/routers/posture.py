from fastapi import APIRouter
from ..models import Posture
from ..mock_db import db
from typing import List

router = APIRouter(prefix="/security/posture", tags=["security"])

@router.get("", response_model=List[Posture])
async def get_posture():
    return db.get_posture()
