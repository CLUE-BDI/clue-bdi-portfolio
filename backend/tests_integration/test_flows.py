import pytest

def test_full_user_flow(client):
    # 1. Register a new user
    register_data = {
        "email": "integration_test@example.com",
        "password": "securepassword123",
        "fullName": "Integration Tester",
        "accountType": "User"
    }
    reg_response = client.post("/api/v1/auth/register", json=register_data)
    assert reg_response.status_code == 201
    assert "token" in reg_response.json()
    assert reg_response.json()["user"]["email"] == register_data["email"]

    # 2. Login with the new user
    login_data = {
        "email": "integration_test@example.com",
        "password": "securepassword123"
    }
    login_response = client.post("/api/v1/auth/login", json=login_data)
    assert login_response.status_code == 200
    token = login_response.json()["token"]
    assert token == "mock-jwt-token"

    # 3. Fetch projects (public endpoint)
    proj_response = client.get("/api/v1/projects")
    assert proj_response.status_code == 200
    # Since it's a fresh DB, it might be empty unless seeded. 
    # But startup event in main.py calls init_db() which seeds.
    assert isinstance(proj_response.json(), list)
    assert len(proj_response.json()) > 0

def test_admin_access_control(client):
    # 1. Register a staff user
    staff_data = {
        "email": "staff_member@example.com",
        "password": "staffpassword123",
        "fullName": "Staff User",
        "accountType": "Staff"
    }
    client.post("/api/v1/auth/register", json=staff_data)

    # 2. Login as staff
    login_response = client.post("/api/v1/auth/login", json={
        "email": "staff_member@example.com",
        "password": "staffpassword123"
    })
    assert login_response.json()["user"]["accountType"] == "Staff"

    # 3. Access admin users list
    admin_response = client.get("/api/v1/admin/users")
    assert admin_response.status_code == 200
    users = admin_response.json()
    assert any(u["email"] == "staff_member@example.com" for u in users)

def test_invalid_login_flow(client):
    # Try login with wrong password
    login_data = {
        "email": "integration_test@example.com",
        "password": "wrongpassword"
    }
    response = client.post("/api/v1/auth/login", json=login_data)
    assert response.status_code == 401
    assert response.json()["detail"] == "Invalid credentials"
