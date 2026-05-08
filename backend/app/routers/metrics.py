from fastapi import APIRouter
from ..models import Metric
from ..mock_db import db
from typing import List

router = APIRouter(prefix="/metrics", tags=["metrics"])

@router.get("", response_model=List[Metric])
async def get_metrics():
    return db.get_metrics()
