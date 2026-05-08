from sqlalchemy.orm import Session
from .database import engine, Base, SessionLocal
from .db_models import User, Project, Metric, Posture
from .mock_db import PROJECTS, METRICS, POSTURE, USERS

def init_db():
    Base.metadata.create_all(bind=engine)
    
    db = SessionLocal()
    try:
        # Seed Users
        if db.query(User).count() == 0:
            for email, user_data in USERS.items():
                user = User(**user_data)
                db.add(user)
        
        # Seed Projects
        if db.query(Project).count() == 0:
            for project_data in PROJECTS:
                project = Project(**project_data)
                db.add(project)
        
        # Seed Metrics
        if db.query(Metric).count() == 0:
            for metric_data in METRICS:
                metric = Metric(**metric_data)
                db.add(metric)
        
        # Seed Posture
        if db.query(Posture).count() == 0:
            for posture_data in POSTURE:
                posture = Posture(**posture_data)
                db.add(posture)
        
        db.commit()
    except Exception as e:
        print(f"Error seeding database: {e}")
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    init_db()
