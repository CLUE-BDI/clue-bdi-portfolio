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
