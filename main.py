from enum import Enum

from fastapi import FastAPI, Query
from pydantic import BaseModel


class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"


app = FastAPI()

fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Barz"}]


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None


@app.get("/")
async def root():
    return {"message": "Hello world"}


@app.get("/items/")
async def read_items(q: str | None = Query(default=None, max_length=50, regex="^fixedquery$")):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results


@app.post("/items/")
async def create_item(item: Item):
    """
    Create item
    """
    item_dict: dict = item.dict()
    if item.tax:
        price_with_tax: float = item.price + item.tax
        item_dict.update({"price_with_tax": price_with_tax})
    return item_dict


@app.put("/items/{item_id}")
async def create_item(item_id: int, item: Item, q: str | None = None):
    result = {"item_id": item_id, **item.dict()}
    if q:
        return result.update({"q": q})
    return {"item_id": item_id, **item.dict()}


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
