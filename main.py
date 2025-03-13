from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel

class Item(BaseModel):
    name: str
    description: str = None
    price: float
    tax: float = None

items = []

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/items")
def create_item(item: Item):
    items.append(item)
    return item

@app.get("/items/{item_id}")
def read_item(item_id: int):
    return items[item_id]

@app.get("/items")
def list_items():
    return items
