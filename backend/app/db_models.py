from sqlalchemy import Column, Integer, String, JSON, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(String, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    password = Column(String, nullable=False)
    fullName = Column(String)
    accountType = Column(String)

class Project(Base):
    __tablename__ = "projects"

    id = Column(String, primary_key=True, index=True)
    title = Column(String, nullable=False)
    category = Column(String, nullable=False)
    status = Column(String, nullable=False)
    description = Column(String, nullable=False)
    tags = Column(JSON, nullable=False)  # List[str]
    links = Column(JSON, nullable=False) # List[Dict]

class Metric(Base):
    __tablename__ = "metrics"

    id = Column(String, primary_key=True, index=True)
    value = Column(String, nullable=False)
    label = Column(String, nullable=False)

class Posture(Base):
    __tablename__ = "postures"

    id = Column(String, primary_key=True, index=True)
    label = Column(String, nullable=False)
    note = Column(String, nullable=False)
    value = Column(Integer, nullable=False)
