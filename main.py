from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
import hashlib

app = FastAPI()
app.counter = 0


class HelloResp(BaseModel):
    msg: str


@app.get("/")
def root():
    return {"message": "Hello world!"}


@app.get("/counter")
def counter():
    app.counter += 1
    return app.counter


@app.get("/hello/{name}", response_model=HelloResp)
def hello_name_view(name: str):
    return HelloResp(msg=f"Hello {name}")


@app.get("/method")
def root():
    return {"method": "GET"}


@app.put("/method")
def root():
    return {"method": "PUT"}


@app.delete("/method")
def root():
    return {"method": "DELETE"}


@app.options("/method")
def root():
    return {"method": "OPTIONS"}


@app.post("/method", status_code=201)
def root():
    return {"method": "POST"}


@app.get("/auth", status_code=204)
def root(password, password_hash):
    if not hashlib.sha512(password.encode('utf-8')).hexdigest() == password_hash:
        raise HTTPException(status.HTTP_401_UNAUTHORIZED)
    else:
        return
