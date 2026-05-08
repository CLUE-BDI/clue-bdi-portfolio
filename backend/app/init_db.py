from sqlalchemy.orm import Session, sessionmaker
from .database import engine as default_engine, Base, SessionLocal
from .db_models import User, Project, Metric, Posture
from .mock_db import PROJECTS, METRICS, POSTURE, USERS
from .security import get_password_hash

def init_db(engine=None):
    if engine is None:
        engine = default_engine
        
    Base.metadata.create_all(bind=engine)
    
    # Create a session for the specific engine
    SessionLocalCustom = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    db = SessionLocalCustom()
    
    try:
        # Seed Users
        if db.query(User).count() == 0:
            for email, user_data in USERS.items():
                data = user_data.copy()
                data["password"] = get_password_hash(data["password"])
                user = User(**data)
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
