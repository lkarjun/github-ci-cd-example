"""Module fastai simple app."""
import random
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    """Return Hello Github CI/CD."""
    return {"Hello": "Github CI/CD"}

@app.get("/get_item")
def get_item():
    """Return random number."""
    return random.random()
