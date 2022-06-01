from fastapi.testclient import TestClient
import pytest

from records.server import app


client = TestClient(app)


@pytest.mark.asyncio
async def test_hello():
    response = client.get("/")
    assert response.status_code == 200
    assert "message" in response.json()


@pytest.mark.asyncio
async def test_get_albums(test_db):
    response = client.get("/albums")
    assert response.status_code == 200


@pytest.mark.asyncio
async def test_post_artist(test_db):
    response = client.post(
        "/artists",
        json={
            "name": "Jamesies",
        },
    )
    body = response.json()
    assert response.status_code == 201
    assert body["name"] == "Jamesies"
    assert type(body["id"]) is int
