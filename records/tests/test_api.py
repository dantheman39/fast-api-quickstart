from fastapi.testclient import TestClient

from records.server import app


client = TestClient(app)


def test_hello():
    response = client.get("/")
    assert response.status_code == 200
    assert "message" in response.json()
