"""Module fastai simple app."""
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    """Return Hello Github CI/CD."""
    return {"Hello": "Github CI/CD"}
