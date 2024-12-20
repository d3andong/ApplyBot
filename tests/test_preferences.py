import pytest
from fastapi.testclient import TestClient
from app.main import app
from sqlmodel import Session
from app.db import engine
from app.models.user import User
from app.models.user_preferences import UserPreferences

client = TestClient(app)

# We'll need a way to authenticate. Since OAuth flow is complicated to test,
# we can simulate by directly inserting a user and manually setting a token cookie.
# In a real scenario, you'd have a test for OAuth or mock the user login.
# For now, let's just create a user and a JWT offline or mock get_current_user.

from app.utils.jwt_utils import create_jwt

@pytest.fixture(name="setup_user")
def setup_user_fixture():
    # Create a test user in the db
    with Session(engine) as session:
        test_user = User(google_id="test_sub", email="test@example.com", name="Test User")
        session.add(test_user)
        session.commit()
        session.refresh(test_user)
        return test_user

def test_get_preferences_no_auth():
    # No token
    response = client.get("/preferences/")
    assert response.status_code == 401

def test_get_preferences_no_prefs(setup_user):
    # With a valid token but no prefs set
    token = create_jwt({"id": setup_user.id})
    response = client.get("/preferences/", cookies={"token": token})
    assert response.status_code == 200
    assert response.json() == {}  # no preferences yet

def test_set_preferences(setup_user):
    token = create_jwt({"id": setup_user.id})
    prefs_data = {
        "roles": ["software engineer"],
        "work_arrangement": "remote",
        "country": "USA",
        "experience_years_min": 0,
        "experience_years_max": 5
    }
    response = client.post("/preferences/", cookies={"token": token}, json=prefs_data)
    assert response.status_code == 200
    data = response.json()
    assert data["roles"] == ["software engineer"]
    assert data["work_arrangement"] == "remote"
    assert data["country"] == "USA"
    assert data["experience_years_min"] == 0
    assert data["experience_years_max"] == 5

    # Now get preferences again
    response = client.get("/preferences/", cookies={"token": token})
    assert response.status_code == 200
    data = response.json()
    assert data["roles"] == ["software engineer"]
    assert data["work_arrangement"] == "remote"
