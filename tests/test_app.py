import pytest
from app import app

@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

def test_home(client):
    r = client.get("/")
    assert r.status_code == 200

def test_squad(client):
    r = client.get("/squad")
    assert r.status_code == 200

def test_results(client):
    r = client.get("/results")
    assert r.status_code == 200

def test_health(client):
    r = client.get("/api/health")
    assert r.status_code == 200
    assert b"Arsenal" in r.data

def test_api_squad(client):
    r = client.get("/api/squad")
    assert r.status_code == 200
    data = r.get_json()
    assert len(data) > 0
