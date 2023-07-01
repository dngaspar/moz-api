from fastapi import FastAPI

from models import Data

description = """
API description
"""

app = FastAPI(
    title="Project Name",
    description=description,
    version="0.0.1",
    contact={
        "name": "Author",
        "url": "https://example.com",
        "email": "admin@example.com",
    },
)


@app.get("/")
def handle_get(id: int, name: str):
    return f"GET: {id} - {name}"


@app.post("/")
def handle_post(data: Data):

    id = data.id
    name = data.name

    return f"POST: {id} - {name}"
