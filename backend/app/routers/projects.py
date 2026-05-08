from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..models import Project as ProjectSchema
from ..db_models import Project
from ..database import get_db
from typing import List

router = APIRouter(prefix="/projects", tags=["projects"])

@router.get("", response_model=List[ProjectSchema])
async def get_projects(db: Session = Depends(get_db)):
    return db.query(Project).all()
