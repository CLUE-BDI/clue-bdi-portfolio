from typing import List, Dict
import uuid

# Initial mock data
PROJECTS = [
    {
        "id": "1",
        "title": "PipelineGuard",
        "category": "DevSecOps",
        "status": "Featured",
        "description": "CI/CD security scanning and analytics platform that normalizes findings from Trivy, Checkov, Semgrep, and Gitleaks.",
        "tags": ["GitLab CI", "Trivy", "Checkov", "BigQuery", "Looker"],
        "links": [
            {"label": "Demo", "href": "#"},
            {"label": "Repo", "href": "https://github.com/CLUE-BDI/pipelineguard"},
            {"label": "Dashboard", "href": "https://datastudio.google.com/reporting/ff3831fe-285a-48bb-9083-e52df6721c00"}
        ]
    },
    {
        "id": "2",
        "title": "CLUE-BDI Portfolio",
        "category": "Cloud",
        "status": "Live Demo",
        "description": "A dynamic, full-stack portfolio hub for showcasing cloud engineering projects, security automation, and data intelligence dashboards.",
        "tags": ["React", "FastAPI", "Tailwind CSS", "Python", "TypeScript"],
        "links": [
            {"label": "Repo", "href": "https://github.com/CLUE-BDI/clue-bdi-portfolio"}
        ]
    },
    {
        "id": "3",
        "title": "Hantavirus Global Tracker",
        "category": "Data Engineering",
        "status": "Live Demo",
        "description": "Containerized real-time SSR epidemiological surveillance platform that coordinates CDC, WHO, PAHO, and ECDC indicators.",
        "tags": ["React 19", "Bun", "FastAPI", "PostgreSQL", "Docker Compose", "Leaflet"],
        "links": [
            {"label": "Repo", "href": "https://github.com/CLUE-BDI/global-tracker-spark"}
        ]
    }
]

METRICS = [
    {"id": "1", "value": "12+", "label": "Security tools integrated"},
    {"id": "2", "value": "5", "label": "Cloud platforms demonstrated"},
    {"id": "3", "value": "3", "label": "Portfolio-ready projects"},
    {"id": "4", "value": "Cloud · Data · Security", "label": "Focus areas"},
    {"id": "5", "value": "100%", "label": "Infrastructure as Code"}
]

POSTURE = [
    {"id": "1", "label": "Secrets detected", "note": "Reduced", "value": 92},
    {"id": "2", "label": "IaC misconfigurations", "note": "Reduced", "value": 78},
    {"id": "3", "label": "Container findings", "note": "Tracked", "value": 100},
    {"id": "4", "label": "IAM Over-privileged", "note": "Remediated", "value": 65}
]

USERS: Dict[str, Dict] = {
    "admin@cluebdi.com": {
        "id": "admin-1",
        "email": "admin@cluebdi.com",
        "password": "password123",
        "fullName": "Admin User",
        "accountType": "Staff"
    },
    "test@example.com": {
        "id": "test-1",
        "email": "test@example.com",
        "password": "password123",
        "fullName": "Test User",
        "accountType": "Recruiter"
    }
}

class MockDB:
    def get_projects(self):
        return PROJECTS

    def get_metrics(self):
        return METRICS

    def get_posture(self):
        return POSTURE

    def add_user(self, user_data: Dict):
        user_id = str(uuid.uuid4())
        user_data["id"] = user_id
        USERS[user_data["email"]] = user_data
        return user_data

    def get_user_by_email(self, email: str):
        return USERS.get(email)

    def get_all_users(self):
        return list(USERS.values())

db = MockDB()
