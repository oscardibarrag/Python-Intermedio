from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

class Libro(BaseModel):
    titulo: str
    autor: str
    paginas: int
    editorial: Optional[str]

#Definir una ruta
@app.get("/")

def raiz():
    return {"Hello": "World"}


@app.get("/items/{item_id}/{m}")
def read_item(item_id: int, m: str = None):
     return {"item_id": item_id, "m":m}
#127.0.0.1:8000/items/808/hola_mundo

@app.get("/Libors/{id}")
async def mostrar_libro(id: int):
    return {"data":id}

@app.post("/Libros/")
async def insertar_libro(libro: Libro):
    return {"message": f"Libro: {libro.titulo} insertado correctamente"} 