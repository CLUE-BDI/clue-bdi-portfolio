import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_get_users():
    response = client.get("/api/v1/admin/users")
    assert response.status_code == 200
    users = response.json()
    assert isinstance(users, list)
    assert len(users) >= 2
    
    # Check for specific users in mock data
    emails = [u["email"] for u in users]
    assert "admin@cluebdi.com" in emails
    assert "test@example.com" in emails
    
    # Verify UserProfile fields
    admin = next(u for u in users if u["email"] == "admin@cluebdi.com")
    assert "id" in admin
    assert "fullName" in admin
    assert "accountType" in admin
    assert admin["accountType"] == "Staff"
