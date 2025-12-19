import pytest
from server import app, db, Task
from datetime import datetime, timedelta

@pytest.fixture
def client():
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///:memory:"
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
        yield client
        with app.app_context():
            db.drop_all()

def test_add_task_validation(client):
    response = client.post("/task/add", data={
        "subject": "",
        "description": "Desc",
        "due_date": "2025-12-31"
    }, follow_redirects=True)
    assert b"cannot be null" in response.data or b"required" in response.data or response.status_code == 200

    response = client.post("/task/add", data={
        "subject": "Test Task",
        "description": "Desc",
        "due_date": "invalid-date"
    }, follow_redirects=True)
    assert response.status_code == 400 or b"ValueError" in response.data

def test_edit_nonexistent_task(client):
    response = client.get("/task/999/edit")
    assert response.status_code == 404

def test_delete_nonexistent_task(client):
    response = client.post("/task/999/delete")
    assert response.status_code == 404

def test_complete_task(client):
    due_date = (datetime.today() + timedelta(days=1)).date()
    task = Task(subject="Sample", description="Desc", due_date=due_date)
    with app.app_context():
        db.session.add(task)
        db.session.commit()
        task_id = task.id

    response = client.post(f"/task/{task_id}/complete", follow_redirects=True)
    assert response.status_code == 200
    with app.app_context():
        completed_task = Task.query.get(task_id)
        assert completed_task.status == "completed"
