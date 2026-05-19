from fastapi.testclient import TestClient
from app.main import app


client = TestClient(app)

def test_create_task():
    response = client.post("/tasks", json={
        "title": "Write CI system",
        "description": "Build real pipeline",
        "priority": 3
    })
    assert response.status_code == 200
    assert response.json()["title"] == "Write CI system"

def test_task_flow():
    r = client.post("/tasks", json={"title": "Test"})
    task_id = r.json()["id"]

    r2 = client.patch(f"/tasks/{task_id}", json={"completed": True})
    assert r2.json()["completed"] is True
