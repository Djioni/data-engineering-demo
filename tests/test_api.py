from fastapi.testclient import TestClient
from app.main import app


client = TestClient(app)

def test_get_users():
    response = client.get("/users")
    assert response.status_code == 200
    users = response.json()
    assert isinstance(users, list)
    

def test_get_orders():
    response = client.get("/orders")
    assert response.status_code == 200
    orders = response.json()
    assert isinstance(orders, list)
    

def test_run_etl():
    response = client.post("/etl")
    assert response.status_code == 200
    assert response.json() == {"message": "ETL workflow started"}