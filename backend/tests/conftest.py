import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.main import app
from app.database import Base, get_db

from app.db_models import User, Project, Metric, Posture
from app.mock_db import PROJECTS, METRICS, POSTURE, USERS
from app.security import get_password_hash

# Use an in-memory SQLite database for testing
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

@pytest.fixture(scope="function")
def db():
    # Create the database and tables
    Base.metadata.create_all(bind=engine)
    db = TestingSessionLocal()
    try:
        # Seed test data
        for email, user_data in USERS.items():
            data = user_data.copy()
            data["password"] = get_password_hash(data["password"])
            db.add(User(**data))
        for project_data in PROJECTS:
            db.add(Project(**project_data))
        for metric_data in METRICS:
            db.add(Metric(**metric_data))
        for posture_data in POSTURE:
            db.add(Posture(**posture_data))
        db.commit()
        
        yield db
    finally:
        db.close()
        # Drop the tables after the test
        Base.metadata.drop_all(bind=engine)

@pytest.fixture(scope="function")
def client(db):
    def override_get_db():
        try:
            yield db
        finally:
            pass
    
    app.dependency_overrides[get_db] = override_get_db
    with TestClient(app) as c:
        yield c
    app.dependency_overrides.clear()
