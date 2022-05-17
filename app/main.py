from random import random
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    """
    Return Hello Github CI/CD
    """
    return {"Hello": "Github CI/CD"}

@app.get("/items/{item_id}")
def read_item(item_id: int):
    """
    Return item_id with random number
    """
    return {"item_id": item_id, "q": random()}
