from fastapi.testclient import TestClient

import pytest

from main import app

client = TestClient(app)


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello world!"}


@pytest.mark.parametrize("name", ["Zenek", "Marek", "Alojzy Niezdąży"])
def test_hello_name(name):
    response = client.get(f"/hello/{name}")
    assert response.status_code == 200
    assert response.json() == {"msg": f"Hello {name}"}


def test_counter():
    response = client.get(f"/counter")
    assert response.status_code == 200
    assert response.text == "1"
    # 2nd Try
    response = client.get(f"/counter")
    assert response.status_code == 200
    assert response.text == "2"
    # 3rd Try
    response = client.get(f"/counter")
    assert response.status_code == 200
    assert response.text == "3"

def test_method_get():
    response = client.get("/method")
    assert response.status_code == 200
    assert response.json() == {"method": "GET"}

def test_method_put():
    response = client.put("/method")
    assert response.status_code == 200
    assert response.json() == {"method": "PUT"}

def test_method_options():
    response = client.options("/method")
    assert response.status_code == 200
    assert response.json() == {"method": "OPTIONS"}

def test_method_delete():
    response = client.delete("/method")
    assert response.status_code == 200
    assert response.json() == {"method": "DELETE"}

def test_method_post():
    response = client.post("/method")
    assert response.status_code == 201
    assert response.json() == {"method": "POST"}

@pytest.mark.parametrize("password", ["haslo", "Marek", "haslo123"])
@pytest.mark.parametrize("password_hash", ["013c6889f799cd986a735118e1888727d1435f7f623d05d58c61bf2cd8b49ac90105e5786ceaabd62bbc27336153d0d316b2d13b36804080c44aa6198c533215", "f34ad4b3ae1e2cf33092e2abb60dc0444781c15d0e2e9ecdb37e4b14176a0164027b05900e09fa0f61a1882e0b89fbfa5dcfcc9765dd2ca4377e2c794837e091", "Alojzy Niezdąży"])
def test_auth(password, password_hash):
    response = client.get(f"/auth?password={password}&password_hash={password_hash}")
    assert response.status_code == 204 or 401