import pytest
from app.app import create_app

@pytest.fixture
def client():
    app = create_app()
    app.testing = True
    with app.test_client() as client:
        yield client

def test_home(client):
    res = client.get("/")
    assert res.status_code == 200

def test_cart(client):
    res = client.get("/cart")
    assert res.status_code == 200
