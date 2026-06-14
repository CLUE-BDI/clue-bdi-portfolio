def test_read_main(client):
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to CLUE BDI Portfolio API"}

def test_get_projects(client):
    response = client.get("/api/v1/projects")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert len(response.json()) > 0

def test_get_metrics(client):
    response = client.get("/api/v1/metrics")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert len(response.json()) > 0

def test_get_posture(client):
    response = client.get("/api/v1/security/posture")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert len(response.json()) > 0

def test_register_and_login(client):
    # Register
    register_data = {
        "email": "newuser@example.com",
        "password": "password123",
        "fullName": "Test User"
    }
    reg_response = client.post("/api/v1/auth/register", json=register_data)
    assert reg_response.status_code == 201
    assert "token" in reg_response.json()
    
    # Login
    login_data = {
        "email": "newuser@example.com",
        "password": "password123"
    }
    login_response = client.post("/api/v1/auth/login", json=login_data)
    assert login_response.status_code == 200
    assert login_response.json()["token"] == "mock-jwt-token"

def test_login_invalid_credentials(client):
    login_data = {
        "email": "nonexistent@example.com",
        "password": "wrongpassword"
    }
    response = client.post("/api/v1/auth/login", json=login_data)
    assert response.status_code == 401

def test_demo_requests(client):
    # Submit a demo request
    payload = {
        "name": "Jane Recruiter",
        "email": "recruiter@hiring.com",
        "organization": "Top Talent Corp",
        "project_title": "Veteran Vitality Assistant",
        "message": "We would like to see a demo of this assistant."
    }
    response = client.post("/api/v1/demo-requests", json=payload)
    assert response.status_code == 201
    data = response.json()
    assert "id" in data
    assert data["name"] == payload["name"]
    assert data["email"] == payload["email"]
    assert data["project_title"] == payload["project_title"]

    # Verify that admin can fetch it
    admin_response = client.get("/api/v1/admin/demo-requests")
    assert admin_response.status_code == 200
    requests_list = admin_response.json()
    assert len(requests_list) > 0
    assert any(req["name"] == payload["name"] for req in requests_list)

