"""Basic API tests using FastAPI's TestClient."""

from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_health_check() -> None:
    """The health endpoint should return status ok."""
    response = client.get("/api/health")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"


def test_index_page() -> None:
    """The root page should render the chat UI."""
    response = client.get("/")
    assert response.status_code == 200
    assert "text/html" in response.headers["content-type"]


def test_chat_requires_message() -> None:
    """An empty message should be rejected."""
    response = client.post("/api/chat", json={"message": ""})
    assert response.status_code in (400, 422)
