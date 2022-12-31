from enum import Enum

from fastapi import FastAPI
from pyexpat import model


class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"


app = FastAPI()

fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Barz"}]


@app.get("/")
async def root():
    return {"message": "Hello world"}

@app.get("/item/")
async def read_item(skip: int = 0, limit: int = 10): 
    return fake_items_db[skip : skip + limit]


@app.get("/items/{item_id}")
async def read_items(item_id: str, needy: str, skip: int = 0, limit: int | None = None):
    item = {"item_id": item_id, "needy": needy, "skip": skip, "limit": limit}
    return item


@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    """
    Predefined values using Enum
    """
    if model_name is ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}

    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}

    return {"model_name": model_name, "message": "Have some residuals"}


@app.get("/path/{file_path:path}")
async def read_file(file_path: str):
    """
    Path parameters containing path
    """
    return {"file_path": file_path}
