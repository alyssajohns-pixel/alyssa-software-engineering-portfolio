from fastapi.testclient import TestClient

from portfolio_api.api import app


def test_health():
    with TestClient(app) as client:
        response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_analyze_endpoint():
    with TestClient(app) as client:
        response = client.post(
            "/analyze",
            json={"change_id": "api-1", "files": {"a.py": "print('x')\n"}},
        )
    assert response.status_code == 200
    body = response.json()
    assert body["change_id"] == "api-1"
    assert body["findings"][0]["kind"] == "debug-print"
