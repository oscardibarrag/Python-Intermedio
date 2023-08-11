from fastapi import FastAPI

app = FastAPI()

#Definir una ruta
@app.get("/")

def raiz():
    return {"Hello": "World"}


@app.get("/items/{item_id}/{m}")
def read_item(item_id: int, m: str = None):
     return {"item_id": item_id, "m":m}
#127.0.0.1:8000/items/808/hola_mundo

