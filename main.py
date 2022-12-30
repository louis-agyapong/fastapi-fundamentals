from enum import Enum

from fastapi import FastAPI

class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello world"}


@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}
