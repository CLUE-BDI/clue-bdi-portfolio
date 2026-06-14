from pydantic import BaseModel, EmailStr
from typing import List, Optional
from enum import Enum

class CategoryEnum(str, Enum):
    DEVSECOPS = "DevSecOps"
    DATA_ENGINEERING = "Data Engineering"
    CLOUD = "Cloud"

class RegisterRequest(BaseModel):
    fullName: Optional[str] = None
    email: EmailStr
    password: str
    accountType: Optional[str] = None

class LoginRequest(BaseModel):
    email: EmailStr
    password: str

class UserProfile(BaseModel):
    id: str
    email: EmailStr
    fullName: Optional[str] = None
    accountType: Optional[str] = None

class AuthResponse(BaseModel):
    token: str
    user: UserProfile

class ProjectLink(BaseModel):
    label: str
    href: str

class Project(BaseModel):
    id: str
    title: str
    category: CategoryEnum
    status: str
    description: str
    tags: List[str]
    links: List[ProjectLink]

class Metric(BaseModel):
    id: str
    value: str
    label: str

class Posture(BaseModel):
    id: str
    label: str
    note: str
    value: int

class DemoRequestCreate(BaseModel):
    name: str
    email: EmailStr
    organization: Optional[str] = None
    project_title: str
    message: Optional[str] = None

class DemoRequestResponse(BaseModel):
    id: str
    name: str
    email: EmailStr
    organization: Optional[str] = None
    project_title: str
    message: Optional[str] = None

