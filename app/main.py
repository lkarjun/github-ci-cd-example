from fastapi import FastAPI
from random import random

app = FastAPI()


@app.get("/")
def read_root():
    """return Hello Github CI/CD"""
    return {"Hello": "Github CI/CD"}


@app.get("/items/{item_id}")
def read_item(item_id: int):
    """return item_id with random number"""
    return {"item_id": item_id, "q": random()}
