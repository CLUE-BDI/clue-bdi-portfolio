from fastapi import APIRouter
from ..models import Project
from ..mock_db import db
from typing import List

router = APIRouter(prefix="/projects", tags=["projects"])

@router.get("", response_model=List[Project])
async def get_projects():
    return db.get_projects()
