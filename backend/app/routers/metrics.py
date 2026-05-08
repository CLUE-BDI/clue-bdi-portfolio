from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..models import Metric as MetricSchema
from ..db_models import Metric
from ..database import get_db
from typing import List

router = APIRouter(prefix="/metrics", tags=["metrics"])

@router.get("", response_model=List[MetricSchema])
async def get_metrics(db: Session = Depends(get_db)):
    return db.query(Metric).all()
