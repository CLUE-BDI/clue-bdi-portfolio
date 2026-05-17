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
        "title": "Blue/Green Security Patch Demo",
        "category": "Cloud",
        "status": "Live Demo",
        "description": "Safe vulnerable-to-patched deployment scenario showing measurable vulnerability reduction across cloud environments.",
        "tags": ["AWS", "Azure", "GCP", "Kubernetes", "Terraform"],
        "links": [
            {"label": "Architecture", "href": "#"},
            {"label": "Runbook", "href": "#"},
            {"label": "Metrics", "href": "#"}
        ]
    },
    {
        "id": "3",
        "title": "Data Engineering Zoomcamp Lab",
        "category": "Data Engineering",
        "status": "Case Study",
        "description": "End-to-end ETL workflows using Docker, Terraform, Kestra, PostgreSQL, GCS, and BigQuery analytics.",
        "tags": ["Docker", "Kestra", "Terraform", "BigQuery", "SQL"],
        "links": [
            {"label": "Writeup", "href": "#"},
            {"label": "Repo", "href": "#"},
            {"label": "Queries", "href": "#"}
        ]
    },
    {
        "id": "4",
        "title": "Cloud Data Pipeline Automation",
        "category": "Data Engineering",
        "status": "Prototype",
        "description": "Secure ingestion and analytics workflow using identity-aware access, automated processing, and dashboard visualization.",
        "tags": ["Python", "Dash", "S3", "Keycloak", "Superset"],
        "links": [
            {"label": "Overview", "href": "#"},
            {"label": "Diagram", "href": "#"},
            {"label": "Dashboard", "href": "#"}
        ]
    },
    {
        "id": "5",
        "title": "Identity Governance Automation",
        "category": "Cloud",
        "status": "In Progress",
        "description": "Automated IAM role review and remediation for multi-cloud environments using AWS Config and Lambda.",
        "tags": ["AWS", "Lambda", "Python", "IAM", "Boto3"],
        "links": [
            {"label": "Design", "href": "#"},
            {"label": "Repo", "href": "#"}
        ]
    },
    {
        "id": "6",
        "title": "Serverless Security Scanner",
        "category": "DevSecOps",
        "status": "Beta",
        "description": "Real-time vulnerability scanning for AWS Lambda functions and S3 buckets with automated alerting.",
        "tags": ["Serverless", "Security", "AWS", "EventBridge"],
        "links": [
            {"label": "Demo", "href": "#"},
            {"label": "Docs", "href": "#"}
        ]
    }
]

METRICS = [
    {"id": "1", "value": "12+", "label": "Security tools integrated"},
    {"id": "2", "value": "5", "label": "Cloud platforms demonstrated"},
    {"id": "3", "value": "8", "label": "Portfolio-ready projects"},
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
